from django.contrib.auth import get_user_model
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
