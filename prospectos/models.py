from django.db import models

# Create your models here.

class Estatus(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Prospecto(models.Model):
    nombre = models.CharField(max_length=200)
    apepat = models.CharField(max_length=200)
    apemat = models.CharField(max_length=200)
    calle = models.CharField(max_length=200)
    num = models.CharField(max_length=20)
    colonia = models.CharField(max_length=200)
    cp = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    rfc = models.CharField(max_length=11)
    estatus = models.ForeignKey(Estatus, on_delete=models.CASCADE, default=1, blank=True)
    observaciones = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return (self.nombre + ' ' + self.apepat)