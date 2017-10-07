# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from models import Cat, Dog

# Create your views here.
def index(request):

	return render(request, "catDog_app/index.html")

def process(request):
	if request.POST["animal"] == "cat":
		Cat.objects.create(name = request.POST["first_name"])
	else:
		Dog.objects.create(name = request.POST["first_name"])

	return redirect("/display")

def display(request):

	context = {
	"cats": Cat.objects.all(),
	"dogs": Dog.objects.all()
	}

	return render(request, "catDog_app/display.html", context)