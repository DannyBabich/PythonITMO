from django.core.paginator import Paginator
from .opensky_api import *
from django.shortcuts import render, get_object_or_404
from .models import Aircraft
from datetime import datetime, timedelta
from django.utils.timezone import make_aware, now
from math import radians, cos, sin, sqrt, atan2

# Радиус Земли в морских милях
R = 3440.065


# Функция для расчета расстояния (haversine)
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


# Определим интервал времени для обновления данных
UPDATE_INTERVAL = timedelta(minutes=30)


# Функция для получения данных о состоянии воздушных судов
def fetch_aircraft_data(bbox=None):
    # Проверяем, когда были обновлены данные в последний раз
    last_aircraft = Aircraft.objects.order_by('-last_updated').first()
    if last_aircraft is not None and (now() - last_aircraft.last_updated) < UPDATE_INTERVAL:
        return  # Если данные были обновлены недавно, не делаем запрос к API

    api = OpenSkyApi()
    if bbox:
        states = api.get_states(bbox=bbox)  # Ограничиваем зону поиска с помощью bbox
    else:
        states = api.get_states()

    if states is not None:
        for s in states.states:
            last_contact_time = datetime.utcfromtimestamp(s.time_position) if s.time_position else None
            if last_contact_time is not None:
                last_contact_time = make_aware(last_contact_time)

            Aircraft.objects.update_or_create(
                icao24=s.icao24,
                defaults={
                    'callsign': s.callsign.strip() if s.callsign else None,
                    'origin_country': s.origin_country,
                    'longitude': s.longitude,
                    'latitude': s.latitude,
                    'altitude': s.geo_altitude,
                    'velocity': s.velocity,
                    'heading': s.true_track,
                    'last_contact': last_contact_time,
                    'last_updated': now(),  # Обновляем время последнего обновления данных
                }
            )


# Главная страница со списком воздушных судов
def aircraft_list(request):
    fetch_aircraft_data()  # Обновление данных о воздушных судах

    # Получаем параметры из запроса
    center_lat = request.GET.get('center_lat')
    center_lon = request.GET.get('center_lon')
    radius = request.GET.get('radius')

    if radius and not (center_lat and center_lon):
        return render(request, 'aircraft_list.html', {
            'error': 'Если указан радиус, необходимо указать широту и долготу центра.'
        })

    # Получаем список всех воздушных судов
    aircrafts = Aircraft.objects.all().order_by('icao24')

    # Фильтрация по координатам, если они указаны (без радиуса)
    if center_lat and center_lon and not radius:
        aircrafts = [ac for ac in aircrafts if ac.latitude and ac.longitude and
                     ac.latitude == center_lon and ac.longitude == center_lat]

    # Фильтрация по координатам и радиусу, если они указаны
    if center_lat and center_lon and radius:
        aircrafts = [ac for ac in aircrafts if ac.latitude and ac.longitude and
                     haversine(center_lon, center_lat, ac.latitude, ac.longitude) <= radius]

    # Пагинация результатов
    paginator = Paginator(aircrafts, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'aircraft_list.html', {'page_obj': page_obj, 'aircrafts': aircrafts})


# Поиск воздушных судов с учётом фильтрации
def search_aircraft(request):
    query = request.GET.get('q')  # Поиск по позывному или стране
    center_lat = request.GET.get('center_lat')
    center_lon = request.GET.get('center_lon')
    radius = request.GET.get('radius')

    # Проверяем, что если введен радиус, то введены и широта, и долгота
    if radius and not (center_lat and center_lon):
        return render(request, 'search_results.html', {
            'error': 'Если указан радиус, необходимо указать широту и долготу центра.'
        })

    # Получаем все воздушные суда
    aircrafts = Aircraft.objects.all().order_by('icao24')

    # Поиск по позывному или стране
    if query:
        aircrafts = aircrafts.filter(callsign__icontains=query) | aircrafts.filter(origin_country__icontains=query)

    # Фильтрация по координатам, если они указаны (без радиуса)
    if center_lat and center_lon and not radius:
        center_lat, center_lon = float(center_lat), float(center_lon)
        aircrafts = [ac for ac in aircrafts if ac.latitude and ac.longitude and
                     ac.latitude == center_lon and ac.longitude == center_lat]

    # Фильтрация по координатам и радиусу, если они указаны
    if center_lat and center_lon and radius:
        center_lat, center_lon = float(center_lat), float(center_lon)
        radius = float(radius)
        print(center_lat, center_lon, radius)
        aircrafts = [ac for ac in aircrafts if ac.latitude and ac.longitude and
                     haversine(center_lon, center_lat, ac.latitude, ac.longitude) <= radius]

    # Пагинация результатов
    paginator = Paginator(aircrafts, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'search_results.html', {'page_obj': page_obj, 'aircrafts': aircrafts})


# Страница с подробной информацией
def aircraft_detail(request, icao24):
    aircraft = get_object_or_404(Aircraft, icao24=icao24)
    return render(request, 'aircraft_detail.html', {'aircraft': aircraft})
