import hashlib
import base64
import string
import random
import datetime
from .models import ShortUrlModel

# FIXME:
# Complete Validators

def url_is_not_valid(url):
	if url.isspace():
		return True

	if ' ' in url:
		return True 

	if '.' not in url:
		return True

	return False

def url_process(url):
	if url.endswith('/'):
		url = url[:-1]

	# FIXME:
	# regex to check startwith
	# url = 'http://' + url is not a good method 

	if url.startswith('https://') or url.startswith('http://'):
		pass
	else:
		url = 'http://' + url

	return url

def code_generater(url, n):
    md5 = hashlib.md5()
    md5.update((url).encode('utf-8'))
    hash_value = base64.b64encode(md5.digest()).decode('utf-8').replace('/', '_').replace('+', '-')
    short_hash_value = hash_value[:n]

    if code_is_not_valid(short_hash_value):
        code_generater(short_hash_value, n)

    return short_hash_value

def code_is_not_valid(short_hash_value):
    if ShortUrlModel.objects.filter(hash_value=short_hash_value):
        return True
    return False

# def randomGenerate(n):
#     char_list = string.ascii_letters + string.digits
#     code = ''.join([random.choice(char_list) for _ in range(n)])
#     if ShortUrl.objects.filter(code=code):
#         return randomGenerate(n)
#     return code
