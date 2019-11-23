import logging

from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from constants.api_response_messages import INVALID_CREDENTIALS
from core.serializers import UserSerializer
from core.utils import get_api_success_response, get_api_error_response

LOG = logging.getLogger(__name__)


class UserViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    @action(methods=['post'], detail=False)
    def login(self, request, *args, **kwargs):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = get_user_model().objects.get(username=username, password=password)
            return get_api_success_response(data=self.get_serializer(user).data)
        except get_user_model().DoesNotExist:
            LOG.info("Invalid credentials provided by user %s", username)
            return get_api_error_response(INVALID_CREDENTIALS)
