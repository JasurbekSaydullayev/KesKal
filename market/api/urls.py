from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('markets', MarketModelViewSet, basename='data3')
router.register('statisticks', StaticModelViewSet, basename='data4')
urlpatterns = router.urls

