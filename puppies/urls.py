from rest_framework.routers import DefaultRouter

from .views import PuppiesViewSet

router = DefaultRouter()

router.register('puppies', PuppiesViewSet, base_name='puppies')

urlpatterns = router.urls
