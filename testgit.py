#-*-     coding: cp949 -*-
# 1�� ������ middle.py �ۼ��� ���� ���� ȭ��
# ���Ͽ� �� �ٿ� ���� ���� �ڷ�(token)�� ���� ��
# �ϳ��� token type���� �д� ������ �մϴ�.

myfile = open("middle.inp" ,"r")  # ���� ������ �غ� ��
myline = myfile.readline()          # ��ü ������ �ϳ��� ���ڿ��� ����
a,b,c = myline.split()              # ������ �������� �ɰ�. 3���� ����

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
