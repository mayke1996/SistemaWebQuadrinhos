from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import info_quadrinhos, usuario

#@login_required
def index(request):
	listQuadrinhos = info_quadrinhos.objects.all()[:200]
	template = loader.get_template('quandrinhosApp/index.html')
	context = {
		'listQuadrinhos': listQuadrinhos,
	}
	return HttpResponse(template.render(context, request))

def detail(request, id):
	return HttpResponse("You're looking at question %s.", info_quadrinhos.id)

def login(request):
	return render(request, 'quandrinhosApp/login.html')

def cadastro(request):
	return render(request, 'quandrinhosApp/cadastro.html')

@csrf_protect
def submit_login(request):
	if request.method == 'POST':
		usuario = authenticate(email=request.POST['email'], password=request.POST['password'])
		if usuario is not None:
			login(request, usuario)
			return redirect('/home')
	return render(request, 'quandrinhosApp/login.html')


