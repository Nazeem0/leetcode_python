# in c if we dont put break after each case it also print the other case statements also
# match case statements are  similar to statements used in c or c++ 
# its similar to  choosing options 
# its different from statements used in python  
x=int(input("enter the value of x"))
match x:
   case 0:
       print("x is 0")
   case 1:
        print("x ios i")
   case 4:
        print("x is 4")
   case _ if x!=90:
        print("x is not 90")
   case _ if x!=100:
        print("x is not 100")    
# x=any number
# here we use  match keyword to define x or to define any word
# case are   different options that are used to match the  value of x or any other value
# if the value(for example x as shown in above) is correct then it would print or do the following operations
# there can be as many number of cases  as the user wishes
# for default we use '_'(underscore keyword )to determine that it is default  and ending of match case statement
# if we give a value that is not there in cases then it will goes to match case statement as shown above 
# if we give 10then it will go to default and print the statements as shown above
# if we put the value of x as 1 then it will print the statements inside that cases
# here in  python we are not going use the brek statement like we use in c or c++ because it is manmdotary and it will automatically come out of the match conditions
# in default statement we can also give the if statement  as shown above
# in case _ if x!=90 if the value of x is not 90 then it will print the statement of that case
# in case _ if x!=80 if the value of x is not 90 then it will print the statement of that case
# but here which ever  case comes first in default statement it will print the  statement of that case 
# as shown above
#  x is not 90(this will be the output if we give x=100)
#  x is not 100(this will be the output if we give x=90)
# if none of the cases are matched then it willgo to the default statement  and it is similar to else statement


