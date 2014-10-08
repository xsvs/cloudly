# -*- coding: utf-8 -*-

import os
import time
import pickle
import logging
import datetime

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from django.http import HttpResponseForbidden
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from userprofile.models import Profile
from userprofile.views import _log_user_activity

logger = logging.getLogger(__name__)

import pymongo
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
client = MongoClient('localhost', 27017)

mongo = client.cloudly

def private_storage(request):

	if not request.user.is_authenticated():
		return HttpResponseRedirect("/")

	user = request.user
	user.last_login = datetime.datetime.now()
	user.save()

	print '-- private storage:'
	print request.user

	ip = request.META['REMOTE_ADDR']
	profile = Profile.objects.get(user=request.user)
	_log_user_activity(profile,"click","/private/storage/","private_storage",ip=ip)

	return render_to_response('private_storage.html', locals(), context_instance=RequestContext(request))
