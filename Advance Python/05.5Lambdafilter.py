# list used because after filter evenlist data is not list 
MYlist=[1,2,3,4,5,6,7,8,9,10]
evenlist=list(filter(lambda i:i%2==0, MYlist)) 
print('The list of even number is ',evenlist)