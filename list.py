# l=[3,5,6]
# print(l)
# print(type(list))
# # lists are the ordered collection of items
# # they store multiple items in single variable
# # they are separated by commas and enclosed with variables
# # list are change able means we can alter the data
# #  to display the marks of the student
# marks=[100,200,99]
# print(marks)
# print(marks[0])
# print(marks[1])
# print(marks[2])
# # the output is    
# # [3, 5, 6]
# # <class 'type'>
# # [100, 200, 99]
# # 100
# # 200
# # 99
# # we can also put different  datatypes in list like string, integer  ,boolean,float etc
# n=[100,"a",True,2.56]
# print(n)
# # the output is [100, 'a', True, 2.56]
# # we can also print marks1,marks 2,marks3
# # list also uses index that is shown above(the index starts from 0 )
# color=["red","blue","green"]
# print(color)
# print(color[0])
# print(color[1])
# print(color[2])
# #  the output is ['red', 'blue', 'green']
# # red
# # blue
# # green
# #  we can also print the length of the color len function 
# print(len(color))
# # the output is    3
# # we can also use negative indexing in list like string
# # negative indexing starts from -1 at the last of the list
# print(color[-1])
# print(color[-2])
# print(color[-3])
# # then the output is    
# # green
# # blue
# # red
# # we can also convert them into positive indexing 
# print(color[len(marks)-3]) #or
# print(color[3-3]) 
# # then the output will remain same that is    red 
# # red 
# # we can use the if statement to check whether the elements are present in list 
# a=[3,5,6]
# if 5 in a:
#     print("yes")
# else:
#     print("no")

# # the output is yes
# b=[3,5,6]
# if 7 in b:
#     print("yes")
# else:
#     print("no")
# # # the output is no
# # n=[100,"a",True,2.56]
# # if "a" in n:
# #     print("yes")
    
# # else:
# #     print("no")
#     # the output is yes
# #  we can also use boolean function to check whether the element is present or not
# #n=[100,"a",True,2.56]
# # if "100" in n:
# #     print("yes")
    
# # else:
# #     print("no")
# # but if we give 100 as a string then will get the output no 
#     # then the output is no
#     #  we can also check whether the string  is present or not
# n=[100,"nazeem",True,2.56]
# if "naz" in "nazeem":
#     print("yes")
    
# else:
#     print("no")
# # then it will give the output yes
# print(n[:])
# # we can also print whole lists like 
# # [100, 'nazeem', True, 2.56] 
# print(n[1:])
# # ['nazeem', True, 2.56]
# print(n[1:3])
# #  output=['nazeem', True]
# print(n[-3:-1])
# # ['nazeem', True]
# print(n[-4:-2])
# # [100, 'nazeem']
# # there is a concept called jump index that means it how many gaps should be taken or like that
# # for example
# d=[100,"nazeem",True,2.56,2,4,5,6,7,]
# print(d[1:9:2])
# # output=['nazeem', 2.56, 4, 6]
# print(d[1:9:3])
# # output ['nazeem', 2, 6]
# # we can also use it in string  
# # list comprehension :
#     # on the spot we are going to print the make the list and generate it     
# #  for example 
# # ls=[i for i in range(1,10)] 
# # print(ls)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# # in simple it means we are using for loop to to generate the list 
# # and in end we are not going to give any colon bcs of list comprehension
# ds=[i for i in range(2,20,3)]#it is the structure of list comprehension
# print(ds)
# # [2, 5, 8, 11, 14, 17] 
# # we can also do index jumping 
# ls=[i*i for i in range(1,10)] 
# print(ls)
# # [1, 4, 9, 16, 25, 36, 49, 64, 81] output
# ls=[i for i in range(1,10) if i%2==0] 
# print(ls)
# # output [2, 4, 6, 8]
# # we can also use if statement 
# cs=[100,200,300,400,500,600,700,800]
# dss=[items for  items in cs[2:7]]
# print(dss)
# # output is [300, 400, 500, 600, 700]
# def runner_up(student_array):
#     student_array=list(student_array)
#     student_array.sort(reverse=True)
#     for score in range(len(student_array)):
#         if student_array[score]!=student_array[score+1]:
#             runner_up=student_array[score+1]
#             break
#         else:
#             continue
#     print( runner_up)        
 
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     runner_up(arr)
#     # thus is an example too find the runer up score in the list of scores
# # the output will be the second highest score in the list of scores
# def grade(names_scores):#grde function
#    scores=[]# scores is a simple list we are going to store the scores in it
#    for names in names_scores:  #iit is a for loop that gives all the names and scores
#        scores.append(names[1])#but we are going to take only the score so we are going to add score in to scores list with the help of the name[1] and tha name[0] is the index for names
#    sorted_score=sorted(set(scores))#in this step we are  going to remove the duplicate scores with help of set function and sirting it 
#    second_lowest_score=sorted_score[1]#and then second lowest score
#    name_sorted_list=[]#here it is the another lisy to store the names of the students 
#    for names in names_scores:#another for loop to take the names 
#       if names[1]==second_lowest_score:#condition to check whether the score is equal to second lowest score
#          name_sorted_list.append(names[0])#inserting it to the second name sorted list
#    sorted_name=sorted(name_sorted_list) #nowagain we are s0rting the name 
#    for name in sorted_name:#for loop
#         print(name)    #print the name

