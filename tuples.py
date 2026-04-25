# tuples are another type of method tht cannot changed once it is used  
tup=(1,2,3)
print(tup)
print(type(tup))
# (1, 2, 3)
# <class 'tuple'>
# if we try to add a element than it will give an error
# tup[0]=11
# print(tup)
# Traceback (most recent call last):
#   File "c:\Users\muhammad nazeem\OneDrive\Desktop\codes\tuples.py", line 8, in <module>
#     tup[0]=11
#     ~~~^^^
# TypeError: 'tuple' object does not support item assignment
# but in list we can add or delete the item  anytime
h=("green","blue","red","orange")
print(type(h),h)
# <class 'tuple'> ('green', 'blue', 'red', 'orange')

# we can display the elemernt in output   
print(h[0])
print(h[3])
print(h[1])
print(h[2])
# the output will be 
# green
# orange
# blue
# red
# positive indexing is same in tuple and list   
print(h[-3])
print(h[-2])
print(h[-1])

# blue
# red
# orange
for green in h:
    print("yes")
# yes
# tuple  slicing
print(h[1:4])
print(h[:])
print(h[3:4])
print(h[-3:-1])
print(h[0:3])
print(h[1:3])
# the output is    
# ('blue', 'red', 'orange')
# ('green', 'blue', 'red', 'orange')
# ('orange',)
# ('blue', 'red')
# ('green', 'blue', 'red')
# ('blue', 'red')
print(h[1:3:2])
print(h[1:4:2])
# ('blue',)
# ('blue', 'orange')