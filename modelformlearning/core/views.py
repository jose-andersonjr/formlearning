from email import message
from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from modelformlearning.core import forms
from django.contrib import messages
from modelformlearning.core.forms import FormularioPrincipal

# Create your views here.
def formulario(request):
    template_name='formulario.html'
    form = FormularioPrincipal(request.POST)
    if request.method == "POST":
        if form.is_valid(): #se o form for válido ele é processado da maneira que está
            print(form.cleaned_data) #aqui é onde acontece o form.save()
            form = FormularioPrincipal() # e então o formulário é renovado para que não seja exibido novamente na página
            messages.success(request, 'Os dados foram enviados com sucesso')
            context = {
                'form':form
            } 
            return render (request, template_name, context=context)
    context = {
        'form':form
    }
    form = FormularioPrincipal()
    return render (request, template_name, context=context)
        
    
