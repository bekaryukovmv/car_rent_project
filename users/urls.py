from django.urls import path
from .views import UserDetail, userform_edit, DeleteUser, add_car

app_name = 'users'

urlpatterns = [
    path('<int:pk>/', UserDetail.as_view(), name='dashboard'),
    path('<int:pk>/edit/', userform_edit, name='user_edit'),
    path('<int:pk>/delete', DeleteUser.as_view(), name='user_delete'),
    path('add_car/<int:car_pk>/', add_car, name='add_car'),
]
