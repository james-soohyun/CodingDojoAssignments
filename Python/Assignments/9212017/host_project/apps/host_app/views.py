# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Site
from django.contrib import messages

# Create your views here.

def index(request):

	return render(request, "host_app/index.html")


def check(request):

	if Site.objects.filter(site = request.POST["check"]).exists():

		messages.error(request, "Website already exists in database...")

		return redirect('/')

	elif request.POST["check"].startswith("www.") == False:

		messages.error(request, "Webste must start with 'www.'")

		return redirect('/')

	elif request.POST["check"].endswith(".com") == False:

		messages.error(request, "Webste must end with '.com'")

		return redirect('/')

	else:

		messages.success(request, "Website does not exist in database, available to add!")

		return redirect('/')


def process(request):

	# Site.objects.all().delete()

	if Site.objects.filter(site = request.POST["site"]).exists():

		messages.error(request, "Website already exists in database...")

		return redirect('/')

	if request.POST["site"].startswith("www.") and request.POST["site"].endswith(".com"):

		Site.objects.create(site = request.POST["site"])

		return redirect ('/display')

	elif request.POST["site"].startswith("www.") == False:

		messages.error(request, "Webste must start with 'www.'")

		return redirect('/')

	elif request.POST["site"].endswith(".com") == False:

		messages.error(request, "Webste must end with '.com'")

		return redirect('/')


def display(request):

	context = {
	"sites": Site.objects.all(),
	}


	return render(request, "host_app/display.html", context)

