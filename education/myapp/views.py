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
	f = open('kinder.csv', 'r')
	rdr = csv.reader(f)

	for row in rdr:
		line.insert(0, row)
		for lines in line:
			kinders = kinder(
				divide = lines[1],
				types = lines[2],
				name = lines[3], 
				snumber= lines[4],
				address = lines[5],
				) 
			kinders.save()

	return render(request, 'myapp/index.html')






def input1(request):
	line = []
	f = open('free.csv','r')
	rdr = csv.reader(f)

	for row in rdr:
		line.append(row)

		frees = free(
			name = line[0]
			)
	frees.save()

	f.close()



def input2(request):
  	line = []
  	f = open('recycle.csv','r')	
  	rdr = csv.reader(f)

  	for row in rdr:
  		line.append(row)

  		recycles = recycle(
  			name = line[0]
  			)
  		recycles.save()

  		f.close()


