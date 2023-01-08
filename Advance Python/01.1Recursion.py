#sum of n numbers
# n=4 : 4+3+2+1 = 10
#finding sum of numbers using  iteration

def find_sum(n):  #function definition
    sum=0
    for i in range(1,n+1):   #iteration
        sum+=i   #sum=sum+i
    return sum
print(find_sum(5))   #function calling 