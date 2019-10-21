from django.http import HttpResponse
from django.template import loader
from .models import info_quadrinhos, usuario


def index(request):
	listQuadrinhos = info_quadrinhos.objects.all()[:200]
	template = loader.get_template('quandrinhosApp/index.html')
	context = {
		'listQuadrinhos': listQuadrinhos,
	}
	return HttpResponse(template.render(context, request))

def detail(request, id):
	return HttpResponse("You're looking at question %s." % info_quadrinhos_id)

def login(request):
	listUsuarios = usuario.objects.all()
	template = loader.get_template('quandrinhosApp/login.html')
	context = {
		'listUsuarios': listUsuarios,
	}
	return HttpResponse(template.render(context, request))

def cadastro(request, id):
	return HttpResponse("You're voting on question %s." % info_quadrinhos_id)


