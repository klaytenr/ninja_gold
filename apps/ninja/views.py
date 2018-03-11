from django.shortcuts import render, redirect
import random

# Create your views here.

def index(request):
    if "gold_count" not in request.session:
        request.session["gold_count"] = 0
    if "logs" not in request.session:
        request.session["logs"] = []
    return render(request, "ninja/index.html")

def process(request):
    if request.POST["action"] == "farm":
        randoms = random.randrange(10, 21)
        request.session["gold_count"] += randoms
        request.session["logs"].append("Earned " + str(randoms) + " golds from the farm!")
    elif request.POST["action"] == "cave":
        randoms = random.randrange(5, 11)
        request.session["gold_count"] += randoms
        request.session["logs"].append("Earned " + str(randoms) + " golds from the cave!")
    elif request.POST["action"] == "house":
        randoms = random.randrange(2, 6)
        request.session["gold_count"] += randoms
        request.session["logs"].append("Earned " + str(randoms) + " golds from the house!")
    elif request.POST["action"] == "casino":
        randoms = random.randrange(-50, 51)
        request.session["gold_count"] += randoms
        if randoms < 0:
            request.session["logs"].append("You lost " + str(randoms*-1) + " golds at the casino!")
        else:
            request.session["logs"].append("Earned " + str(randoms) + " golds from the casino!")
    print request.session["gold_count"]
    return redirect("/")