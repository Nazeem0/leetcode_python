list=[
    "cristiano Ronaldo",
    "michael jordan",
    "virat kholi"
    
]
total_money=0
football=input("name the most famous football player in the world ?")
if football==list[0]:
    print("correct")
    total_money=total_money+1000
    print("total money:", total_money)
basketball=input("name the most famous basketball player in the world ?")
if basketball==list[1]:
    print("correct")
    total_money=total_money+1000
    print("total money:", total_money)
cricket=input("name the most famous cricket  player in the world ?")
if cricket==list[2]:
    print("correct")
    total_money=total_money+1000
    print("total money:", total_money)
    
print(f"the overall total money he is going to take to home is {total_money}")
