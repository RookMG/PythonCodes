from time import time
start = time()
n = int(input("n값을 입력하세요: "))
count = 1
for _ in range(2,n+1):
    if n%_ == 0 :
        count += 1
out = "소수입니다." if count==2 else "소수가 아닙니다."
out+="\ntime :"+str(time()-start)
print(out)