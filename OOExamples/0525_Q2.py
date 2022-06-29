sum = 0
size = 0
with open('data.txt','r') as f:
    while True:
        line = f.readline()
        if line == '' :
            break
        sum += float(line.strip())
        size += 1
with open('output.txt','w') as f:
    f.write("합계="+str(sum)+'\n'+"평균="+str(sum/size))

# C:\Users\tngks\프로그래밍\python\data.txt