from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class Parentesco(models.Model):
    nombre = models.CharField('Parentesco', max_length=50)

    class Meta:
        verbose_name = 'Parentesco'
        verbose_name_plural = 'Parentescos'

    def __str__(self):
        return self.nombre

class TipoIdentificacion(models.Model):
    nombre = models.CharField('Tipo identificación', max_length=50)

    class Meta:
        verbose_name = 'TipoIdentificacion'
        verbose_name_plural = '-TipoIdentificaciones'

    def __str__(self):
        return self.nombre


class Acompanante(models.Model):
    tipoIdentificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.CASCADE)
    numIdentificacion = models.CharField('Número identificación', max_length=50)
    nombreP = models.CharField('Primer Nombre', max_length=50, blank=True, null=True)
    nombreS = models.CharField('Segundo Nombre', max_length=50, blank=True, null=True)
    apellidoP = models.CharField('Primer Apellido', max_length=50, blank=True, null=True)
    apellidoS = models.CharField('Segundo Apellido', max_length=50, blank=True, null=True)
    municipioHabitual = models.CharField('Municipio de residencia', max_length=50, blank=True, null=True)
    direccionHabitual = models.CharField('Dirección de residencia', max_length=50, blank=True, null=True)
    telefono = models.CharField('telefono', max_length=50, blank=True, null=True)
    parentesco_id = models.ForeignKey(Parentesco, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Acompañante'
        verbose_name_plural = 'Acompañantes'

    def __str__(self):
        return self.numIdentificacion

class Profesional(models.Model):
    numIdentificacion = models.CharField('Número identificación', max_length=50)
    nombreP = models.CharField('Primer Nombre', max_length=50)
    nombreS = models.CharField('Segundo Nombre', max_length=50)
    apellidoP = models.CharField('Primer Apellido', max_length=50)
    apellidoS = models.CharField('Segundo Apellido', max_length=50)
    telefono = models.CharField('telefono', max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'

    def __str__(self):
        return self.numIdentificacion

class Afiliado(models.Model):
    numIdentificacion = models.CharField('Número identificación', max_length=50, blank=True, null=True)
    tipoIdentificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.CASCADE, blank=True, null=True)
    numCarnet = models.CharField('Número de carné', max_length=50)
    nombreP = models.CharField('Primer Nombre', max_length=50, blank=True, null=True)
    nombreS = models.CharField('Segundo Nombre', max_length=50, blank=True, null=True)
    apellidoP = models.CharField('Primer Apellido', max_length=50, blank=True, null=True)
    apellidoS = models.CharField('Segundo Apellido', max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Afiliado'
        verbose_name_plural = 'Afiliados'

    def __str__(self):
        return self.numIdentificacion


class Servicio_Remitido(models.Model):
    servRemId = models.CharField('Id servicio', max_length=50)
    nombre = models.CharField('Nombre Servicio',  max_length=50, blank=True, null=True)
    codigoReps = models.CharField('Código REPS',  max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.servRemId


class Remision_Contraremision(models.Model):
    RemiContId = models.CharField('Id remision', max_length=50)
    Afil_numIdentificacion = models.ForeignKey(Afiliado, on_delete=models.CASCADE)
    Acom_numIdentificacion = models.ForeignKey(Acompanante, on_delete=models.CASCADE)
    Prof_numIdentificacion = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    ServRem_id = models.ForeignKey(Servicio_Remitido, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'remision'
        verbose_name_plural = 'remisiones'

    def __str__(self):
        return self.RemiContId



