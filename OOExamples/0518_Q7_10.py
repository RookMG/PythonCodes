from random import randrange
ans = randrange(20)+1
print("debugging : ans =",ans)
count = 0
call = 0
while call != ans :
    print("1~20까지의 숫자를 입력하세요:",end = ' ')
    call = int(input())
    count += 1
    if call != ans:
        print(call,"보다 "+("큽니다!" if call<ans else "작습니다!"))
    else :
        print("정답입니다!")
if count <3 :
    print(count,"번 만에 맞춘 당신은 천재!")
elif count <7 :
    print(count,"번 만에 맞추셨네요. 잘 했어요^^")
else :
    print(count,"번 만에 맞추다니 쩝쩝...")