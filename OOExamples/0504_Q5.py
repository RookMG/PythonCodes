from random import randint as r
a = r(1,100)
b = r(1,100)
print(str(a)+" - "+str(b)+" = ", end='')
ans = input()
if ans == str(a-b) :
    print("맞았습니다.")
else :
    print("틀렸습니다.")