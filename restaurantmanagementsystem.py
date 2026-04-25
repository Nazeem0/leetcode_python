# define the mnu of the restaurantusing dictionary
menu={
    "pizza":50,
    "pasta":80,
    "burger":90,
    "salad":70,
    "coffee":80,
}
print("Welcome to the restaurant ")
print("pizza:50\npasta:80\nburger:90\nsalad:70\ncoffe:80")

# get the user's choice 
order_total=0
# all the total will be addeed to order token
item_1=input("enter the name of the item you want to order\n")
if item_1 in menu:
    order_total+=menu[item_1]
    print("Your item has been added to your order ")
else:
    print(f"Ordered item {item_1}is not available yet\n  ")
# create another variable
another_order=input("Do you want to add another item ?(Yes/No)\n")
if another_order=="Yes":
    item_2=input("Enter the name of the second item\n ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"item {item_2} has been added to order\n")
    else:
        print(f"Ordered item{item_2} is not available\n")
print(f"the total amount of item to pay is  {order_total}")  
     


