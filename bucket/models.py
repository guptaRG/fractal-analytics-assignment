# Create your models here.

from django.conf import settings
from django.db import models
from django.db.models import CASCADE

from core.models import ModelBase


class Bucket(ModelBase):
    """
    Optional Bucket to segregate user ToDos
    """
    name = models.CharField(max_length=128)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    description = models.TextField()

    class Meta:
        """
        Meta properties of Bucket
        """
        db_table = 'bucket'
        verbose_name = 'Bucket'
        verbose_name_plural = 'Buckets'
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name
