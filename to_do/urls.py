from rest_framework.routers import DefaultRouter

from to_do.views import ToDoViewSet

router = DefaultRouter()
router.register(r'to-do', ToDoViewSet, base_name='to_do')
