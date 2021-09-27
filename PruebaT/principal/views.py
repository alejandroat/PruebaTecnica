from django.shortcuts import render, redirect
from .models import Ticket, Pelicula
from .form import PeliculaForm, TicketForm

def inicio(request):
	ticket = Ticket.objects.all()
	pelicula = Pelicula.objects.all()
	contexto= {
		'tickets': ticket,
		'peliculas': pelicula,
	}
	return render(request, "inicio.html", contexto)

def crearpelicula(request):
	if request.method == 'GET':
		forms = PeliculaForm()
		contexto = {
			'form': forms
		}
	else:
		form = PeliculaForm(request.POST)
		contexto = {
			'form': form
		}
		if form.is_valid():
			form.save()
			return redirect('inicio')
	return render(request, "crearPelicula.html",contexto)

def crearticket(request):
	if request.method == 'GET':
		forms = TicketForm()
		contexto = {
			'form': forms
		}
	else:
		form = TicketForm(request.POST)
		contexto = {
			'form': form
		}
		if form.is_valid():
			form.save()
			return redirect('inicio')
	return render(request, "crearTicket.html",contexto)

def editarpelicula(request,id):
	pelicula = Pelicula.objects.get(id = id)
	if request.method == 'GET':
		form = PeliculaForm(instance=pelicula)
		contexto = {
			'form': form
		}
	else:
		form = PeliculaForm(request.POST, instance=pelicula)
		contexto = {
			'form': form
		}
		if form.is_valid():
			form.save()
			return redirect('inicio')
	return render(request,"crearPelicula.html", contexto)

def eliminarpelicula(request,id):
	pelicula = Pelicula.objects.get(id = id)
	pelicula.delete()
	return redirect('inicio')

def editarticket(request,id):
	ticket = Ticket.objects.get(id = id)
	if request.method == 'GET':
		form = TicketForm(instance=ticket)
		contexto = {
			'form': form
		}
	else:
		form = TicketForm(request.POST, instance=ticket)
		contexto = {
			'form': form
		}
		if form.is_valid():
			form.save()
			return redirect('inicio')
	return render(request,"crearTicket.html", contexto)

def eliminarticket(request,id):
	ticket = Ticket.objects.get(id = id)
	ticket.delete()
	return redirect('inicio')