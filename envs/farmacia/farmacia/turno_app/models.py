from django.db import models

# Create your models here.
class Turno(models.Model):
    localizacion = models.CharField(max_length=255)
    turno_date = models.DateField()
    turno_time = models.TimeField()

    #foranea
    farmacia = models.ForeignKey(
        'farmacia_app.Farmacia', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.localizacion