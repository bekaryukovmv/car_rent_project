from django.urls import path
from .views import UserDetail, UserDelete, UserUpdate

app_name = 'users'

urlpatterns = [
    path('<int:pk>/', UserDetail.as_view(), name='dashboard'),
    path('<int:pk>/edit/', UserUpdate.as_view(), name='user_edit'),
    path('<int:pk>/delete', UserDelete.as_view(), name='user_delete'),
]
