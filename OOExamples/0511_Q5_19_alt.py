s_list = ['abc','bcd','abc','abba','cddc','opq','opq']
print("s_list =",s_list)
new_s_list = []
for _ in s_list:
    if _ not in new_s_list :
        new_s_list.append(_)
print("new_s_list =",new_s_list)