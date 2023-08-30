import uuid
from django.db import models


class Shipment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data = models.JSONField('Data')
    shipper = models.ForeignKey(
        'Shipper',
        on_delete=models.CASCADE,
        related_name='shipments'
    )


class Shipper(models.Model):
    cnpj = models.CharField('CNPJ', unique=True)
    name = models.CharField('Name')