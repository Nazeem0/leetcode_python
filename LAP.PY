def is_leap(year):
    if(year%400==0):
        return True
    elif(year%100==0):
        return False
    elif(year%4==0):
        return 
    else:
       return False
        

    


year = int(input())
print(is_leap(year))