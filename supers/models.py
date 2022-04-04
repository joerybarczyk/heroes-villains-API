from django.db import models
from super_types.models import SuperType

# Create your models here.
class Power(models.Model):
    name = models.CharField(max_length=255)

class Super(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    powers = models.ManyToManyField(Power)
    catchphrase = models.CharField(max_length=255)
    super_type = models.ForeignKey(SuperType, on_delete=models.CASCADE)

