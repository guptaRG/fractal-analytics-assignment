from django.contrib import admin

from core.models import UserLoginHistory


class UserLoginHistoryAdmin(admin.ModelAdmin):
    """
    Class registering model Bucket to django admin with properties representing the visibility of the same.
    """
    list_display = ('user', 'browser_name', 'browser_version', 'os', 'created_on', 'updated_on')

    class Meta:
        """
        Admin class meta to define the model name
        """
        model = UserLoginHistory


admin.site.register(UserLoginHistory, UserLoginHistoryAdmin)
