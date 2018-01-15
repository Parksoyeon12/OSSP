from django.shortcuts import render
import csv
from .models import kinder, free, recycle
import urllib.request
import json

# Create your views here.

def index(request):

		if request.method == 'GET':

		    client_id = "DshukL7WQcANLYUiQTsY"
		    client_secret = "p5RxLlzjyJ"

		    q = request.GET.get('q')
		 
		    encText = urllib.parse.quote("{}".format(q))
		    url = "https://openapi.naver.com/v1/search/news?query=" + encText #json 결과
		    movie_api_request = urllib.request.Request(url)
		    movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
		    movie_api_request.add_header("X-Naver-Client-Id", client_id)
		   	

		    response = urllib.request.urlopen(movie_api_request)
		    rescode = response.getcode()

		    if (rescode == 200):
		        response_body = response.read()
		        result = json.loads(response_body.decode('utf-8'))
		        items = result.get('items')

		       #	frees = free.objects.all()

		        context = {
		            'items':items,
		            #'frees':frees
		        }

		        return render(request, 'myapp/index.html', context=context)


def input1(request):

	q = request.GET.get('q')

	kinders = kinder.objects.filter(name__contains = q)
	context = {
		'kinders' : kinders
	}

	return render(request, 'myapp/index.html', context)



def input2(request):

  	q = request.GET.get('q')
  	frees = free.objects.filter(facility__contains = q)

  	context = {
  		'frees' : frees
  	}
  	return render(request, 'myapp/index.html', context)




def input3(request):

  	q = request.GET.get('q')
  	recycles = recycle.objects.filter(center__contains = q)

  	context = {
  		'recycles' : recycles
  	}
  	return render(request, 'myapp/index.html', context)


