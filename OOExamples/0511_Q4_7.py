def mean3(l):
    return (l[0]+l[1]+l[2])/3

def max3(l):
    ans = l[0] if l[0]>l[1] else l[1]
    ans = ans if ans>l[2] else l[2]
    return ans

def min3(l):
    ans = l[0] if l[0]<l[1] else l[1]
    ans = ans if ans<l[2] else l[2]
    return ans

print("세 수를 입력하시오 : ",end='')
n = list(map(int,input().split()))
nstr = str(n[0])+", "+str(n[1])+", "+str(n[2])
print(nstr+"의 평균값은",mean3(n))
print(nstr+"의 최댓값은",max3(n))
print(nstr+"의 최솟값은",min3(n))