from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', GetMethod, basename='data')
urlpatterns = router.urls
