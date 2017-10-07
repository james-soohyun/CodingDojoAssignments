# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib import messages

from ..login_app.models import *

from django.contrib import messages

# Create your views here.

def dashboard(request):
	if 'email' not in request.session:
		return redirect('/main')
	users = User.objects.exclude(id = request.session['id'])
	curUser = User.objects.get(id = request.session['id'])
	context = {
		'users': User.objects.exclude(id = request.session['id']),
		'friends': [],
		'notFriends': []
	}
	for user in users:
		if user in curUser.friends.all():
			context['friends'].append(user)
		else:
			context['notFriends'].append(user)
	return render(request, 'users_app/users.html', context)

def logout(request):
	request.session.flush()
	return redirect('/main')

def display(request, user_id):
	if 'email' not in request.session:
		return redirect('/main')
	context = {
		'user': User.objects.get(id = user_id),
	}
	return render(request, 'users_app/profile.html', context)

def addFriend(request, user_id):
	if 'email' not in request.session:
		return redirect('/main')
	curUser = User.objects.get(id = request.session['id'])
	friendUser = User.objects.get(id = user_id)
	curUser.friends.add(friendUser)
	messages.success(request, 'You are now friends with {}'.format(friendUser.alias))
	return redirect('/friends')

def removeFriend(request, user_id):
	if 'email' not in request.session:
		return redirect('/main')
	curUser = User.objects.get(id = request.session['id'])
	friendUser = User.objects.get(id = user_id)
	curUser.friends.remove(friendUser)
	messages.success(request, 'You are no longer friends with {}'.format(friendUser.alias))
	return redirect('/friends')







