from random import randrange as dice
rom = dice(6) + 1
jul = dice(6) + 1
print("로미오의 주사위 숫자는",rom,"입니다.")
print("줄리엣의 주사위 숫자는",jul,"입니다.")
if rom == jul :
    out = "비겼습니다."
else :
    out = "로미오가 " if rom>jul else "줄리엣이 "
    out += "이겼습니다."
print(out)