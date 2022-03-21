from django.db import models

# Create your models here.


class propiedades(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    nombrePropiedad = models.CharField(max_length=40, null=True)

    def __str__(self):
        return"{0}".format(self.nombrePropiedad)
    tipos = [
        ('Cas', 'Casa'),
        ('Dep', 'Departamento'),
        ('Vil', 'Villa'),
        ('Res', 'Residencia'),
        ('Ofi', 'Oficina'),
        ('Ter', 'Terreno'),
        ('Bod', 'Bodega'),
        ('Des', 'Desarrollo'),
        ('Edi', 'Edificio')
    ]
    tipoPropiedad = models.CharField(
        max_length=3, choices=tipos, default='Cas')
    operaciones = [
        ('V', 'Venta'),
        ('R', 'Renta')
    ]
    tipOperacion = models.CharField(
        max_length=1, choices=operaciones, default='V')
    descripcion = models.TextField(max_length=2000, null=False, blank=False)
    ubicacion = models.CharField(max_length=35, null=False, blank=False)
    costo = models.SlugField(max_length=255, null=False)
    habitaciones = models.IntegerField(default=0, null=False, blank=False)
    banos = models.IntegerField(default=0, null=False, blank=False)
    estacionamientos = models.IntegerField(default=0, null=False, blank=False)
    metrosTerreno = models.IntegerField(default=0, null=False, blank=False)
    metrosConstruccion = models.IntegerField(
        default=0, null=False, blank=False)
    pisos = models.IntegerField(blank=True)
