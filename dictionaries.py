# these are key value pairs                   
# these are the  ordered collection of data items they store multiple  items in a single variable  it is a key value pair               
# for example   
dic={
    "nazeem":"human being",
    "spoon":"object"
}
print(dic)
# the output will be 
# {'nazeem': 'human being', 'spoon': 'object'}
# we can also print the keys or values 
print(dic.keys())
# the output will be 
# dict_keys(['nazeem', 'spoon'])

print(dic.values())
# the output will be   
# dict_values(['human being', 'object'])
# we can also print the  values of the keys 
print(dic["nazeem"])
# the output will be 
# human being
disc={
    4:"muhammad",
    5:"naz",
    6:"nazeem"
}
print(disc[4])
# the output will be 
# muhammad
# but if we access it keys using keys that are not present using bracket notation it will give aN ERROR    
# but if we access it keys using keys that are not present using DOT notation it will give  OUTPUT AS NONE  
# example  
# print(disc[45])  
# the output will be      
# Traceback (most recent call last):
#   File "c:\Users\muhammad nazeem\OneDrive\Desktop\codes\dictionaries.py", line 34, in <module>
#     print(disc[45])
#           ~~~~^^^^
# KeyError: 45
# else 
for key in disc.keys():
    print(f"the value of the {key}is   {disc[key]}")
    # the output will be 
    # the value of the 4is   muhammad
    # the value of the 5is   naz
    # the value of the 6is   nazeem

# if you want both then items method  will give it in key value pairs  
print(disc.items())       
# the output will be 
# dict_items([(4, 'muhammad'), (5, 'naz'), (6, 'nazeem')]) 
for key,value in disc.items():
     print(f"the value of the {key}is{value}")
    #  the output will be 
#      the value of the 4is   muhammad
# the value of the 5is   naz
# the value of the 6is   nazeem
print(disc[4])#it will give random output 
# muhammad

