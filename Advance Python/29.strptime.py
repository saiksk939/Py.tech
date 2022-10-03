from datetime import datetime

datestring='28 January 2022'
date_obj=datetime.strptime(datestring, '%d %B %Y')
print(date_obj)