#finding sum of numbers using recursion
#n=4
#4 + find_sum(4-1) = 4 + find_sum(3) 1st cycle
#4 + 3 + find_sum(3-1) = 4 + 3 + find_sum(2) 2nd cycle
#4 + 3 + 2 + find_sum(2-1) = 4 +3 + 2 + find_sum(1) = 4+3+2+1=10
#4+3+2+1=10


def find_sum(n):
    if n==1:
        return 1
    return n+find_sum(n-1)
print(find_sum(4))