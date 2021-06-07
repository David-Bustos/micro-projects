from django.shortcuts import HttpResponse, render, redirect
import random
import datetime

# vincular a templates
def menu(request): 
    if 'gold' not in request.session:
        request.session['gold']= 0

    if 'activities' not in request.session:
        request.session['activities'] = [5,6,85]

    return render (request, "ninja_gold.html")

def money(request):

    place = request.POST['place']

    # print('### Datos del POST: ' + place)
    
    if place == 'farm':
        amount = random.randint(10, 20)
        time = str(datetime.datetime.now().strftime("%d/%m/%y - %I:%M:%S %p"))
        request.session["gold"] += amount
        request.session['activity'] = f"Earned {amount} golds from the farm! ({time})"
        request.session['activities'].insert(0,request.session["activity"])
    
    elif place == 'cave':
        amount = random.randint(5, 10)
        time = str(datetime.datetime.now().strftime("%d/%m/%y - %I:%M:%S %p"))
        request.session["gold"] += amount
        request.session['activity'] = f"Earned {amount} golds from the cave! ({time})"
        request.session['activities'].insert(0,request.session["activity"])

    elif place == 'house':
        amount = random.randint(2,5)
        time = str(datetime.datetime.now().strftime("%d/%m/%y - %I:%M:%S %p"))
        request.session["gold"] += amount
        request.session['activity'] = f"Earned {amount} golds from the house! ({time})"
        request.session['activities'].insert(0,request.session["activity"])

    elif place == 'casino':
        amount = random.randint(-50, 50)
        time = str(datetime.datetime.now().strftime("%d/%m/%y - %I:%M:%S %p"))
        request.session["gold"] += amount
        if amount > 0:
            request.session['activity'] = f"Entered a casino and win {amount} golds...Nice! ({time})"
        else:
            request.session['activity'] = f"Entered a casino and lost {amount} golds...Ouch! ({time})"
        request.session['activities'].insert(0,request.session["activity"])

    return redirect("/ninja_gold")

def restart(request):
    request.session["gold"]=0
    request.session['activities'] = []
    return redirect("/ninja_gold")