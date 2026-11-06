from rest_framework.routers import DefaultRouter
from .project_views import ProjectViewSet
router = DefaultRouter()
router.register('', ProjectViewSet, basename='project')
urlpatterns = router.urls
