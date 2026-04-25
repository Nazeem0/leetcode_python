# update value is used to update the value of the key assigned to it oer else it will consider it as new key value pair 
# consider the employeee dictionaries and their marks
ep1={1:49,4:45,456:99}
# now lets if we consider ep2
ep2={122:45,222:48}
# # now if we want to update the value of ep1 with value of ep2 then
# ep1.update(ep2)
# print(ep1)
# # if we execute it then output is 
# # {1: 49, 4: 45, 456: 99, 122: 45, 222: 48}
## clear method is used to   clear the dictionaries\
# ex/
# ep1.clear()
# print(ep1)
# {}
# it will give an empty dictionary
# pop method is used to remove the key value pairs 
# ep1.pop(1)
# print(ep1)
# # {4: 45, 456: 99}
# # it will pop the value and key  that has the key  1 and the answer is shown below
# if we want to remove the last item we have to us ethe command popitem
# ep1.popitem()
# print(ep1)
# {1: 49, 4: 45}hence you can see thatthe last item is removed
# del command is used to delete the delete the entire dictionary 
# del ep1
# print(ep1)
# # File "c:\Users\muhammad nazeem\OneDrive\Desktop\codes\dmethods.py", line 28, in <module>
#     print(ep1)
#           ^^^
# NameError: name 'ep1' is not defined. Did you mean: 'ep2'?
# here you can see that if we print the ep1 taht is already deleted than it will show you an errorlike above
# but if we want to delete a particular key then we need to write as 
# del ep1[1]
# print(ep1)
# {4: 45, 456: 99}then it will delte the key 1
# /if we write it as string yhen we could get an error
# if  we forgot anything then there will be a website called python dictionary documentation
