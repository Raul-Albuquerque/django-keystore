from django.db import models


# Create your models here.
class Keystore(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    client_ip = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.key} = {self.value}"
