import uuid

from django.db import models

class Joya(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero = models.PositiveIntegerField(default=0, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False, blank=False)