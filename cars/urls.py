from django.urls import path
from .views import CarCreateView, CarListView, AddCarUser


urlpatterns = [
    path('', CarListView.as_view(), name='home'),
    path('create_car/', CarCreateView.as_view(), name='create_car'),
    path('<int:pk>/add_car/', AddCarUser.as_view(), name='add_car'),
]
