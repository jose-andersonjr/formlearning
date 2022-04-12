from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from modelformlearning.core import forms
from modelformlearning.core import forms
from modelformlearning.core.forms import FormularioPrincipal

# Create your views here.
def formulario(request):
    form = FormularioPrincipal()
    context = {
        'form':form
    }
    template_name='formulario.html'
    return render(request, template_name, context=context)