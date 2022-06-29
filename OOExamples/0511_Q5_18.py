s_list = ['abc','bcd','bcdefg','abba','cddc','opq']
short = s_list[0]
for _ in s_list :
    short = _ if len(short)>len(_) else short
print("가장 길이가 짧은 문자열 :",short)