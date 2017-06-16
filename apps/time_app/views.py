# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
	today = datetime.datetime.now().date()
	now = datetime.datetime.now().time()

	context = {
		'date': today,
		'time': now
	}
	return render(request, 'time_app/index.html', context)
