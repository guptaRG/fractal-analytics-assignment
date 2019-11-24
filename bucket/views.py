# Create your views here.
import logging

from rest_framework import status as http_status
from rest_framework import viewsets, mixins

from bucket.models import Bucket
from bucket.serializers import BucketSerializer
from constants.api_response_messages import CREATE_BUCKET_ERROR
from core.permissions import IsUser
from core.utils import get_api_success_response, get_api_error_response

LOG = logging.getLogger(__name__)


class BucketViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    permission_classes = (IsUser,)
    serializer_class = BucketSerializer

    def get_queryset(self):
        return Bucket.objects.filter(user=self.request.user, name__isnull=False)

    def create(self, request, *args, **kwargs):
        data = request.data
        data.update(user=request.user.id)
        serializer_obj = self.get_serializer(data=data)
        if serializer_obj.is_valid(raise_exception=True):
            serializer_obj.save()
            LOG.info("Created new bucket %s for user %s", data["name"], request.user)
            return get_api_success_response(data=serializer_obj.data, status=http_status.HTTP_201_CREATED)
        LOG.error("Something went wrong while creating new bucket %s for user %s", data["name"], request.user)
        return get_api_error_response(message=CREATE_BUCKET_ERROR)
