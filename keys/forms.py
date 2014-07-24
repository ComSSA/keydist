from django import forms

class KeyImportForm(forms.Form):
	keyfile = forms.FileField(required = True, label = "Key file", help_text = "A valid CSV file from the CoderDojo @ Curtin mentor signup sheet.")