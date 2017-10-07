# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
	if "word" not in request.session:
		request.session["word"] = ""
	if "attempt" not in request.session:
		request.session["attempt"] = 0
	context = {
	"attempt": request.session["attempt"],
	"random_word": request.session["word"]
	}
	return render(request, 'random_word_app/index.html', context)

def generate(request):
	request.session["word"]= get_random_string(length=14)
	request.session["attempt"]+=1
	return redirect('/random_word_app/')

# def index(request):n
# 	attempt=0
# 	attempt+=1
# 	word = {
# 	"attempt": attempt,
# 	"random_word": get_random_string(length=14)
# 	}
# 	return render(request, 'random_word_app/index.html', word)