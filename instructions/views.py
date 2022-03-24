from django.shortcuts import render

# Create your views here.


def instructions(request):
    """ A view to return the instructions page """

    return render(request, 'instructions/instructions.html')
