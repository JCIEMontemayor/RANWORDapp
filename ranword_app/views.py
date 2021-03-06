from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def random_word(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    else:
        request.session['count'] += 1
    request.session['rword'] = get_random_string (length=14)
    
    return render(request, 'index.html')

def reset(request):
    request.session.flush()
    return redirect('/')


# Create your views here.
