j=open("D:/Python Advance/text5.txt",'x')
j.write('this is a new line 1')
j.write('this is a new line 2')


j=open("D:/Python Advance/text5.txt",'r')
print(j.read())
j.close()