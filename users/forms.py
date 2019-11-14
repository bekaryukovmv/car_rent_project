from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from allauth.account.forms import AddEmailForm


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('email', 'username', 'user_lang',)


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('email', 'username', 'user_lang',)


# class MyCustomSignupForm(SignupForm):
    
#     def save(self, request):
#         user = super(MyCustomSignupForm, self).save(request)
