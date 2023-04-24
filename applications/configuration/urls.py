from rest_framework.routers import DefaultRouter
from .views import ConfigurationView

router = DefaultRouter()
router.register('', ConfigurationView)

urlpatterns = []
urlpatterns.extend(router.urls)
