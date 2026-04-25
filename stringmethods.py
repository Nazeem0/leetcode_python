# today we arte going to study about conversinons
# strings are immutable
a="nazeem"
# we can get a  length of string using a len function
print(len(a))
# we can also convert the string into lower or upper case
# for example
print(a.lower())
print(a.upper())
# lower()function is to convert string to lower function
# upper() function is to convert string to upper function as shown above
# since the string are immutable it cannot be changed  but it creates a new string based  on  existing string 
# for ex here b is a string if we apply lower or upper function it does not change the  original string instead of that it gives a new string with upper or lower alphabets
b="NAZEEM"
print(b.lower())
print(b.upper())
# rstrip() function is used to strip the unwanted parts of the string
# it only strips the right side unwanted parts of the string
c="Nazeemm1111111111"
print(c.rstrip("1"))
print(c.rstrip("m"))
print(c.strip("N"))
d="@@@@muhammad nazeem11111"
# lstrip():it is used to strip the unwanted parts of the string from  left side
print(d.lstrip("@"))
print(d.rstrip("1"))
# replace()function is used to replace all the string from another string
e="nazeem11111"
print(e.replace("nazeem","irfan"))
f="nazeem1111nazeem"
print(f.replace("nazeem","irfan"))
# note:these functions can only be used for strings
# split function is used to split the function  and gives a string
#  we can give any alphabet or wite space  or special characters if it nis present in string
i="nazeem nazeeemm nazeemmm !!!!"
print(i.split(" "))
# this will be the output of program 
# ['nazeem', 'nazeeemm', 'nazeemmm', '!!!!']
# capitalize() function is used to capitalize the first letter of the string  and also converts the strings in the lower case
# for example it will convert the i of introduction to capital I
heading="introduction to python "
print(heading.capitalize())
# as written  above
blog="welcome muhammaD nazeem"
print(blog.capitalize())
# center function :it is used to center the string
g="welcome to python nazeem"
print(g.center(50))
# it gives 50 spaces from  the begining
# if we want to print the len of the g
print(len(g.center(50)))
print(len(g))
# count function is used to count the particular word in string or letter
h="nazeem is a nazeem and nazeem"
print(h.count("nazeem"))
print(h.count("e"))
# ends with function is used to  check whether the function ends with  some letter or alphabet or  special character
j="nazeem1234567"
print(j.endswith("1234567"))
# the output will be in boolean value true or false
k="welcome to the console"
print(k.endswith("to",4,10))
# we can also check whether it is  true or false in between the index
# find() method  is used to  find the  string or gives the specific  index
print(k.find("to"))
# it only detects  which comes first 
print(k.find("hello"))
# if there is no word then it will give -1
# index function: it  is similar to find() method but in find if there is no letter then it will give -1 output but in index method it give error
# print(k.index("hello"))
# ValueError: substring not found(it will give the output like this)
# isalnum():it is used to check whether the string  is alphanumerical
l="welcometoconsole1234"
print(l.isalnum())
# it should only consist of alphabets or numerical characters and should not consist of spaces or special characters  otherwise it will give error
# isalpha():it is used to check whether the there are only capital or small alphabets  and should not consist of any number or space or special case
m="welcometoconsole"
print(m.isalpha())
# otherwise it will give an error 
n="welcome00"
print(n.isalpha())
# it will give you the output False
# islower()  function is used to check whether the string is lower or not
o="welcome"
print(o.islower())
# if it is lower case it will give boolean value true or else boolean value false
# isupper() function is used to check whether the function is upper case or not 
p="WELCOME"
print(p.isupper())
# if it is true it will written  boolean value true or else boolean value false
# isprintable()  checks whether the all the  value in string are printable or it will return false
q="welcome,nazeem"
print(q.isprintable())
# if it is correct it will give true
r="welcome to python\n"
print(r.isprintable())
# it will give false because it  \n cannot be written but it can return true if it is \" or \' but not for \n or \0
# isspace() function is used to check whether th  string has swhiteapce or not
s="welcome nazeem"
print(s.isspace())
t="    "
print(t.isspace())
# istitle  checks whether the first character is  of a word is capital
# if it is capital then it gives true
# or else it gives false
u="World Health Organization"
print(u.istitle())
w="world health organization"
print(w.istitle())
# startswith() is similar to endswith function
# checks whether the  string starts with  a given  word  for example
x="world health organization"
print(x.startswith("world"))
# if its true it returns true or else it return false
# swapcase() is  conversion of upper csae to lower  case
y="World Health Organization"
print(y.swapcase()) 
# title() is used to  convert every first letter of the word to capital

z="world health organization"
print(z.title())

 
