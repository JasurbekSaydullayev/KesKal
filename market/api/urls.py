from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('statistics', StaticModelViewSet, basename='statistics')
router.register('markets', MarketSerializer, basename='markets')
urlpatterns = router.urls
