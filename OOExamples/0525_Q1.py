print("파일 이름을 입력하시오 : ", end = '')
text_file_path = input()
new_text_content = ''
print("삭제할 문자열을 입력하시오 : ", end = '')
target_word = input()
with open(text_file_path,'r') as f:
    lines = f.readlines()
    for i, l in enumerate(lines):
        new_string = l.strip().replace(target_word,'')
        if new_string:
            new_text_content += new_string + '\n'
        else:
            new_text_content += '\n'
                
with open(text_file_path,'w') as f:
    f.write(new_text_content)

# C:\Users\tngks\프로그래밍\python\words.txt
# Twinkle, twinkle, little star How I wonder what you are