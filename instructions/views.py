from django.shortcuts import render
from .models import Recipe

# Create your views here.


def instructions(request):
    """ A view to return the instructions page """

    recipes = Recipe.objects.all()
    
    template = 'instructions/instructions.html'
    
    context = {
        'recipes': recipes
    }

    return render(request, template, context)
