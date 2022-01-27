from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.utils.timezone import now

# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to='media')
    published = models.DateTimeField(default=now, verbose_name='Fecha de Publicación')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = 'Servicios'
        verbose_name_plural = 'Servicios'
        ordering = ['-created']

    def __str__(self):
        return self.title