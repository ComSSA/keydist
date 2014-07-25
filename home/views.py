from django.shortcuts import render
from keys.models import *

def index(request):
	return render(request, 'home/index.html', {
		'skus': SKU.objects.all()
		})