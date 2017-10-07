# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):

	request = {
	'POST': {},
	'GET': {},
	'session': {}
	}
	print request[]

	return render(request, "survey_app/index.html")