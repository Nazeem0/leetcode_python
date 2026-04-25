# today we are going to study about string slicing
# it is a continuation of string 
# example
name="muhammad nazeem"
print(name[0:6])
# we can obtain a  half of string we can sting slicing
# it uses index notation from 0 to any number
# we can also find the length of the string using len() function
# for example
print(len(name))
fruit="mango"
len1=len(fruit)#takes length of fruit
print("mango is a ",len1,"character word" )

print(fruit[2:4])#gives letter from  index 2to three but it will not give  till four  because index starts from 0(first value )  including 2 but not including 4  
print(fruit[0:-3])#reverse slicing 
print(fruit[0:len(fruit)-3])#lengthg of fruit- 3
print(fruit[:4])
print(fruit[-3:-1])#len(fruit)-3:len(fruit)-1 ans is 5-3:5-1=2:4 that is ng
alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i  in alphabets:
      print(i) 
      
nm="nazeem"
print(nm[-4:-1])   
