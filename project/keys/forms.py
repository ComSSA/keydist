# coding=utf-8
from __future__ import absolute_import, unicode_literals
from django import forms
from django.contrib.auth import get_user_model
from .models import SKU, Product


class KeyImportForm(forms.Form):

    keyfile = forms.FileField(
        required=True, label="Key file",
        help_text="A valid CSV from DreamSpark.")


class AllocateForm(forms.Form):

    user = forms.ModelChoiceField(queryset=get_user_model().objects.all())

    SKU = forms.ModelChoiceField(queryset=SKU.objects.all())
