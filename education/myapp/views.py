from django.shortcuts import render
import csv
from .models import kinder

# Create your views here.

def index(request):
	return render(request, 'myapp/index.html')




#csv파일 불러오는 함수
def input(request):

	line = []
 
	f = open('recycle.csv', 'r')
	rdr = csv.reader(f)

	for row in rdr:
		line.append(row)
		print(line[0])
		kinders = kinder(
			name = line[0]
			)
		kinders.save()

	f.close()
	return render(request, 'myapp/input.html')


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


