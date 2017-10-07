# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'blogs_app/index.html')

def new(request):
	return render(request, 'blogs_app/newBlog.html')

def create(request):
	return render(request, 'blogs_app/index.html')

def show(request):
	return render(request, 'blogs_app/15.html')

def edit(request):
	return render(request, 'blogs_app/edit15.html')

def delete(request):
	return render(request, 'blogs_app/index.html')