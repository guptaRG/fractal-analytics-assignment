# Register your models here.

from django.contrib import admin

from bucket.models import Bucket


class BucketAdmin(admin.ModelAdmin):
    """
    Class registering model Bucket to django admin with properties representing the visibility of the same.
    """
    list_display = ('id', 'name', 'user')

    class Meta:
        """
        Admin class meta to define the model name
        """
        model = Bucket


admin.site.register(Bucket, BucketAdmin)
