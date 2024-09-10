from django.db import models
#Comentario de prueba si
# Create your models here.

# Tabla TBL_GENERO

class Genero(models.Model):
    tipo = models.CharField(max_length=45,null=True)

    class Meta:
        db_table = 'TBL_GENERO'

class Persona(models.Model):
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL,null=True)
    nombre = models.CharField(max_length=150, null=True)
    apellido = models.CharField(max_length=150, null=True)
    fecha_nacimiento = models.DateField(null=True)

    class Meta:
        db_table = 'TBL_PERSONA'