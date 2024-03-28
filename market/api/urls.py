from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('statistics', StaticModelViewSet, basename='statistics')
urlpatterns = router.urls
