# while loop and for loop are very similar 
# for example 
for i in range(3):
    print(i)
# if we do it in while loop it will be  
i=0  
while i<3:
    print(i)
    i=i+1
    # but in while loop we need to declare the variable but that is not there in for loop 
# first initialization 
# checks the comdition 
# ifits true then then prints the output 
# at last increement of thew variable 
# but in for loop in a single line it is defined all the iniutialization and condition and increement and printing    
#  or we can we take the input from the user    #
a=int(input("enter the element"))
while (a<=38):
    a=int(input("enter the element"))
    print(a)
print("done with this loop")
# the output will be given
# enter the element23
# enter the element2
# 2
# enter the element23
# 23
# enter the element34
# 34
# enter the element12
# 12
# enter the element23
# 23
# enter the element23
# 23
# enter the element45
# 45
# done with this loop
# if the value of the a is given less than 38 but inside the while loop if we give more than 38 it will stop the loop and comes out of the loop an prints the last statement 
# the while loop checks both the outer tnput and inner input also
# if the outer  input is false then it will not enter into the loop
# decreement loop
# but if we give count+1 instead of -1  it will give an infinite loop
count=5   
while count>=0:
    print(count)
    count=count-1
else:
    print("i am inside else")
    #  we can also add else to the loopas shown above
# 5
# 4
# 3
# 2
# 1
# 0
# i am inside else
# in python there is no do while loop
# but the syntax is    
# do{
#    loop body      
# }while(condition);
# if er run the bdo while loop it will give an error 
# but once it is written in c or c++ it will give atleast once the output if the condition is true or false             
# it is also known as th "exit controlled loop"  
print("\nDo-While loop in python")
while(True):
  number=int(input("Enter the positive number: "))
  print(number)
  # if not number>0:
  #  break
  if number<0:
       break
#    and the output is given below 
#    Do-While loop in python
# Enter the positive number: 1
# 1
# Enter the positive number: 1
# 1
# Enter the positive number: 1
# 1
# Enter the positive number: -1
# -1
