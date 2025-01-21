 # we trying to get input from  a user of a menu continously and
 # showing the price of each item one by one if it is exist in dict(menu)
# until the User Press the "Control d "
# # how we can input and process "Control d" by using EOFError in our except block
# at the end we will give back the total the cosr or price of these items of the menu


# In this section define the dictonary of the items
Menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
Total=0

    # In this section we looping again and again to get input as many time's as user wanted
while True:
        # we trying  to get input
        try:
            User=input("Enter :").title()
            if User in Menu:
                Total += Menu[User]
                print("Total: $",end="")
                print("{:.2f}".format(Total))
        # if we having the EOFError then user had input the something's like 'ctrl d' etc
        except EOFError:
           print()
           break



