from django.urls import path

from .views import UserList,UserDetail,CarList

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
    path('<int:pk>/cars', CarList.as_view()),
]
