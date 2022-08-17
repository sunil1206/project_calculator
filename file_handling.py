# file =open("demo.txt",'w')

# file=open("demo.txt",'r')
#
# content=file.read(10)
# print(content)
# file.close()

# file=open("demo.txt",'w')
# content=file.write('am super')
# print(content)
# file.close()

file=open("demo.txt",'a')
content=file.write(' am append')
print(content)
file.close()