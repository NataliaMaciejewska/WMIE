from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password


class HashedPasswordAuthBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        user_model = get_user_model()

        try:
            user = user_model.objects.using('users').get(email=username)
            correct_password = check_password(password, user.password)
            if user is not None and correct_password:
                return user
            else:
                return None
        except user_model.DoesNotExist:
            return None

    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            return user_model.objects.using('users').get(pk=user_id)
        except user_model.DoesNotExist:
            return None
