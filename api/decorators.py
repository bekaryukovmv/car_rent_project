from django.utils import translation
from django.shortcuts import redirect


class ChangeLangMixin:
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_language = request.user.user_lang
            translation.activate(user_language)
            request.session[translation.LANGUAGE_SESSION_KEY] = user_language
            return super().get(request, *args, **kwargs)
        else:
            return redirect('rest_framework:login')
