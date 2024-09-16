from django.http import HttpResponseRedirect
from django.urls import path, include

urlpatterns = [
    path('flights/', include('flights.urls')),
    path('', lambda request: HttpResponseRedirect('/flights/')),
]
