# python doc strings ae string literals that appear after the definition of function,method,class,or module
# for example 
def square(n):
    '''Takes a number  n, returns the square of n''' 
    print(n**2)
square(5)   
# here it will give the output of 25 
# but it does notreturn any description  that return in triple code 
# but if we write it as 
print(square.__doc__)
# 25
# Takes a number  n, returns the square of n
# it will give the description of the  function
# in order to get the docstrings we need to put three quotes  like above 
# its not like comment python considers it as a special case 
# if we change te doc sTRING  then the we can changer the program
# comments are ignored ,docstrings cannot be         
# butn if we give print(n) or print(n**2) the there will be no docstrings it will become none 
def square(n):
    print(n)
    '''Takes a number  n, returns the square of n''' 
    print(n**2)
square(5)   
print(square.__doc__)
# the output is 
# 5
# 25
# None
# it will become none .it will print 5,25 and none but not description  we should put describe docstring right below the function name like above fnction
# PEP -8
#  pep-8 is a guidline and best practice for python code                    
# to make python program consistent,readable,maintainable
# the full form is python enhancement proposal      
# ZEN OF PYTHON           
# if we put 'import this' then it will give poem of tim  peters