# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import Teacher

# Create your views here.
def index(request):
	return render(request, "countTeacher_app/index.html")

def process(request):
	Teacher.objects.create(name = request.POST["name"])
	return redirect('/display')

def display(request):
	context = {
	"count": len(Teacher.objects.filter(name="Ray")),
	"teachers": Teacher.objects.exclude(name = "Ray")
	}
	return render(request, "countTeacher_app/display.html", context)