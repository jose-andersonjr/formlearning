import email
from django import forms 

# ============ CONSTANTES =============
CHOICES_SEXO = (
    ('m','Masculino'), #O primeiro valor é como a variável a ser inserida no banco de dados, o segundo valor é como será exibido ao usuário
    ('f','Feminino'),
    ('n','Nenhumas das alternativas')
)

CHOICES_COR =(
    ('pt','Preto'),
    ('pd', 'Pardo'),
    ('i', 'Índio'),
    ('b', 'Branco'),
)

# ============= Classe do formulário =============
class FormularioPrincipal(forms.Form): #o FormularioPrincipal herdará o atributo forms da classe Form
    # Campos do formulário
    email = forms.EmailField(required=False)
    nome = forms.CharField(max_length=30)
    sexo = forms.ChoiceField(choices=CHOICES_SEXO, required=True)
    cor = forms.ChoiceField(choices=CHOICES_COR)
    idade = forms.IntegerField()
    data_nascimento = forms.DateField(required=False, error_messages={'invalid': "Insira uma data no formato DD/MM/AAAA"})