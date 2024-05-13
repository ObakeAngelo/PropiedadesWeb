from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class EmpresaCorredora(AbstractUser):
    rut_empresa = models.CharField(max_length=50, primary_key=True)
    telefono = models.CharField(max_length=15)
    razon_social = models.CharField(max_length=100)
    giro = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.rut_empresa} - {self.username}"
    
    