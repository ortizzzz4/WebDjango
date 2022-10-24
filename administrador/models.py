from operator import mod
from django.db import models

class Registro(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    residencia=models.CharField(max_length=200)
    image=models.ImageField(upload_to='fotos/', null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    numero_identificacion=models.IntegerField()
    
    
    
    class Meta : 
        verbose_name = "registro"
        verbose_name_plural = "registros"
    
    def __str__(self) :
        return f'Registro : { self.nombre }'    