# Create your models here.
from django.db import models
from django.db.models import CASCADE

from bucket.models import Bucket
from core.models import ModelBase


class ToDo(ModelBase):
    """
    Model to store user ToDos
    """
    bucket = models.ForeignKey(Bucket, on_delete=CASCADE)
    done = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=256)

    class Meta:
        """
        Meta properties of Bucket
        """
        db_table = 'to_do'
        verbose_name = 'To Do'
        verbose_name_plural = 'ToDos'

    def __str__(self):
        name = self.title
        if self.done:
            name += ":Done"
        return name
