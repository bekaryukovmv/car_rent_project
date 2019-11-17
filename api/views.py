from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.utils import translation

from rest_framework import generics


from .serializers import UserSerializer, CarSerializer
from .permissions import IsUserSuperuserOrReadOnly
from cars.models import Car
# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all().order_by('pk')
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsUserSuperuserOrReadOnly,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class CarList(generics.ListAPIView):
    model = Car
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    
    def get_queryset(self):
        queryset = super(CarList, self).get_queryset()
        return queryset.filter(owner__pk=self.kwargs.get('pk'))


def change_lang(request):
    if request.user.is_authenticated:
        user_language = request.user.user_lang
        translation.activate(user_language)
        request.session[translation.LANGUAGE_SESSION_KEY] = user_language
        return redirect('api')
    return redirect('home')
