from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('login/', views.login, name='login'),
    # ex: /polls/5/
    path('/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('home/', views.index, name='index'),
    # ex: /polls/5/vote/
    path('cadastro/', views.cadastro, name='cadastro'),

    path('login/submit/', views.submit_login)
]