from django.shortcuts import render
from .models import Areas
from .forms import AreasForm

def inicial(request):
	return render(request, 'home.html')

def perfil(request):
	return render(request, 'perfil.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):

	return render(request, 'cadastro.html')

def contato(request):
	return render(request, 'contato.html')


def areas_listar(request):
	areas = Areas.objects.all()
	contexto = {
	    'areas_listar': areas

	}
	return render(request, 'areas.html', contexto)

def areas_cadastrar(request):

	if request.POST:
		pass
	else:
		form = AreasForm()
		contexto = {
		    'form' : form
		}
	return render(request, 'cadastro_areas.html', contexto)

