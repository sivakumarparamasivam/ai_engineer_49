import re
with open('sample.txt',"r") as file_obj:
    content = file_obj.read()
    content_result = re.split(r'[,. "" ]+', content)
    for word in content_result:
        if word.isdigit():
            print(word)   

x=""
for i in 'a1b2c3':
    x=x+chr(ord(i)+1)
print(x)