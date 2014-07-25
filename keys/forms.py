from django import forms
from django.contrib.auth import get_user_model
from keys.models import SKU, Product


class KeyImportForm(forms.Form):
	keyfile = forms.FileField(required = True, label = "Key file", help_text = "A valid CSV file from the CoderDojo @ Curtin mentor signup sheet.")

class AllocateForm(forms.Form):
	user = forms.ModelChoiceField(
		queryset = get_user_model().objects.all(),
	)

	SKU = forms.ModelChoiceField(
		queryset = SKU.objects.all(),
	)