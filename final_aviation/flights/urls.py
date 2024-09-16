from django.urls import path
from . import views

urlpatterns = [
    path('', views.aircraft_list, name='aircraft_list'),
    path('search/', views.search_aircraft, name='search_aircraft'),  # Страница с результатами поиска
    path('aircraft/<str:icao24>/', views.aircraft_detail, name='aircraft_detail'),
]