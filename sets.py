# set is a best example of datatype that doesnot consist of repeated entries and it doesnot maintain order it is enclosed within curly brackets
s={2,4,2,6}
print(s) 
# the ooutput is 
# {2, 4, 6}
# it is a example of set where 2,4,2,6 is present in set but while printing it only print 2,4,6
# set can take any datatype items and are also similar to list but it doesnoy repeats item
s1={1,"2",2.18,2.18,False}
print(s1)
# the output is   
# {'2', 1, 2.18, False}
# tuple=()
# list=[]
# sets={}
# sets are unchangable   and they cannot be replacable
# if we create an empty set and print the type of the empty set then the output is
nazeem={}
print(type(nazeem))
# the output will be 
# <class 'dict'>
# because dictionary and set have same syntax for emoty set    
# if we want to get type of set with empty set then we should write            
naz=set()
print(type(naz))
# then the output will be 
# <class 'set'>
# we can access the  items with the help of for loop   
s2={1,"2",2.18,2.18,False}
for i in s2:
    print(i)
# yhe output is      
# False
# 1
# 2.18
# 2
