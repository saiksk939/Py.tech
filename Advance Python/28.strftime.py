from datetime import datetime

now=datetime.now()

t1=now.strftime('%H:%M:%S')
print('Time :',t1)


t2=now.strftime('%d/%m/%y, %H:%M:%S')
print('Time :',t2)