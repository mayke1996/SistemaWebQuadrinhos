
from django.contrib import admin
from django.urls import include, path
from quandrinhosApp import views

urlpatterns = [
	path('', include('quandrinhosApp.urls')),
    path('admin/', admin.site.urls),
    path('login/submit', views.index)
    
]
