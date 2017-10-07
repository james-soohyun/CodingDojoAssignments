# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	if "name" not in request.session:
		request.session["name"] = ""
	context = {
		"name": request.session["name"]
	}
	return render(request, "dayAssign_app/index.html", context)

def display(request):
	request.session["name"] = request.POST["firstName"]
	return redirect("/")

def reset(request):
	request.session.flush()
	return render(request, "dayAssign_app/index.html")