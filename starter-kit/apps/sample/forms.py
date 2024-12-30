from django import forms
from .models import Candidato, Vaga
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    ext = value.name.split('.')[-1].lower()
    valid_extensions_foto = ['jpg', 'jpeg', 'png']
    valid_extensions_curriculo = ['pdf', 'doc', 'docx', 'txt']

    if value.field.name == 'foto' and ext not in valid_extensions_foto:
        raise ValidationError('Formato de arquivo não suportado para foto.')
    elif value.field.name == 'curriculo' and ext not in valid_extensions_curriculo:
        raise ValidationError('Formato de arquivo não suportado para currículo.')


class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['titulo']


class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ['nome', 'email', 'telefone', 'vaga_interesse', 'observacoes', 'processo_selecao', 'resultado', 'foto', 'curriculo']

