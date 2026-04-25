# string formatting python           
# for example 
letter="hey my name is {} and I am from {}"
country="india"
name="nazeem"


print(letter.format(name,country))
# here format method  takes name from the name and puts inside the first paranthesis and country name in second paranthesis 
# the output is 
# hey my name is nazeem and I am from india
# but if we gave name and country reverse the the output will be
print(letter.format(country,name))
# the output will be
# hey my name is india and I am from nazeem
# we can also number in paranthesis for accessing
letter="hey my name is {1} and I am from {0}"
country="india"
name="nazeem"
print(letter.format(country,name))
# output is 
# hey my name is nazeem and I am from india
# and index begins with 0,1,...... 
# becaue of this  it becomes very complicated 
# so for that we use f string              
# ex        
print(f"hey my name is {name} ,Iam from {country}")
# the output is 
# hey my name is nazeem ,Iam from india    
txt="for only {price:.2f} dollars !"
print(txt.format(price=49.99999))
# the output is 
# for only 50.00 dollars !
# instead of that         
price=49.0999
txt=f"for only {price:.2f} dollars !"

print(txt)
# the output is   
# for only 49.10 dollars ! 
n="muhammad nazeem"
print(f"my name is {n}")
# the output is 
# my name is muhammad nazeem            
# the the type of class is string 
print(type(f"{2*30}"))
# the output is    
# <class 'str'> 
print(type(f"{name}"))
# /the output is      
# <class 'str'>  
# if we want toprint the curly brackets then we use f strings like things
print(f"hey my name is {{name}} ,Iam from {{country}}")
# to show the words and paranthesis we use f strings like this  by covering them with {}(paranthesis)
# the output  is   
# hey my name is {name} ,Iam from {country}
