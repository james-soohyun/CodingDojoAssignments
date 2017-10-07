# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import User

# Create your views here.
def index(request):
	context = {
	"users": User.objects.all()
	}
	return render(request, "semi_app/index.html", context)

def add(request):
	return render(request, "semi_app/add.html")

def create(request):
	User.objects.create(full_name = request.POST['first_name'] + request.POST['last_name'], email = request.POST['email'])
	return redirect('/users')

def delete(request):
	# tempUser = User.objects.get(request.POST[])
	return "hello"