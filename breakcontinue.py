# a brteak statement enables the program to skip over the part of program
# a break statement terminates the very loop it lies within
# for example
for i in range(0,11):
    print(i)
    if(i==5):
        break
# 0
# 1
# 2
# 3
# 4
# 5
# and the output is as showm above
# but if we give an else statement then the output is    
for i in range(0,11):
    print(i)
    if(i==5):
        break
    else:
        print("continue loop")
#         0
# continue loop
# 1
# continue loop
# 2
# continue loop
# 3
# continue loop
# 4
# continue loop
# 5
# th eoutput is as shown above 
# another example
for i in range(12):
    print("5*",i+1,"=",5*(i+1))
    if(i==9):
        break
# break statement will come out of loop
# 5* 1 = 5
# 5* 2 = 10
# 5* 3 = 15
# 5* 4 = 20
# 5* 5 = 25
# 5* 6 = 30
# 5* 7 = 35
# 5* 8 = 40
# 5* 9 = 45
# 5* 10 = 50
# but if we give the if statement above then the output will be
for i in range(12):
    if(i==9):
        break
    print("5*",i+1,"=",5*(i+1))
#     5* 1 = 5
# 5* 2 = 10
# 5* 3 = 15
# 5* 4 = 20
# 5* 5 = 25
# 5* 6 = 30
# 5* 7 = 35
# 5* 8 = 40
# 5* 9 = 45
#  it will only give till nine
# but if we put i==10 at the begining
for i in range(12):
    if(i==10):
        break
    print("5*",i+1,"=",5*(i+1)) 
    # the output will be 
#     5* 1 = 5
# 5* 2 = 10
# 5* 3 = 15
# 5* 4 = 20
# 5* 5 = 25
# 5* 6 = 30
# 5* 7 = 35
# 5* 8 = 40
# 5* 9 = 45
# 5* 10 = 50
# we can also use  in the while loop 
# but in continue statement it will come out of iteration 
for i in range(12):
    if(i==10):
      print("come out of the iteration")
      continue
    print("5*",i,"=",5*i) 
    # 5* 1 = 5
# 5* 2 = 10
# 5* 3 = 15
# 5* 4 = 20
# 5* 5 = 25
# 5* 6 = 30
# 5* 7 = 35
# 5* 8 = 40
# 5* 9 = 45
# come out of the iteration
# 5* 11 = 55
# the output of the above  continue statement is given below 
for i in[2,3,4,5,6,7,8,9,10]:
    if(i%2==0):
        continue
    print(i)
#     3
# 5
# 7
# 9
for i in[2,3,4,5,6,7,8,9,10]:
    if(i%2!=0):
        continue
    print(i)
    
# 2
# 4
# 6
# 8
# 10
# hence the output is above 
# but if we use in while loop 
#  and it is also example of do while loop
    i=0
    while True:
        print(i)
        i=i+1
        if(i%10==0):
            break
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 8
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# it will be the output of the program 
# first it will print the details and then checks the output 