# if __name__ == '__main__':
#     names_scores=[]
#     for _ in range(int(input())):
#         name = input()
#         scores = float(input())
#         names_scores.append([name,scores])
    
# grade(names_scores)
# import math

# def is_prime(n):
 
#     if n <= 1:
#         return False
#     if n == 2 or n == 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     for i in range(5, int(math.sqrt(n)) + 1, 6):
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#     return True

# def primeproduct(m):

#     if m <= 1:
#         return False
    
   
#     for i in range(2, int(math.sqrt(m)) + 1):
#         if m % i == 0:  
#             if is_prime(i) and is_prime(m // i):
#                 return True
    
#     return False

# n = int(input())
# print(primeproduct(n))
# def delchar(c,s):
#     if len(s)==1:
#         return c.replace(s,"")
        
#     else:
#         return c
# c="banana"
# s="a"
# print(delchar(c,s))
# hacker rank no 10
# def grade(name,n):
#     sum=0
#     len=3
#     if name in student_marks:
#         for i in range(len):
#             sum=sum+student_marks[name][i]
#     average=sum/len
#     # Format to always show 2 decimal places
#     return "{:.2f}".format(average)
        

    
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
# print(grade(query_name,n))
# list comprehension
# def list_comprehension(x, y, z, n):
#     result = [[i, j, k]
#               for i in range(x+1)
#               for j in range(y+1)
#               for k in range(z+1)
#               if i + j + k != n]
#     print(result)

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
# #     z = int(input())
# #     n = int(input())
# #     list_comprehension(x, y, z, n)
# # list opearations
# if __name__ == '__main__':
#     N = int(input())
#     list=[]
#     a=int(input())
#     x=input()
#     match(x):
#     case "insert":
#             list.insert(i,a)
#             break
#     case "append":
#             list.append(a)
#             break
#     case "remove":
#             list.remove(a)
#             break
#     case "pop":
#             list.pop()
#             break
#     case "sort":
#             list.sort()
#             break
#     case "reverse":
#             list.reverse()
#             break
#     case "print":
#             print(list)
#             break
#     case "exit":
#             break
# def str(string):
#     # Check if string has any alphanumeric characters
#     print(any(c.isalnum() for c in string))
    
#     # Check if string has any alphabetical characters
#     print(any(c.isalpha() for c in string))
    
#     # Check if string has any digits
#     print(any(c.isdigit() for c in string))
    
#     # Check if string has any lowercase characters
#     print(any(c.islower() for c in string))
    
# #     # Check if string has any uppercase characters
# #     print(any(c.isupper() for c in string))



# # if __name__ == '__main__':
# #     s = input()
# #     result=str(s)  
# #     print(result)

# import textwrap

# def wrap(string, max_width):
#     wrapped_list = textwrap.wrap(string, max_width)
#     for item in wrapped_list:
#         print(item)
#     return ""

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)


# def mystery(l):
#   l = l[1:]
#   return()

# mylist = [7,11,13]
# print(mystery(mylist))
# startmsg = "python"
# endmsg = ""
# for i in range(1,1+len(startmsg)):
#   endmsg = startmsg[-i] + endmsg
# print(endmsg)
# b = [23,44,87,100]
# a = b[1:]
# d = b[2:]
# c = b
# d[0] = 97
# c[2] = 77
# print(a[1])
# print(b[2])
# print(c[2])
# print(d[0])
# x = ["slithy",[7,10,12],2,"tove",1]  # Statement 1
# # y = x[0:50]                          # Statement 2
# # z = y                                # Statement 3
# # w = x                                # Statement 4
# # x[0] = x[0][:5] + 'ery'              # Statement 5
# # y[2] = 4                             # Statement 6
# # z[4] = 42                            # Statement 7
# # w[0][:3] = 'fea'                     # Statement 8
# # x[1][0] = 5555                       # Statement 9
# print(a = (x[4][1] == 1)) 
# covert to bcd numbers 
# def print_formatted(number):
#     # Calculate the width needed for binary representation
#     width = len(bin(number)[2:])
    
#     for i in range(1, number + 1):
#         # Convert to different bases
#         decimal = str(i)
#         octal = oct(i)[2:]  # Remove '0o' prefix
#         hexadecimal = hex(i)[2:].upper()  # Remove '0x' prefix and make uppercase
#         binary = bin(i)[2:]  # Remove '0b' prefix
        
#         # Format with proper spacing
#         print(f"{decimal:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}")

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)
# progran to find the hash of the tuple
# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split())
#     integer_tuple = tuple(integer_list)
    
#     print(hash(integer_tuple))
# program to find the substrung in the string
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count
            
            
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)