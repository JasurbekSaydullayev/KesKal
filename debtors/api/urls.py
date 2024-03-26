from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('debtors', DebtorsModelViewSet, basename='data2')
urlpatterns = router.urls