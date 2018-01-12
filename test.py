import csv

line = []
 
f = open('kinder.csv', 'r')
rdr = csv.reader(f)
for row in rdr:
    line.append(row)
    
print(line[0])
f.close()  s