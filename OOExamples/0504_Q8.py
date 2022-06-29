from random import randint as r
a = r(2,9)
b = r(2,9)
while True :
    print(str(a)+" x "+str(b)+" = ",end='')
    ans = input()
    if ans == str(a*b) :
        break
print("맞았습니다.")