# Create your views here.
import logging

from django.contrib.auth.models import AnonymousUser
from rest_framework import status as http_status
from rest_framework import viewsets, mixins
from rest_framework.exceptions import PermissionDenied

from bucket.models import Bucket
from constants.api_response_messages import INVALID_BUCKET, INVALID_USER
from core.permissions import IsUser
from core.utils import get_api_error_response
from to_do.models import ToDo
from to_do.serializers import ToDoSerializer

LOG = logging.getLogger(__name__)


class ToDoViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = ToDoSerializer
    permission_classes = (IsUser,)

    def get_queryset(self):
        if isinstance(self.request.user, AnonymousUser):
            LOG.error("No user could be authorized in this request: %s", self.basename)
            raise PermissionDenied(INVALID_USER)
        return ToDo.objects.select_related('bucket').filter(bucket__user=self.request.user)

    def create(self, request, *args, **kwargs):
        bucket_id = request.data.get('bucket_id')
        if bucket_id:
            if not Bucket.objects.filter(id=bucket_id, user=request.user).exists():
                LOG.error("Bucket with id %s doesn't exist for user %s", bucket_id, request.user)
                return get_api_error_response(message=INVALID_BUCKET, status=http_status.HTTP_404_NOT_FOUND)
        else:
            bucket, _ = Bucket.objects.get_or_create(user=request.user, name=None)
            request.data.update(bucket_id=bucket.id)
        return super(ToDoViewSet, self).create(request, *args, **kwargs)
