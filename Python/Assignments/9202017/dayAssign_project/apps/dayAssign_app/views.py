# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import User

# Create your views here.
def index(request):
	return render(request, "dayAssign_app/index.html")

def process(request):
	User.objects.create(name = request.POST['name'])
	return redirect('/display')

def display(request):
	context = {
		"users": User.objects.all()
	}
	return render(request, "dayAssign_app/names.html", context)