from django.urls import path
from .views import *

urlpatterns = [
    path('', vetmag_main, name='vetmag_main'),
    path('login/', vetmag_login, name='vetmag_login'),
    path('registration/', vetmag_registration, name='vetmag_registration'),
    path('personal_area/', vetmag_personal_area, name='vetmag_personal_area'),
    path('logout/', logout_view, name='logout'),  # Для выхода из аккаунта
    path('catalogue/', vetmag_catalogue, name='vetmag_catalogue'),
]
