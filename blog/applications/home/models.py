"""Modelos de la aplicación Home"""
from django.db import models
# App terceros
from model_utils.models import TimeStampedModel
# Create your models here.


class Home(TimeStampedModel):
    """Modelo para datos de la pantalla Home"""
    title = models.CharField('Nombre', max_length=30)
    descripcion = models.TextField()
    about_title = models.CharField('Titulo Nosotros', max_length=50)
    about_text = models.TextField()
    contact_email = models.EmailField(
        'Email de contacto', blank=True, null=True)
    phone = models.CharField('Telefono contacto', max_length=20)

    class Meta:
        verbose_name = 'Página Principal'
        verbose_name_plural = 'Página Principal'

    def __str__(self):
        return self.title


class Suscribers(TimeStampedModel):
    """Modelo que recibe los suscriptores"""
    email = models.EmailField()

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.email


class Contact(TimeStampedModel):
    """Modelo para formulario de contacto"""
    full_name = models.CharField('Nombres', max_length=60)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensaje'

    def __str__(self):
        return self.full_name
