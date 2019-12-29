"""
Base models
"""
from django.conf import settings
from django.db import models
from django.db.models import CASCADE


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


class UserLoginHistory(ModelBase):
    """
    Model for maintaining user login history
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    browser_name = models.CharField(null=True, blank=True, max_length=128)
    os = models.CharField(null=True, blank=True, max_length=128)
    browser_version = models.CharField(null=True, blank=True, max_length=128)

    def __str__(self):
        return "%s : %s" % (self.user, self.created_on)

    class Meta:
        """
        Meta properties of UserLoginHistory
        """
        db_table = 'user_login_history'
        verbose_name = 'User Login History'
        verbose_name_plural = 'User Login History'
