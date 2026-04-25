# since we cannot add any value to tuple 
# we have to convert it to list 
tup=("green","blue","red","yellow")
temp=list(tup)
temp.append("white")
print(temp)
# output will be
# ['green', 'blue', 'red', 'yellow', 'white']
temp.pop(3)#3 is index va;ue 
print(temp)
# the output will be
# ['green', 'blue', 'red', 'white']
temp[2]="purple"
tuple=tuple(temp)
print(tuple)
# the output will be
# ('green', 'blue', 'purple', 'white')
# but if there are 5 items then it must contain 5 items only   
# but there some methods like count method 
temp1=(1,2,3,4,5,5,6,6,6,6)
print(temp1.count(6))
# the output is 
# 4
print(temp1.index(3))
# the output is 
# 2
# but if we wnt to look it in some Portion           
temp2=(3,5,3,4,2,3,7,5,3,3)
print(temp2.index(3,3,8))#here he first value is element to find ,second is starting position ,third is ending position
# the output is 
# 5
# len function is used to give the length of the object
res=len(temp2)
print(res)
# output will be
# 10