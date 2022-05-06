from django.urls import path
from api import views

urlpatterns = [
    path('', views.load_venue_data),
]