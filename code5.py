file=open('demo.txt','w')
# file.read()
# print(file)
file.close()

file=open('demo.txt','w')
file.write("Hai welcome to Linus World.")
file.close()

file=open('demo.txt','a')
file.write(' Fun start here!!!')
print(file)
file.close()



