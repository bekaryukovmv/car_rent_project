from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('email', 'username', 'user_lang',)


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email', 'username', 'user_lang',)


class UserFormForEdit(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'user_lang')


class MyCustomSignupForm(SignupForm):
    user_lang = forms.ChoiceField(choices=(('ru', 'Русский'),
        ('en', 'English'),), required=True, label='Язык')

    def signup(self, request, user):
        user_lang = self.cleaned_data['user_lang']
        user,save()
        return user
