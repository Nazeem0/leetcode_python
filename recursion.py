# they are basically functions that are repeated again and again      
# it is mainly used for factorial     
        # factorial means:
# for example 
# 5!=5*4*3*2*1
# 4!=4*3*2*1
# but in order to run it as program to find the factorial of any number 
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
print(factorial(2))
print(factorial(4))
# the output is      
# 120
# 2
# 24
# fibonacci series 
n=int(input("enter the number of elements"))
n1=0
n2=1

count=0   
sum=0   
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    while(count<n):
        print(sum)
        n1=n2
        n2=sum
        sum=n1+n2
        count=count+1