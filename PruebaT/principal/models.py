from django.db import models

# Create your models here.
class Ticket(models.Model):
	id = models.AutoField(primary_key=True)
	precio = models.CharField(max_length=30)
	pelicula = models.ForeignKey('pelicula', on_delete=models.CASCADE)


class Pelicula(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=50)
	def __str__(self):
		return self.nombre