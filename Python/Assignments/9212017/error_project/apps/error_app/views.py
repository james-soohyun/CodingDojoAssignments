# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Guest
from django.contrib import messages

# Create your views here.
def index(request):

	return render(request, "error_app/index.html")

def process(request):

	if len(request.POST["first_name"]) >=3:
		Guest.objects.create(name = request.POST["first_name"])

		return redirect('/display')
		
	else:
		messages.error(request, ' boooooooo')
		return redirect('/')
		

def display(request):
	context = {
	"guests": Guest.objects.all()
	}
	return render(request, "error_app/display.html",context)