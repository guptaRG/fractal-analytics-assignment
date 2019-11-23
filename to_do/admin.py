# Register your models here.

from django.contrib import admin

from to_do.models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    """
    Class registering model ToDo to django admin with properties representing the visibility of the same.
    """
    list_display = ('id', 'title', 'bucket', 'done')

    class Meta:
        """
        Admin class meta to define the model name
        """
        model = ToDo


admin.site.register(ToDo, ToDoAdmin)
