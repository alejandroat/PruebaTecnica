from django import forms
from .models import Pelicula, Ticket

class PeliculaForm(forms.ModelForm):
	class Meta:
		model = Pelicula
		fields = '__all__'


class TicketForm(forms.ModelForm):
	class Meta:
		model = Ticket
		fields = '__all__'