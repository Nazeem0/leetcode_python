# joining the set                    
# union method is used to join the two sets

s1={1,2,3,4}
s2={5,6,7,8}
print(s1.union(s2))
# the output will be 
# {1, 2, 3, 4, 5, 6, 7, 8}
# but during the process s1 and s2 remains untouched but we can update the s1 or s2 sets by using the update method
s1.update(s2)
print(s1)
# this is the updated form of the s1 sets it is same as union method but the difference it will update in first or second set
# {1, 2, 3, 4, 5, 6, 7, 8}
s3={"tokyo","osaka","japan"}
s4={"japan","madrid","nigeria"}
print(s3.union(s4))
# the output will be
# {'madrid', 'tokyo', 'japan', 'osaka', 'nigeria'}
cities={"tokyo","osaka","japan"}
cities4={"japan","madrid","nigeria"}
print(cities.intersection(cities4))
# the output will be 
# {'japan'}
# we can also use intersection update function to update the either one of the sets with the intersection values and rest of tem are removed   
cities={"tokyo","osaka","japan","madrid"}
cities4={"japan","madrid","nigeria"}
cities.intersection_update(cities4)
print(cities)
# the ooutput will be 
# {'japan', 'madrid'}
cities1={"tokyo","osaka","japan"}
cities5={"japan","osaka","nigeria"}
cities3=cities1.symmetric_difference(cities5)
print(cities3)
# the output will be
# {'tokyo', 'nigeria'}
cities6={"tokyo","osaka","japan","berlin"}
cities5={"japan","osaka","nigeria"}
citis=cities6.difference(cities5)
print(citis)
# the output is 
# {'berlin', 'tokyo'}
cities6={"tokyo","osaka","japan","berlin"}
cities5={"japan","osaka","nigeria"}
citiees=cities6.isdisjoint(cities5)
print(citiees)
# disjoint set means there should be no intersection  btw the two sets 
# then the output is 
# False
# it gives the true or false value
# another example 
cities7={"tokyo","osaka1","japan1","berlin"}
cities8={"japan","osaka","nigeria"}
citieees=cities7.isdisjoint(cities8)
print(citieees)
# the output will be
# True
# superset method to check whether the set is a super set of another set  or  checks whether the elements of set b is already present in set a  if its true then it returns true otherwise false   

cities9={"tokyo","osaka","japan"}
cities10={"japan","osaka","nigeria"}
print(cities9.issuperset(cities10))
# the output will be 
# False
cities11={"tokyo","osaka","japan","nigeria"}
cities12={"japan","osaka","nigeria"}
print(cities11.issuperset(cities12))
# the output will be 
# True
# sub set method    \
    #  checks whether the  set b is subset of    set a  if its true then it returns true otherwise false   
    # the set b elment should be present in set a   

print(cities12.issubset(cities11))
# the output is 
# True
# add method is used to add a new element to the set 
cities15={"tokyo","osaka","japan","nigeria"}
cities15.add("helsinki")
print(cities15)
# the output is    
# {'tokyo', 'helsinki', 'osaka', 'nigeria', 'japan'}
# update method is similar to the union method means updating or adding tyhe second set elements
cities17={"tokyo","osaka","japan","nigeria"}
cities16={"helsinki","london","madrid"}
cities17.update(cities16)
print(cities17)
# the output is 
# {'tokyo', 'osaka', 'london', 'japan', 'nigeria', 'helsinki', 'madrid'}
cities17={"tokyo","osaka","japan","nigeria"}
# remove method is used to remove an item from the list         
cities17.remove("osaka")
print(cities17)
# the output will be 
# {'japan', 'tokyo', 'nigeria'}
# the main difference btw the remove and discard method is  that the remove method will raise an error  if there are no such Element and discard method will not raise an error if there are no such element     
cities17={"tokyo","osaka","japan","nigeria"}

cities17.discard("osaka1")
print(cities17)
# the output is 
# {'nigeria', 'osaka', 'tokyo', 'japan'}
# cities17={"tokyo","osaka","japan","nigeria"}
# cities17.remove("osaka1")
# print(cities17)
# it will show you the error 
# Traceback (most recent call last):
#   File "c:\Users\muhammad nazeem\OneDrive\Desktop\codes\setmethods.py", line 104, in <module>
#     cities17.remove("osaka1")
# KeyError: 'osaka1'
# item method is used to pop a random element from the set
cities17={"tokyo","osaka","japan","nigeria"}

item=cities17.pop()
print(cities17)
print(item)
# the outpput will be    /
# {'nigeria', 'osaka', 'japan'}
# tokyo
# del is a keyword which is used to delete the entire set    
# cities17={"tokyo","osaka","japan","nigeria"}

# del cities17
# print(cities17)
# # the output will be 
# Traceback (most recent call last):
#   File "c:\Users\muhammad nazeem\OneDrive\Desktop\codes\setmethods.py", line 124, in <module>
#     print(cities17)
#           ^^^^^^^^
# NameError: name 'cities17' is not defined. Did you mean: 'cities1'?
# clear method is used tto clear the entire list  element

cities17={"tokyo","osaka","japan","nigeria"}

cities17.clear()
print(cities17)
# the output will be
# set()
# check if items is present 

cities16={"helsinki","london","madrid"}
if "helsinki" in cities16:
    print("it is present")
else:
    print("its not present")
    # the output will be 
    # it is present