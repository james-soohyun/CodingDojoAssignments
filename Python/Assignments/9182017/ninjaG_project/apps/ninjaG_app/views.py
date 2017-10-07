# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	# request.session.flush()
	if "gold" not in request.session:
		request.session["gold"] = 0

	if 'msg' not in request.session:
		request.session['msg'] = []

	context = {
	"gold": request.session["gold"],
	"msg": request.session["msg"]
	}

	return render(request, "ninjaG_app/index.html", context)

def process(request):
	if request.POST["place"] == 'tavern':
		request.session['gold']-=20
		request.session['msg'].append("You went to the Tavern and lost some money")
	if request.POST["place"] == 'cave':
		request.session['gold']-=10
		request.session['msg'].append("You went to the Cave and lost some money")

	return redirect('/')

def reset(request):
	request.session['gold'] = 0
	request.session['msg'] = []
	return redirect('/')