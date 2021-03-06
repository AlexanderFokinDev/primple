# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from .forms import MyRegistrationForm
from django.template.context_processors import csrf 
from knowledge_base.models import KnowledgeBase

# Create your views here.
def index(request):

	if request.user.is_authenticated():
		return render(request,
					 "knowledge_base/kblist.html", 
					 {'knowledge_base': KnowledgeBase.objects.all()})
	else:
		return render(request, "auth/need_authenticate.html")

# index page
def home(request):

	if request.user.is_authenticated():
		return HttpResponseRedirect('/user_desktop/')
	else:
		return render(request, "index.html")

#--------------------------------------------------------------------
# knowledge_base views

def knowledge_base_entry(request, knowledge_base_id=1):

	if request.user.is_authenticated():
		return render(request,
					 "knowledge_base/kbentry.html", 
					 {'knowledge_base_entry': KnowledgeBase.objects.get(id=knowledge_base_id)})
	else:
		return render(request, "auth/need_authenticate.html")

def knowledge_base_new(request, knowledge_base_id=1):

	if request.user.is_authenticated():
		return render(request, "knowledge_base/kb_new_entry.html")
	else:
		return render(request, "auth/need_authenticate.html")

#--------------------------------------------------------------------


#--------------------------------------------------------------------
# Authenticate views

def login(request):
	return render(request, "auth/login.html")

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		#return HttpResponseRedirect('/accounts/loggedin/')
		return HttpResponseRedirect('/user_desktop/')
	else:
		return HttpResponseRedirect('/accounts/invalid/')

def loggedin(request):
	return render(request, "auth/loggedin.html", {'full_name': request.user.first_name})

def invalid_login(request):
	return render(request, "auth/invalid_login.html")

def logout(request):
	first_name = request.user.first_name
	auth.logout(request)
	return render(request, "auth/logout.html", {'full_name': first_name})

def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success/')
		else:
			args = {}
			args.update(csrf(request))
			args['form'] = MyRegistrationForm(request.POST)
	else:
		args = {}
		args.update(csrf(request))
		args['form'] = MyRegistrationForm()

	return render(request, "auth/register.html", args)

def register_success(request):
	return render(request, "auth/register_success.html")

#--------------------------------------------------------------------

#--------------------------------------------------------------------
# Main user desktop

def user_desktop(request):
	if request.user.is_authenticated():
		first_name = request.user.first_name
		return render(request, "user_desktop.html", {'full_name': first_name})
	else:
		return render(request, "auth/need_authenticate.html")

#--------------------------------------------------------------------