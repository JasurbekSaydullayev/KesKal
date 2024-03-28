from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductView, basename='product')
urlpatterns = router.urls
