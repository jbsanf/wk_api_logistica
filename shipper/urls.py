from rest_framework import routers
from .viewsets import ShipperViewSet
router = routers.SimpleRouter()

router.register(r'shippers', ShipperViewSet)

urlpatterns = router.urls