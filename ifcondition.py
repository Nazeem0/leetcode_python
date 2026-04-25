# today we are going to study  if conditions 
# if statements are used to check the conditions are true ar false  and returns the output based on conditions 
# for example 
#  some ohf the conditional operators are
# > < >= <= == !=
a=int(input("enter your age"))
print("your age is",a) 
# print(a>18)
# print(a<18) 
# print(a!=18) 
# print(a==18) 
# print(a<=18) 
# print(a>=18) 
# THIS WILL CHECK WHETHR  a is edual or not or others operations as shown above an give true or false values


if(a>=18):
    print("you can drive")

else:
    print("you cannot drive")
print("have  a nice day")
# it consist of  an indentation  that is main in python 
# if we use indentation  in if then it means that youre starting a block of code 
# after giving the colon and press enter it will automatically  give a space  tht is called indentation
# in if condition if the condition is false then it will not print the statement inside them 
# else statement: but in else  if there is no condition also it will print the statement only if the if statement is false
# if we give any statement outside the indentation block then as always it will print that statement\
#but you cannot give in the middle of the if statement or in between elif statement it will give an error
# it is always written at the end of the else  statement outside the block 
# in if statement the  condition is true it will print the output otherwise  it will go to else statement and print it

# elif statement :it is used to when we want to print more than one condition to check and to print output


b=int(input("enter your age"))
print("your age is",b)
if(b>=18 and b<60):
    print("you can drive")
elif(b>60):
    print("you are very old to drive you cannot drive correctly")
# it similar to if statement but we use keyword elif
else:
    print("you cannot drive")
print("have  a nice day")

num=int(input("enter the number"))
if(num<0):
    print("number is negative")
elif(num==0):
    print("number is zero")
elif(num==999):
    print("number is special")
else:
    print("its positive ")
print("im happy")
# nested if statement  means  an  if statementb or elif contains another  condition 
# as shown below in example 
n=18 
if(n<0):
    print("its negative")
elif(n>0):
    if(n<10):
        print("its less than 10")
    elif(n>10 and n<50):
        print("its between the 10 and 50")
    else:
        print("its greater than 50")
else:
    print("its zero" )
    
    

