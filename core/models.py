from django.db import models


class ModelBase(models.Model):
    """
    Abstract model class to register default fields to children models
    """
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        """
        Meta properties of ModelBase
        """
        abstract = True
