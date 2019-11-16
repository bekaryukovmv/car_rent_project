from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_auth.registration.serializers import RegisterSerializer

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'user_lang',)


class CustomRegisterSerializer(RegisterSerializer):
    user_lang = serializers.ChoiceField([('ru', 'Русский'),
        ('en', 'English'),])

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['user_lang'] = self.validated_data.get('user_lang', '')
        return data_dict
