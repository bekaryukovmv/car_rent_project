from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

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
    user_lang = forms.ChoiceField(choices=settings.LANGUAGES, required=True, label=_('Язык'))

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.user_lang = self.cleaned_data['user_lang']
        user.save()
        return user
