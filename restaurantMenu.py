order = input("Enter your order: ")
wants_cheese = input("Do you want cheese: ")
wants_extra_toppings= input("Do you want any toppings: ")

if order == "burger":
    if wants_cheese=="yes":
        print("Cheeseburger added to order.")
    else:
        print("Regular burger added to order.")
elif order == "pizza":
    if wants_extra_toppings=="yes":
        print("Pizza with extra toppings.")
    else:
        print("Plain pizza.")
elif order == "Rice bowl":
    print("Rice bowl ordered")
    
