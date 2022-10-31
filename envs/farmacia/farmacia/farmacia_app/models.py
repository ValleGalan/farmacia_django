from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.


class Farmacia(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='farmacia')
    ubicacion = models.CharField(max_length=255)
    localidad = models.CharField(max_length=255)
    turno_date = models.DateField()
    turno_time = models.TimeField()

   # turno = models.ForeignKey(
       # 'turno.Turno', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre