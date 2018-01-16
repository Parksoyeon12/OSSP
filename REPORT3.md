REPORT 3
======
담당교수님 : 최동민 교수님

분반 : 02분반

학과 : 컴퓨터공학과 

학번 : 20154294 

이름 : 박소연

제출일 : 1월 18일


## 1) 데이터 넣기 ##

#### data.go.kr에서 받아온 csv 파일이 제대로 들어갔는지 시험하는 test만들기 ####

##### - 테스트용으로 데이터를 올리기(data migration) #####

- urls

![screen](https://github.com/Parksoyeon12/OSSP/blob/master/1.PNG?raw=true)
- views

![screen](https://github.com/Parksoyeon12/OSSP/blob/master/2.PNG?raw=true)

- data넣기  test
 
_csv를 불러오는 함수_test용_
```
line = [] # csv파일에서 가져온 데이터를 저장할 list생성
f = open(kinder.csv','r') #csv파일을 읽기 전용으로 열기
rdr = csv.reader(f) # csv파일 읽기
for row in rdr; 
	line.append(row) #데이터 list에 저장
```

## 2) 초기 수정 ##

### 1. 초기에 발생한 오류를 모두 수정하기 ###

### 2. 속성 찾아서 모델 작성하기 ###

### 3. 파일 본격적으로 넣기 ###

- admin 설정하기
```
from .modls import kinder
+admin.site.register(kinder)
# 데이터가 잘 들어갔는지 확인하기 위해 데이터 모델을 관리자 사이트에 추가
```

- models 설정하기(속성 찾아서 모델 작성하기)

![screen](https://github.com/Parksoyeon12/OSSP/blob/master/3.PNG?raw=true)

- index 재설정 위치의 변화

![screen](https://github.com/Parksoyeon12/OSSP/blob/master/3.PNG?raw=true)

- 새로운 페이지 만들기 연습

![screen](https://github.com/Parksoyeon12/OSSP/blob/master/5.PNG?raw=true)


- views에서 csv 파일을 본격적으로 넣기

```
def input(request): #데이터 저장하는 함수
	line = []
    
    f= open('kinder.csv','r')
    rdr = csv.reader(f)
    
    for row in rdr;
    	line.append(row)
        kinders = kinder(
        	name = line[0] #데이터베이스 저장
            )
        kinders.save() # 데이터베이스 저장
    f.close() # 파일 닫기
```

## 3) News search 기능 추가

### 1. 속성에 맞춰 data 올리기 ###
### 2. 약간의 모델 수정 ###
### 3. index에 뉴스 api 추가함 ###

- 속성에 맞춰  데이터 올리기

![screen](https://github.com/Parksoyeon12/OSSP/blob/master/6.PNG?raw=true)

- 변경된 데이터 모델 

![screen](https://github.com/Parksoyeon12/OSSP/blob/master/7.PNG?raw=true)

- 뉴스 검색 기능 추가됨

![screen](https://github.com/Parksoyeon12/OSSP/blob/master/8.PNG?raw=true)

- urls 연결

![screen](https://github.com/Parksoyeon12/OSSP/blob/master/9.PNG?raw=true)


- views

``` 
def input(request)
	line = []
    f= open('kinder.csv','r')
    rdr=csv.reader(f)
    
    for row in rdr;
        line.insert(0, row) 
        for lines in line;
        	kinders =kinder{
            	divide = lines[1]; # 속성에 맞게 저장하기
                types =lines[2];
                name =lines[3];
                snumber = lines[4];
                address =lines[5];
                )
             kinders.save()
    return render(request, 'myapp/index.html')
    
    f.close()
    return render(request, 'myapp/input.html')
```   

## 4.유치원 검색창 만들기 ##
### 1. 검색창 만들기 ###

- index 변경

![screen](https://github.com/Parksoyeon12/OSSP/blob/master/10.PNG?raw=true)

- urls 추가

![screen](https://github.com/Parksoyeon12/OSSP/blob/master/11.PNG?raw=true)

- views 수정_화면에 띄우려고!!
```
def input(request):

	line = []
    f = open(kinder.csv,'r')
    rdr =csv.reader(f)
    
    for row in rdr:
    	lline.insert(0,row)
        for lines in line:
        kinders = kinder(
        	divide =lines[1],
            types = lines[2],
            name = lines[3],
            snumber = lines[4],
            address = lines[5],
            )
      kinder.save()
 return render(request,'myapp/index.html') # html 파일을 화면에 띄운다(render가)
```     
       
 ## 5. FREE MEAL 검색창 만들기 ##
 ### 1. 검색창 만들기 ###
- admin 추가
 
![screen](https://github.com/Parksoyeon12/OSSP/blob/master/12.PNG?raw=true)

 - index 수정

![screen](https://github.com/Parksoyeon12/OSSP/blob/master/13.PNG?raw=true)


- views
_오타로 인해 오류가 발생하였는데 수정함_


## 6. recycle 검색 창 만들기 ##
### 1. 검색창 만들기 ###
- index 수정

![screen](https://github.com/Parksoyeon12/OSSP/blob/master/14.PNG?raw=true)

- views 

![screen](https://github.com/Parksoyeon12/OSSP/blob/master/15.PNG?raw=true)



## 7. 최종오류(데이터베이스 수정)
### 1. models의 CHARFIED의 값을 변화시켜봄 ###
### 2. 기존의 함수를 변경시킴 ###
    
- MODELS에서 값을 수정

![screen](https://github.com/Parksoyeon12/OSSP/blob/master/16.PNG?raw=true)

- 기존의 함수를 변경시킴
```
for lines in line:
	recycles = recycle(
    center =lines[0],
    road = lines[2],
    address = lines[3],
    area = lines[6],
    vechivcle = lines[8],
    item = lines[9],
    operatin = lines[10],
    telephone = lines[11],
    )
```
## 8. 가독성을 위해 표를 추가함 ##
### 1. css에서 표를 만드는 법을 찾아서 표를 추가 ###

![screen](https://github.com/Parksoyeon12/OSSP/blob/master/17.PNG?raw=true)
    

