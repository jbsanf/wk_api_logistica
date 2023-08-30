from rest_framework import viewsets
from .models import Shipper
from .serializers import ShipmentSerializer


class ShipperViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Shipper.objects.all()
    serializer_class = ShipmentSerializer