from django.urls import path, include

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('detail/', views.detail, name='detail'),
    path('home/', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/submit/', views.index, name='homePage'),
    

]