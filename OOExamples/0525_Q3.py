with open('input.txt','r') as f:
    lines = f.readlines()
    print("단어 입력: ",end = '')
    s = input()
    print(s+"빈도: "+str(len(lines[0].upper().split(s.upper()))-1))

# C:\Users\tngks\프로그래밍\python\input.txt