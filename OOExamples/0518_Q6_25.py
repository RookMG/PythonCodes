print("사전 프로그램 시작... 종료는 q를 입력")
line = ''
dict = {}
while line != 'q':
    print("$",end=' ')
    line = input()
    pivot = line.find(':')
    if line == 'q':
        print("사전 프로그램을 종료합니다.")
    elif line[0] == '<' :
        dict[line[2:pivot]]=line[pivot+1:]
    elif line[0] == '>' :
        if line[2:] in dict :
            print(dict[line[2:]])
        else :
            print(line[2:]+"가 사전에 없습니다.")
    else :
        print("입력오류가 발생했습니다.")


'''
< boy:소년
< girl:소녀
< man:남자, 사람
> boy
man
> man
q
'''