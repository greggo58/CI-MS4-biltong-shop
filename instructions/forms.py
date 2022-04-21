""" Recipe forms """
from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """ RecipeForm Class """
    class Meta:
        """ Meta Class """
        model = Recipe
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
