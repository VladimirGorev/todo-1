from django import forms
from todo_item.models import ListItem


class ItemForm(forms.ModelForm):

    expare_date = forms.DateField(
        widget=forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = ListItem
        fields = ('name', 'list_model', 'expare_date')
