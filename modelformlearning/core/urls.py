from django.urls import include, path, re_path
from modelformlearning.core import views #Importe as views da sua aplicação


# Insira os urls das views aqui 
urlpatterns = [
    path('home', views.formulario, name='formulario')
]

