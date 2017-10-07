# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib import messages

# Create your views here.
def index(request):

	return render(request, "calculator_app/index.html")


def process(request):

	if request.POST["num1"].isalpha() and request.POST["num2"].isalpha():

		messages.error(request, "Both inputs must be numbers!")

		return redirect('/')

	elif request.POST["num1"].isalpha():

		messages.error(request, "First input must be a number!")

		return redirect('/')

	elif request.POST["num2"].isalpha():

		messages.error(request, "Second input must be a number!")

		return redirect('/')

	else:

		request.session["num1"] = request.POST["num1"]
		request.session["num2"] = request.POST["num2"]

		return redirect('/results')



def results(request):

	if "num1" not in request.session:
		request.session["num1"] = 0

	if "num2" not in request.session:
		request.session["num2"] = 0

	sum = int(request.session["num1"]) + int(request.session["num2"])

	context = {
	"sum": sum,
	}

	return render(request, "calculator_app/results.html", context)