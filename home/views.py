from django.shortcuts import render
from keys.models import *

def index(request):
	return render(request, 'home/index.html', {
		'skus': SKU.objects.all(),
        'users': get_user_model().objects.all()
    })