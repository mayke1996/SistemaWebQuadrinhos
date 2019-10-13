from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('/login/', views.login, name='login'),
    # ex: /polls/5/vote/
    path('/vote/', views.vote, name='vote'),
]