def sort3(i,j,k):
    ans = []
    ans.append(i)
    ans.append(j)
    ans.append(k)
    ans.sort()
    return ans
print("세 수를 입력하세요 :")
n1 = int(input())
n2 = int(input())
n3 = int(input())
n = sort3(n1,n2,n3)
print("정렬된 리스트는 다음과 같습니다:",n[0],n[1],n[2])