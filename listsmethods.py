# append method is used to enter the value to the end of the existing string 
# for ex     
l=[1,2,3,4,]
print(l)
l.append(7)
print(l)
# the output will be  
# [1, 2, 3, 4]
# [1, 2, 3, 4, 7]
# yhge insert method is used to insert the element at the specific index 
# here the first value is index  and second value is data
l.insert(1,8)
print(l)
# [1, 8, 2, 3, 4, 7]
# sort method is used to sort the vlues in the arrays  
# for ex       
a=[3,2,4,1,9,4,2,7]
a.sort()
# but if we want to get it in descending order 
# a.sort(reverse=True)
# print(a)
#  the  output will be  
# [1, 2, 2, 3, 4, 4, 7, 9]
# [9, 7, 4, 4, 3, 2, 2, 1] 
# or we can use reverse method 
a.reverse()
print(a)
# /the output will be 
# [9, 7, 4, 4, 3, 2, 2, 1] 
color=["green","blue","red","orange"]
color.sort()
print(color)
# the output is   
# ['blue', 'green', 'orange', 'red']
# index method returns the index of the first occurence of the list item 
b=[44,55,22,15,5,5,5,5]
print(b.index(55))
print(b.index(22))
# the value inside the bracket is data value 
# the output is 
# 1
# 2
# print(color.index("green"))
# output is 
# 1
# because it gives from the value of the list in colort
# count method is used to count how mwny times data is  present in the list 
print(b.count(5))
# the output is 
# 4
# the copy function is used to copy the origional list and modify the copied list 
# for ex          
c=[10,2,3,6,7,4]
d=c    
d[0]=20
print(d)
# then the output is 
# [20, 2, 3, 6, 7, 4]
# but instead of that we can use the copy method 
e=c.copy() 
print(e)
# [20, 2, 3, 6, 7, 4]
# if we make changes in d then it  will effect the e also 
# entend method is used to join the two list or extend it with another list     
f=[10,2,3,6,7,4]
g=[44,55,22,15,5,5,5,5]
f.extend(g)
print(f)
# the output is 
# [10, 2, 3, 6, 7, 4, 44, 55, 22, 15, 5, 5, 5, 5]

i=["green","blue","red","orange"]

h=["green","blue","red","orange"]
i.extend(h)
print(i)
# the output is
# ['green', 'blue', 'red', 'orange', 'green', 'blue', 'red', 'orange']
# concatinating the list    another way to join the list      
g=[44,55,22,15,5,5,5,5]
m=[10,2,3,6,7,4]
k=g+m
print(k)
# the output  is       
# [44, 55, 22, 15, 5, 5, 5, 5, 10, 2, 3, 6, 7, 4]
