# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib import messages

from ..loginReg_app.models import *

from django.contrib import messages

# Create your views here.

def dashboard(request):
	if 'email' not in request.session:
		return redirect('/main')
	for friends in Friendship.objects.exclude(from_person = request.session['id']):
		print friends

	print Friendship.objects.exclude(from_person = request.session['id'])

	context = {
		'users': User.objects.exclude(id = request.session['id']),
		'friends': Friendship.objects.filter(from_person = request.session['id']),
		'notFriends': Friendship.objects.exclude(from_person = request.session['id']),
	}

	return render(request, 'users_app/dashboard.html', context)

def logout(request):
	request.session.flush()
	return redirect('/main')

def display(request, user_id):
	context = {
		'user': User.objects.get(id = user_id),
	}
	return render(request, 'users_app/profile.html', context)

def addFriend(request, user_id):
	user = User.objects.get(id = request.session['id'])
	friend = User.objects.get(id = user_id)
	if len(Friendship.objects.filter(to_person = friend)) < 1:
		tempFriendship = Friendship.objects.create(from_person = user, to_person = friend)
		messages.success(request, 'You are now friends with {}'.format(friend.alias))
	else:
		messages.error(request, 'You are already friends')

	return redirect('/friends')

# def addFriend(request, user_id):
# 	user = User.objects.get(id = user_id)
# 	rel = user.friendships.filter(to_people__from_person = user)
# 	request.session['args'] = {'friends': rel}
# 	return redirect('/friends')

def removeFriend(request, user_id):
	user = User.objects.get(id = request.session['id'])
	friend = User.objects.get(id = user_id)
	Friendship.objects.get(from_person = user, to_person = friend).delete()
	return redirect('/friends')









