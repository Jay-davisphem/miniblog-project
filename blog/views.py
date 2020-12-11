from django.shortcuts import render

# Create your views here.
def index(request):
    """View function for blog homepage"""
    context  = {
        'author': 'David Oluwafemi',
    }
    return render(request, 'index.html', context=context)
