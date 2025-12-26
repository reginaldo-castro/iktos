from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Perfil(models.TextChoices):
        ADMIN = 'admin', 'Administrador'
        TECNICO = 'tecnico', 'Técnico'
    
    perfil = models.CharField(max_length=10, choices=Perfil.choices, default=Perfil.TECNICO)