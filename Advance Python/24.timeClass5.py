from datetime import time

x=time(5,30,20)
print('Hour=',x.hour)
print('Minutes=',x.minute)
print('Second=',x.second)

y=time(hour=2, minute=32, second=44)
print('Time y=',y)

z=time(7,30,22,123457)
print('Time z=',z)