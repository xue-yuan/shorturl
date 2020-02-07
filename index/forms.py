from django import forms
from .utils import url_is_not_valid, url_process
from .models import ShortUrlModel

class CreateShortenForm(forms.ModelForm):
	class Meta:
		model = ShortUrlModel
		fields = ['url']

	def clean_url(self):
		url = self.cleaned_data['url']
		if url_is_not_valid(url):
			raise forms.ValidationError("Please remove the whitespace character")

		url = url_process(url)
		return url
