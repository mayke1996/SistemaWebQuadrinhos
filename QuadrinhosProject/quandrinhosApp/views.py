from django.http import HttpResponse
from django.template import loader
from .models import info_quadrinhos


def index(request):
    latest_question_list = info_quadrinhos.objects.order_by('id')[:5]
    template = loader.get_template('quandrinhosApp/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, id):
    return HttpResponse("You're looking at question %s." % info_quadrinhos_id)

def login(request):
    return HttpResponse(response % info_quadrinhos_id)

def vote(request, id):
    return HttpResponse("You're voting on question %s." % info_quadrinhos_id)


