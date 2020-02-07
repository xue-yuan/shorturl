from django.db import models

# Create your models here.
class ShortUrlModel(models.Model):
	# URL
	url = models.CharField(max_length=200, blank=False)
	# Hash Value
	hash_value = models.CharField(max_length=100, blank=True)
	# Create Time
	create_time = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
	# Whether is private
	private = models.BooleanField(default=False)
	# Need password if private is enabled
	password = models.CharField(max_length=50)
	# Whether is permanent
	permanent = models.BooleanField(default=False)
	# Need Expire if permanent is disabled

	# TODO:
	# expire_time

	expire_time = models.DateTimeField(null=True)
	# More Option
	custom = models.BooleanField(default=False)

    ### custom fields
	# og:title
	title = models.CharField(max_length=200, blank=True)
	# og:description
	description = models.CharField(max_length=200, blank=True)
	# og:image
	thumbnail = models.ImageField(upload_to="thumbnails", blank=True)