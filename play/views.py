from django.shortcuts import render

# Create your views here.
def play(request):
    lis_t = [
        'Love',
        'Hatred',
        'Pleasure',
        'Happiness',
        'Sadness',
        'Craziness',
        'Greed',
        'Contempt'
    ]

    return render(request, 'play.html', context={'lis_t': lis_t})
