from django.urls import path
from .views import HomePageView, CarCreateView


urlpatterns = [
    path('', HomePageView.as_view(), name='lang_ch'),
    path('home/', HomePageView.as_view(), name='home'),
    path('create_car/', CarCreateView.as_view(), name='create_car'),
]
