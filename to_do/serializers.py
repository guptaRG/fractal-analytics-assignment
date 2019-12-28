from rest_framework import serializers

from bucket.serializers import BucketSerializer
from to_do.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    bucket_id = serializers.IntegerField(write_only=True, required=False)

    def to_representation(self, instance):
        data = super(ToDoSerializer, self).to_representation(instance)
        if instance.bucket.name:
            data['bucket'] = BucketSerializer(instance.bucket).data
        else:
            del data['bucket']
        return data

    class Meta:
        model = ToDo
        exclude = ('created_on', 'updated_on')
        read_only_fields = ('bucket',)
        write_only_fields = ('bucket_id',)
        required_fields = ('title', 'description')
