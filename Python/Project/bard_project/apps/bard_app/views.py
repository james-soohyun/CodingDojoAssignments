# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from models import User

from django.contrib import messages

# Create your views here.

def home(request):

	return render(request, 'bard_app/home.html')


def register(request):

	return render(request, 'bard_app/register.html')


def create(request):

	results = User.objects.validate(request.POST)

	if results['status'] == True:

		user = User.objects.creator(request.POST)
		messages.success(request, 'New user has been created')

	else:

		for error in results['errors']:

			messages.error(request, error)

	return redirect('/register')

def loginPage(request):
	return render(request, 'bard_app/login.html')

def login(request):
	results = User.objects.loginVal(request.POST)
	if results['status'] == False:
		messages.error(request, 'You done goofed, check your password or email and try again!!!!')
		return redirect('/')
	request.session['email'] = results['user'].email
	request.session['first_name'] = results['user'].first_name
	return redirect('/dashboard')

def dashboard(request):
	if 'email' not in request.session:
		return redirect('/')
	return render(request, 'bard_app/dashboard.html')

def logout(request):
	request.session.flush()
	return redirect('/')