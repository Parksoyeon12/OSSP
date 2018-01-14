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




#csv파일 불러오는 함수
def input(request):

	line = []
	f = open('free.csv', 'r')
	rdr = csv.reader(f)

	for row in rdr:
		line.insert(0, row)
		for lines in line:
			frees = free(
				facility = lines[0],
				address = lines[1],
				support = lines[2], 
				telephone= lines[3],
				location = lines[4],
				opponent = lines[5],
				time = lines[6],
				day = lines[7]

				) 
			frees.save()

	return render(request, 'myapp/index.html')



def input1(request):

	q = request.GET.get('q')

	kinders = kinder.objects.filter(name = q)
	context = {
		'kinders' : kinders
	}

	return render(request, 'myapp/index.html', context)



def input2(request):

  	q = request.GET.get('q')
  	frees = free.objects.filter(facility = q)

  	context = {
  		'frees' : frees
  	}
  	return render(request, 'myapp/index.html', context)


