from django.shortcuts import render
from django.http import HttpResponse 

rev = [
    {
        'user': 'cslee95',
        'res_name': 'Cute and Comfy!',
        'review': 'I love it here! Def will come again!',
        'date_posted': 'April 1, 2019',
    },
    {
        'user': 'supercarolineXD',
        'res_name': 'The New Central Park!',
        'review': 'Bring your friends, 10/10 would recommend!!',
        'date_posted': 'April 2, 2019',
    },
]

def index(request):
    context = {
        'rev': rev
    }
    return render(request, 'reviews/index.html', context)
              

def about(request):
    return render(request, 'reviews/about.html', {'title': 'About'})

