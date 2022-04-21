from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from modelformlearning.core import forms
from modelformlearning.core import forms
from modelformlearning.core.forms import FormularioPrincipal

# Create your views here.
def formulario(request):
    template_name='formulario.html'
    if request.method == "POST":
        form = FormularioPrincipal(request.POST)
        print(form.data['nome'])
        context = {
            'form':form
        }
        return render(request, template_name, context=context)
    else:
        form = FormularioPrincipal()
        context = {
            'form':form
        }
        return render(request, template_name, context=context)
