from django.shortcuts import render
import csv
from .models import kinder

# Create your views here.

def index(request):
	return render(request, 'myapp/index.html')




#csv파일 불러오는 함수
def input(request):
	line = []
 
	f = open('kinder.csv', 'r')
	rdr = csv.reader(f)

	for row in rdr:
		line.apprnf(row)
		
		kinders = kinder(
			name = line[0]
			)
		kinders.save()

	f.close()  



