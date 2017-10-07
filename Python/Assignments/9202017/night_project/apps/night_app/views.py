# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import User

# Create your views here.
def index(request):
	return render(request, "night_app/index.html")

def process(request):
	User.objects.create(first = request.POST['first'], last = request.POST['last'])
	return redirect("/display")

def display(request):
	context = {
	"users": User.objects.all()
	}
	return render(request, "night_app/display.html", context)