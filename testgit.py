#-*-     coding: cp949 -*-
# 1번 과제물 middle.py 작성을 위한 도움 화일
# 파일에 한 줄에 여러 개의 자료(token)이 있을 때
# 하나씩 token type으로 읽는 연습을 합니다.

myfile = open("middle.inp" ,"r")  # 읽을 파일을 준비 함
myline = myfile.readline()          # 전체 라인을 하나의 문자열로 읽음
a,b,c = myline.split()              # 공백을 기준으로 쪼갬. 3개의 숫자

x = int(a)
y = int(b)
z = int(c)

if x >= y :
    if y >= z : middle = y
    else :
        if x >= z : middle = z
        else : middle = x

else :
    if x >= z : middle = x
    else:
        if y >= z : middle = z
        else : middle = y

myfileout = open("middle.out", "w")
print>> myfileout, middle
myfileout.close()
myfile.close()
