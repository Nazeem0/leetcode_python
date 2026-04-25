# today we are going to  study pythoon
# strings are written usig  double quotes or single quotes (""or'')
# string islike  array of textual data taht are enclosed with quotes 
name="nazeem"
state="discipline"
print("the name is "+name+ "the state is"+state)
# it doesnot matter whether the string is quoted with double or single
# sometime we might might make the string as part of string  by using backslash and quotes
apple="he wants to an \"apple \" "
print(apple)
# or we can use single code in the end
banana='he wants to have a \"banana\"'
print(banana)
# multiple strings 
hi="""hi,nazeem 
 how are you 
 are you fine"""#  we can use triple single quote or double
print( hi)
# indexing :location of an element or letter 
# indexing always starts with 0 
# for example 
print(name[0])
print(name[1])
print(name[3])
print(name[2])
print(name[4])
# then it will just give the first letter 
# and it goes on like 0,1,2,3,4,5,6,7
# if you give more value than index  then it will give index error
# for multiple lines we can use a for loop 
for character in hi:
    print(character )
# or 
for character in name:
    print(character)
