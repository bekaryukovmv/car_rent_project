from django.urls import path
from .views import CarCreateView, home


urlpatterns = [
    path('', home, name='home'),
    path('create_car/', CarCreateView.as_view(), name='create_car'),
]
