from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, get_list_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm

# Create your views here.


def instructions(request):
    """ A view to return the instructions page """

    recipes = Recipe.objects.all()

    template = 'instructions/instructions.html'

    context = {
        'recipes': recipes
    }

    return render(request, template, context)


@login_required
def add_recipe(request):
    """ Add a recipe to the instructions page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added recipe!')
            return redirect(reverse('instructions'))
        else:
            messages.error(request, 'Failed to add recipe. \
                Please ensure the form is valid.')
    else:
        form = RecipeForm()

    template = 'instructions/add_recipe.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_recipe(request, recipe_id):
    """ Edit a recipe in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated recipe!')
            return redirect(reverse('instructions'))
        else:
            messages.error(request, 'Failed to update recipe. \
                Please ensure the form is valid.')
    else:
        form = RecipeForm(instance=recipe)
        messages.info(request, f'You are editing {recipe.name}')

    template = 'instructions/edit_recipe.html'
    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, template, context)


@login_required
def delete_recipe(request, recipe_id):
    """ Delete a recipe from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    messages.success(request, 'Recipe deleted!')
    return redirect(reverse('instructions'))
