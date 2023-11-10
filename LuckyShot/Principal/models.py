from django.db import models

import json
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=25, unique=True, default='')
    apellido_paterno = models.CharField(max_length=25, default='')  
    apellido_materno = models.CharField(max_length=25, default='')  
    nombres = models.CharField(max_length=50, default='') 
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=50)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    edad = models.IntegerField()

    def __str__(self):  
        return f"{self.id_usuario} - {self.nombre_usuario}"  


'''
class UsuarioVIP(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    beneficios_vip = models.JSONField(default=dict)

    def str(self):
        return f"VIP - {self.usuario.nombre}"
'''
class Apuesta(models.Model):
    id_apuesta = models.AutoField(primary_key=True)
    nombre_apuesta = models.CharField(max_length=100, default='')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_apuesta = models.DateTimeField(auto_now_add=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def str(self):
        return f"{self.IdApuesta} - Usuario: {self.IdUsuario.nombre}, Monto: {self.Monto}"
    
class TipoApuesta(models.Model):
    idTipo = models.AutoField(primary_key=True)
    idApuesta = models.ForeignKey(Apuesta, on_delete=models.CASCADE)
    DescripcionTipo = models.CharField(max_length=100)

    def str(self):
        return f"{self.idTipo} - Apuesta: {self.idApuesta.IdApuesta}, Descripcion: {self.DescripcionTipo}"
    
class ApuestaEvento(models.Model):
    idApuesta = models.OneToOneField(Apuesta, on_delete=models.CASCADE, primary_key=True)
    idTipo = models.ForeignKey(TipoApuesta, on_delete=models.CASCADE)
    idEvento = models.ForeignKey('Evento', on_delete=models.CASCADE)  # 'Evento' se coloca entre comillas para evitar problemas de importación circular
    Monto = models.DecimalField(max_digits=10, decimal_places=2)
    ESTADO_EVENTO_CHOICES = [
        ('FUTURO', 'Futuro'),
        ('ACTIVO', 'Activo'),
        ('TERMINADO', 'Terminado'),
    ]
    EstadoEvento = models.CharField(max_length=10, choices=ESTADO_EVENTO_CHOICES, default='FUTURO')

    def str(self):
        return f"Apuesta: {self.idApuesta.IdApuesta}, Tipo: {self.idTipo.DescripcionTipo}, Evento: {self.idEvento.NombreEvento}, Monto: {self.Monto}, Estado: {self.EstadoEvento}"
    
class Evento(models.Model):
    idEvento = models.AutoField(primary_key=True)
    idDeporte = models.ForeignKey('Deporte', on_delete=models.CASCADE)  # 'Deporte' se coloca entre comillas para evitar problemas de importación circular
    NombreEvento = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    ESTADO_EVENTO_CHOICES = [
        ('FUTURO', 'Futuro'),
        ('ACTIVO', 'Activo'),
        ('TERMINADO', 'Terminado'),
    ]
    EstadoEvento = models.CharField(max_length=10, choices=ESTADO_EVENTO_CHOICES, default='FUTURO')

    def str(self):
        return f"{self.NombreEvento} ({self.idDeporte.NombreDeporte}), Fecha: {self.fecha}, Estado: {self.EstadoEvento}"

class Deporte(models.Model):
    idDeporte = models.AutoField(primary_key=True)
    Deporte = models.CharField(max_length=50)

    def str(self):
        return self.Deporte
    
class Participante(models.Model):
    idParticipante = models.AutoField(primary_key=True)
    NombreParticipante = models.CharField(max_length=100)
    idDeporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)

    def str(self):
        return f"{self.NombreParticipante} ({self.idDeporte.Deporte})"