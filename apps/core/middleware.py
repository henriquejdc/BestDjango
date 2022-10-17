from re import sub
from django.conf import settings
from django.utils import translation

from apps.accounts.models import UserProfile


# from rest_framework.authtoken.models import Token


class LanguageMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs) -> None:
        user = None
        # header_token = request.META.get('HTTP_AUTHORIZATION', None)
        # if header_token is not None:
        #     try:
        #         token = sub('Token ', '', request.META.get('HTTP_AUTHORIZATION', None))
        #         token_obj = Token.objects.get(key=token)
        #         user = token_obj.user
        #     except Token.DoesNotExist:
        #         pass
        if not user:
            user = getattr(request, 'user', None)
        if user is not None and user.is_authenticated:
            try:
                active_language = UserProfile.objects.get(user=user).active_language
            except UserProfile.DoesNotExist:
                active_language = settings.LANGUAGE_CODE

            translation.activate(active_language)
            request.LANGUAGE_CODE = translation.get_language()
