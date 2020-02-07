from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from . import models
from . import forms
from .utils import code_generater

BASE_URL = settings.SITE_URL

# Create your views here.
def index(request):
	# if request.method == 'POST':
	# 	submitted_form = forms.CreateShortenForm(request.POST)
	# 	if submitted_form.is_valid():
	# 		url = submitted_form.cleaned_data['url']
	# 		url_object, is_not_created = models.ShortUrlModel.objects.get_or_create(url=url, custom=False)
	# 		if is_not_created:
	# 			hash_value = code_generater(url, 5)
	# 			url_object.hash_value = hash_value
	# 			url_object.save()

	# 		short_url = BASE_URL + url_object.hash_value

	# 		# TODO:
	# 		# use Ajax instead of render 

	# 		return render(request, 'index.html', context=locals())

	create_form = forms.CreateShortenForm()
	return render(request, 'index.html', context=locals())

def ajax(request):
	if request.method == 'POST':
		submitted_form = forms.CreateShortenForm(request.POST)
		if submitted_form.is_valid():
			url = submitted_form.cleaned_data['url']
			url_object, is_not_created = models.ShortUrlModel.objects.get_or_create(url=url, custom=False)
			if is_not_created:
				hash_value = code_generater(url, 5)
				url_object.hash_value = hash_value
				url_object.save()

			short_url = BASE_URL + url_object.hash_value

	data = {}
	data['status'] = 'SUCCESS'
	data['short_url'] = short_url
	# data['log_info'] = request.POST['username']
	return JsonResponse(data)

def redirect_url(request, hash_value):
	try:
		url_object = models.ShortUrlModel.objects.get(hash_value=hash_value)
	except:
		return render(request, 'redirect_404.html', locals())

	if url_object.custom:
		return render(request, 'redirect.html', locals())
	else:
		return redirect(url_object.url)

