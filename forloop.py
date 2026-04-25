# for loop
# it is a iteration  means it is used to repeat over and over  to print  that is present in that iterations
# for example to print  the number from 1 to 20
for i in range(1,21):
    print(i)
    # here it helps to print the number from one to 20
    # or to print other functions

name="muhammad nazeem"
# print(name.capitalize())
# print(name.title())
# print(name.upper())
# print(name.count("a"))
# print(name,sep="%")
# print(name.split(" "))
# print(name.replace("nazeem","irfan"))
# print(name,end="_")
# or if we want to print the letters of the name 
# for example
for i in range(len(name)):
    print(name[i])
# or we can also give as
for i in name:
    print(i)
    # it will give the letters of the name  as shown in output
# m
# u
# h
# a
# m
# m
# a
# d

# n
# a
# z
# e
# e
# m
# m
# u
# h
# a
# m
# m
# a
# d

# n
# a
# z
# e
# e
# m
for i in  name:
    print(i)
    if i=="a":
        print("this is something special")    
        
# we can also put if statement in for loop also
# for loop in list
colors=["red","blue","green"]
for color in colors:
    print(color)
# we can get the letters also
    for i in color:
        print(i)
# red
# r
# e
# d
# blue
# b
# l
# u
# e
# green
# g
# r
# e
# e
# n
# it will give you the output like this
# you can use the rangeb function to print the range of numbers as shown below
# the output will be given below
for k in range(5):
    print(k)
# 0
# 1
# 2
# 3
# 4
for k in range(1,16):
    print(k)
# it will print from 1 to 15 but not 16
# we can also  give the difference     
for k in range(1,16,2):#but if we give floating point numbers in for loop it will give the error
    print(k)
# here the first one is starting point and second one is ending point (number-1)not gives the last number but before that number and the third one is difference or (if we give the any number like 2 and if it starts from 1 that will give the difference of two numbers ) as shown below 
# the output will be
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15


