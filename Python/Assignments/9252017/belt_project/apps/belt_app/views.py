# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from models import User, Author, Book

from django.contrib import messages

# Create your views here.

def index(request):

	return render(request, 'belt_app/index.html')


def register(request):

	results = User.objects.validate(request.POST)

	if results['status'] == True:
		user = User.objects.creator(request.POST)
		messages.success(request, 'Registration successful')

	else:
		for error in results['errors']:
			messages.error(request, error)

	return redirect('/')


def login(request):
	results = User.objects.loginVal(request.POST)
	if results['status'] == False:
		messages.error(request, 'Email/password is invalid')
		return redirect('/')
	request.session['email'] = results['user'].email
	request.session['name'] = results['user'].name
	request.session['alias'] = results['user'].alias
	return redirect('/books')

def books(request):
	if 'email' not in request.session:
		return redirect('/')
	return render(request, 'belt_app/books.html')

def logout(request):
	request.session.flush()
	return redirect('/')

def add(request):
	return render(request, 'belt_app/add.html')

def review(request):
	
	return redirect('/books')