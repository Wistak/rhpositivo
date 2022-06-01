from django import forms
from .models import Prospecto, Estatus


class NuevoProspecto(forms.ModelForm):
    nombre = forms.CharField()
    apepat = forms.CharField()
    apemat = forms.CharField()
    calle = forms.CharField()
    num = forms.CharField()
    colonia = forms.CharField()
    cp = forms.CharField()
    tel = forms.CharField()
    rfc = forms.CharField()

    class Meta:
        model = Prospecto
        fields = '__all__'

class EvaluarProspecto(forms.ModelForm):

    ESTATUS_CHOICES= [
    ('1', 'Enviado'),
    ('2', 'Autorizado'),
    ('3', 'Rechazado'),
    ]

    estatus = forms.CharField(label='Estatus: ', widget=forms.Select(choices=ESTATUS_CHOICES))
    observaciones = forms.CharField(label='Observaciones: ', widget=forms.Textarea, required=False)

    class Meta:
        model = Prospecto
        fields = ['estatus', 'observaciones']

