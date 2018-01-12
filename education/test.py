import csv

line = []
 
f = open('recycle.csv', 'r')
rdr = csv.reader(f)

for row in rdr:
	line.append(row)
	for lines in line:
		print(lines[6])

f.close()