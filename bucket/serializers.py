from rest_framework import serializers

from bucket.models import Bucket


class BucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        exclude = ('created_on', 'updated_on')
