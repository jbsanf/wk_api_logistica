from rest_framework import routers
from .viewsets import ShipmentViewSet
router = routers.SimpleRouter()

router.register(r'shippers', ShipmentViewSet)

urlpatterns = router.urls