from copy import deepcopy


def solution(food_times, k):
    tmp = deepcopy(food_times)
    while k>=len(tmp)*min(tmp):
        m = min(tmp)
        k-=len(tmp)*m
        food_times = [_-m if _!=0 else _ for _ in food_times]
        tmp = [_-m for _ in tmp]
        while 0 in tmp:
            tmp.remove(0)
    return find(food_times, k)

def find(arr,k):
    i=0
    for _ in range(len(arr)):
        i+= 1 if arr[_]!=0 else 0
        if i==(k+1):
            return _+1
    return -1
print(solution([5,3,4,7],14))
# 4

print(solution(	[3, 1, 2], 5))
#1