from random import randint as r
c = [0,0,0,0,0,0]
for _ in range(1000):
    c[r(0,5)] += 1
for i in range(6):
    print("주사위가 "+str(i+1)+"인 경우는",c[i])