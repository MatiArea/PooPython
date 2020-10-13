from django.db import models

class Venta(models.Model):
    nombreMedicamento = models.CharField(max_length=25)
    droga = models.CharField(max_length=25)
    obraSocial = models.CharField(max_length=25)
    plan = models.CharField(max_length=25)
    importe = models.FloatField(default=0)
    fechaHoraVenta = models.DateTimeField()
