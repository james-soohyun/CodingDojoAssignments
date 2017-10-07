# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from models import Comment

from django.contrib import messages

# Create your views here.

def index(request):

	context = {
		'comments': Comment.objects.order_by('-created_at')
	}

	return render(request, 'comment_app/index.html', context)

def comment(request):

	results = Comment.objects.validator(request.POST)

	if results['status'] == True:
		Comment.objects.creator(request.POST)
		return redirect('/')

	else:
		for error in results['errors']:
			messages.error(request, error)
			return redirect('/')