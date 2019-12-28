from rest_framework.routers import DefaultRouter

from bucket.views import BucketViewSet

router = DefaultRouter()
router.register(r'bucket', BucketViewSet, base_name='bucket')
