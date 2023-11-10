from django.contrib import admin
from Principal import models
# Register your models here.

@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nombre_usuario', 'nombres', 'apellido_paterno', 'apellido_materno', 'correo', 'saldo', 'edad')
    search_fields = ['id_usuario', 'nombre_usuario', 'correo']

@admin.register(models.Apuesta)
class ApuestaAdmin(admin.ModelAdmin):
    list_display = ('id_apuesta', 'nombre_apuesta', 'id_usuario', 'monto', 'fecha_apuesta')
    search_fields = ['id_apuesta', 'nombre_apuesta']
