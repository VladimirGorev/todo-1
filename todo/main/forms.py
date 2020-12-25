from django import forms
from main.models import ListModel


class ListForm(forms.ModelForm):

    class Meta:
        model = ListModel
        fields = ('name', 'user')
