from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here. #These are mapped to urls.py 
# Views must return http response or exception


def home(request):
	context = {
		'posts': Post.objects.all()  #posts is the list of post dictionary
	}

	return render(request, 'alertsteps/home.html', context) # context var is db data

def about(request):
	return render(request, 'alertsteps/about.html', {'title': 'About'}) 

