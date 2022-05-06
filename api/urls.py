from django.urls import path
from api import views

urlpatterns = [
    path('venues/', views.load_venue_data),
    path('contacts/', views.load_close_contact_list),
]