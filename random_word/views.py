from django.shortcuts import HttpResponse, render, redirect

from django.utils.crypto import get_random_string

# vincular a templates
def generator(request): 

    if 'count' not in request.session:
            request.session['count']= 0

    request.session['count'] += 1

    rs = get_random_string(length=14)

    context ={ 
        "random_string": rs, 
    }		 
    return render (request, "random_word.html", context)

def reset(request):
    request.session.flush()
    return redirect('/random_word')