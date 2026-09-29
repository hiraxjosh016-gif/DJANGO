from rest_framework.routers import DefaultRouter
from .views import TaskViewsets

router = DefaultRouter()
router.register('tasks', TaskViewsets)

urlpatterns = router.urls