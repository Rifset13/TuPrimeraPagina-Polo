from django.db import models

# Create your models here.

class Insumo(models.Model): 
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    cantidad_en_stock = models.IntegerField()




class Productos(models.Model): 
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()
    cantidad_en_stock = models.IntegerField()
    
    
class Atencion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion_del_problema = models.TextField()