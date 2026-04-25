# today we are going to study about function arguments 
def average(a,b):
    print("the average is ",(a+b)/2)


average(5,10)
# there arew four types of arguments   that we can provide in function
# * default arguments 
# * keyboard  arguments 
# * variable length   arguments 
# * required   arguments 
# default arguments : means we can give values  while passing the arguments itself   and these are called default arguments 
# example
def average(a=1,b=10):
    print((a+b)/2)
average()
# and we can also give the arguments while calling the function  and it will the consider the values from this function not from the arguments 
def average(a=1,b=10):
    print((a+b)/2)
average(2,2)
# it will run the program still if we do not the value while calling
#  we can also give only value fo ex
def average(a=1,b=10):
    print((a+b)/2)
average(3)
# here i have only given  value for a and did not for b still it will change the only value of a ,b remains same  
# the average is  7.5
# 5.5
# 2.0
# 6.5


# Nonebut if we need to pass the value for b  then it will be
def average(a=1,b=10):
    print((a+b)/2)
average(b=3)
# we should gin=ve the variable name 
def name(fname,mname="D",lname="nazeem"):
    print("hello ", fname, mname,lname)
name("muhammad")
# the output is 
#hello  muhammad D nazeem
# its the example for default argument 
# keyword arsguments = with the help of this argument we can change the order of the arguments  as we want  
def name(fname,mname,lname):
    print("hello ", fname, mname,lname)
print(name(fname="muhammad",lname="nazeem",mname="D"))
# the output is 
# hello  muhammad D nazeem
def average(a=1,b=10):
    print((a+b)/2)
print(average(b=3,a=3))
# 3.0
# but if you want to give any two  value but it has three arguments then it would  be 
def avera(a,b,c=3):
    print((a+b+c)/2)

avera(2,3,4)
avera(a=1,b=3,c=1)
# 4.5
# 2.5
# arbitrary function :while creating a function pass* berfore define the parameter name while defining them.the function accesses the arguments by processing them in the form of tuple
# example :
def name(*name):
    print("hello ", name[0], name[1],name[2])
name("muhammad","D","nazeem")
# hello  muhammad D nazeem 
def average(*numbers ):
    print(type(numbers)) #<class 'tuple'>
    sum=0
    for i in numbers:
        sum=sum+i
        avg=sum/len(numbers)
        print(avg)
        
average(4)
# 4.0
# it is also an example of arbitrary length 
# we can also use the dictionary 
# ex      
def name(**name):
    print(type(name))#<class 'dict'>
    print("hello",name["fname"],name["mname"],name["lname"])
    
name(fname="muhammad",lname="nazeem",mname="D")   

# hello muhammad D nazeem (output)
# return statement:it used to return the value to th calling function and we can print it there 
# ex
def average(*numbers ):
    print(type(numbers)) #<class 'tuple'>
    sum=0
    for i in numbers:
        sum=sum+i
        avg=sum/len(numbers)
        return avg
        
        
print(average(4))
# <class 'tuple'>
# 4.0
def average(*numbers ):
    print(type(numbers)) #<class 'tuple'>
    sum=0
    for i in numbers:
        sum=sum+i
        avg=sum/len(numbers)
        return 7
        return avg
        
        
print(average(4,5,6,7,8,9))
#  it will return the value which ever comes first if 7 comes then it will return 7 or else average 
# output 
# 7
def name(fname,mname,lname):
    print(type(name))
    return "hello "," "+fname," "+ mname," "+lname
print(name("muhammad","nazeem","D"))
# ('hello ', ' muhammad', ' nazeem', ' D')  (output)
# it will clear once we clear the tuple 