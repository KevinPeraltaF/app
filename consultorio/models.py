from django.contrib.auth.models import User
from django.db import models
#
genero_masculino = 1
genero_femenino = 2
GENERO_CHOICE = (
    (genero_masculino,"Masculino"),
    (genero_femenino,"Femenino"),

)
# Create your models here.
class ModeloBase(models.Model):
    usuario_creacion = models.ForeignKey(User, verbose_name='Usuario Creación', blank=True, null=True, on_delete= models.CASCADE, related_name='+', editable=False)
    fecha_creacion = models.DateTimeField(verbose_name='Fecha creación',auto_now_add=True)
    fecha_modificacion = models.DateTimeField(verbose_name='Fecha Modificación', auto_now=True)
    usuario_modificacion = models.ForeignKey(User, verbose_name='Usuario Modificación', blank=True, null=True, on_delete= models.CASCADE, related_name='+', editable=False)
    status = models.BooleanField(verbose_name="Estado del registro", default=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        usuario = None
        if len(args):
            usuario = args[0].user.id
        if self.id:
            self.usuario_modificacion_id = usuario
        else:
            self.usuario_creacion_id = usuario
        models.Model.save(self)

class Persona(ModeloBase):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    Apellido1 = models.CharField(verbose_name="1º Apellido", max_length=250)
    Apellido2 = models.CharField(verbose_name="2º Apellido", max_length=250)
    Nombre1 = models.CharField(verbose_name="1º Nombre", max_length=250)
    Nombre2 = models.CharField(verbose_name="2º Nombre", max_length=250)
    cedula = models.CharField(verbose_name="Cédula", max_length=10,unique=True)
    email = models.EmailField(verbose_name="Correo Electrónico", unique=True)
    fecha_nacimiento = models.DateField(verbose_name="Fecha Nacimiento")
    genero = models.IntegerField(verbose_name="Género", choices=GENERO_CHOICE)



