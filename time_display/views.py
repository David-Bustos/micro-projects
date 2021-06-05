from django.shortcuts import render

# Create your views here.
from time import gmtime, strftime, localtime
    
def current_td(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", localtime())
    }
    return render(request,'data_time.html', context)