""" Models for Products, Categories, and Reviews """
from django.db import models

# Create your models here.


class Recipe(models.Model):
    """ Class for recipe and instructions """
    recipe_class = models.CharField('Class', max_length=1)
    name = models.CharField('Name', max_length=50)
    summary = models.CharField('Summary', max_length=500, blank=True)
    requirements = models.TextField('Requirements', blank=True)
    steps = models.TextField('Steps', blank=True)

    class Meta:
        """ Meta class for biltong recipies """
        ordering = ['recipe_class']
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipies'

    def __str__(self):
        return f'{self.name}'

    def requirements_as_list(self):
        """ Split requirements text field into and an array """
        return self.requirements.split('>')

    def steps_as_list(self):
        """ Split steps text field into and an array """
        return self.steps.split('>')
