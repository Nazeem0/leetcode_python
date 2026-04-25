# function are used to  repeat the a statement or operations any number of times   
# a function is a block of code that is used for specific functions that executes when its called 
# for example 
# to find a mean       
# a=13    
# b = 5
# mean=(a+b)/2
# print(mean)
# # BUT IF WE PRINT AGAIN ANOTHER VARIABLE THEN 
# C=4 
# D=4
# CMEAN=C+D/2
# print(CMEAN)
# but if we need to write more than 10 times it will be  a very long program and its a waste of time instead of that we can use the functions
# for ex 
# here def is to define the function 
# mean is function name
# aand b are arguments 
# m=mean formula
# return function is used to return the functions
# and at the bottom the mean function is calledwith arguments  
def mean(a,b):
    m=(a+b)/2
    return m  
print(mean(3,5))
# and the output is 4.0 
# we can give any value
# we can call the function as much as you want
# like
print(mean(2,3)) 
print(mean(4,7)) 
print(mean(5,6)) 
# and the outputs are            
# 2.5
# 5.5
# 5.5
# or we can also  give the print function at the function define     
def ma(a,b):
    m=(a+b)/2
    print( m ) 
ma(4,6)
ma(6,5)
ma(5,4)
# nd he outputs are           
# 5.0
# 5.5
# 4.5

# for greater than or smaller function /
def comp(e,f):
    if e>f:
       print("e is greater than f")
    else:
        print("f is greater than e") 
comp(4,5)
comp(9,5)
# the output is 
# f is greater than e
# e is greater than f
# if we not the bodyn of the function yhen it will give an error
# but if we give pass in body of the function it will execute the other program
def lesser(e,f):
     pass
# def lesser(e,f):
#     if e<f:
#         print("e is lesser than f")
#     else:
#         print("f is lesser than e")
# lesser(4,5)
# lesser(9,5)
# the output
# e is lesser than f
# f is lesser than e
 # and also we can pass any number of arguments in the function   

  
  
  
  