import csv
from .models import recycle 
from .models import free
line = []
 
f = open('recycle.csv', 'r')
rdr = csv.reader(f)

for row in rdr:
	line.append(row)
	
for lines in line:
	recycles = recycle(
		center = lines[0],
		road = lines[2],
		address = lines[3], 
		area= lines[6],
		vehicle = lines[8],
		item = lines[9],
		operating = lines[10],
		telephone = lines[11]
		) 

f.close()

f = open('free.csv', 'r')
rdr = csv.reader(f)

for row in rdr:
	line.append(row)
	for lines in line:
		for i in range(22):
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
f.close()

f = open('kinder.csv', 'r')
rdr = csv.reader(f)

for row in rdr:
	line.append(row)
	for lines in line:
		for i in range(22):
			kinders = kinder(
				divide = lines[1],
				types = lines[2],
				name = lines[3], 
				snumber= lines[4],
				address = lines[5],
				) 
	


f.close()