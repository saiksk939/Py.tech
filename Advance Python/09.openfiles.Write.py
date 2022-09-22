j=open("D:/Python Advance/text3.txt",'w')
j.write('this is a new line 4 ')
j.write('this is a new line 3')


j=open("D:/Python Advance/text3.txt",'r')
print(j.read())
j.close()