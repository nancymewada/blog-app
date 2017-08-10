# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
class Homepageview(TemplateView):
	def get(request,*args,**kwargs):
		return render(request,'index.html',context=None)

class AboutPageView(TemplateView):
	template_name = 'parkingform.html'