j=open("D:/Python Advance/text3.txt",'a')
j.write('this is a new file text3')

j=open("D:/Python Advance/text3.txt",'r')
print(j.read())
j.close()