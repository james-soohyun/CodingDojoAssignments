# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

import random, datetime

# Create your views here.
def index(request):
	# request.session.flush()
	if "gold" not in request.session:
		request.session["gold"] = 0

	if "log" not in request.session:
		request.session["log"] = []

	context = {
	"gold": request.session["gold"],
	"log": request.session["log"]
	}
s
	return render(request, "ninjaGold_app/index.html", context)

def process(request):
	if request.POST["place"] == "farm":
		ranNum = random.randint(10,20)
		request.session["gold"]+= ranNum
		request.session["log"].append("Earned {} golds from the farm! ({})".format(ranNum, datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")))

	elif request.POST["place"] == "cave":
		ranNum = random.randint(5,10)
		request.session["gold"]+= ranNum
		request.session["log"].append("Earned {} golds from the cave! ({})".format(ranNum, datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")))

	elif request.POST["place"] == "house":
		ranNum = random.randint(2,5)
		request.session["gold"]+= ranNum
		request.session["log"].append("Earned {} golds from the house! ({})".format(ranNum, datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")))

	elif request.POST["place"] == "casino":
		ranNum = random.randint(-50,50)
		request.session["gold"]+= ranNum
		if ranNum > 0:
			request.session["log"].append("Entered a casino and earned {} golds. Yay! Will your luck continue? ({})".format(ranNum, datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")))
		elif ranNum < 0:
			request.session["log"].append("Entered a casino and lost {} golds... Ouch... ({})".format(ranNum, datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")))
		else:
			request.session["log"].append("Entered a casino and broke even at {} golds. Is this a sign to continue or quit? ({})".format(ranNum, datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")))
	return redirect("/")
