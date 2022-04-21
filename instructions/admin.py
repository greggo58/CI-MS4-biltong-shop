""" Products admin """
from django.contrib import admin
from .models import Recipe

# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    """ A list of Recipe fields to display """
    list_display = (
        'recipe_class',
        'name',
        'summary',
        'requirements',
        'steps',
    )

    ordering = ('recipe_class',)


admin.site.register(Recipe, RecipeAdmin)
