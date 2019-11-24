import logging

from django.contrib.auth import get_user_model, authenticate
from django.db import IntegrityError
from rest_framework import status as http_status
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from constants.api_response_messages import INVALID_CREDENTIALS, INVALID_REQUEST, USER_EXISTS
from core.permissions import IsUser
from core.serializers import UserSerializer
from core.utils import get_api_success_response, get_api_error_response

LOG = logging.getLogger(__name__)


class UserViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['login', 'signup']:
            return [AllowAny()]
        return super(UserViewSet, self).get_permissions() + [IsUser()]

    @action(methods=['post'], detail=False)
    def login(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            LOG.info("User %s has logged in successfully", user)
            return get_api_success_response(data=self.get_serializer(user).data)
        else:
            LOG.info("Invalid credentials provided by user: %s", username)
            return get_api_error_response(INVALID_CREDENTIALS)

    @action(methods=['post'], detail=False)
    def signup(self, request, *args, **kwargs):
        try:
            username = request.data.pop('username')
            user = get_user_model().objects.create(username=username)
            password = request.data.pop('password')
            user.set_password(password)
            serializer_obj = self.get_serializer(user, data=request.data, partial=True)
            if serializer_obj.is_valid(raise_exception=True):
                serializer_obj.save()
            LOG.info("Successfully registered user %s", user)
            return get_api_success_response(data=serializer_obj.data, status=http_status.HTTP_201_CREATED)
        except KeyError as key:
            LOG.error("%s is absent in the request body", key, exc_info=True)
            return get_api_error_response(INVALID_REQUEST)
        except IntegrityError as error:
            LOG.error("User %s already exists", username)
            return get_api_error_response(USER_EXISTS)
