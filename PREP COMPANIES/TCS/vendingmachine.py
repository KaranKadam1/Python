'''

Problem Statement

FULLY AUTOMATIC VENDING MACHINE – dispenses your cuppa on just press of button.
A vending machine can serve range of products as follows:

Coffee
Espresso Coffee
Cappuccino Coffee
Latte Coffee

Tea=
Plain Tea
Assam Tea
Ginger Tea
Cardamom Tea
Masala Tea
Lemon Tea
Green Tea
Organic Darjeeling Tea

Soups =
Hot and Sour Soup
Veg Corn Soup
Tomato Soup
Spicy Tomato Soup

Beverages=
Hot Chocolate Drink
Badam Drink
Badam-Pista Drink
Write a program to take input for main menu & sub menu and display the name of sub menu selected in the following format (enter the first letter to select main menu):

Welcome to CCD 

Enjoy your

Example 1:

Input:
c
1
Output
Welcome to CCD!
Enjoy your Espresso Coffee!
Example 2:

Input
t
9
Output
INVALID OUTPUT!

'''

coffee = ['Espresso Coffee','Cappuucino Coffee','Latte Coffee'] 
tea = ['Plain Tea', 'Assam Tea','Ginger Tea','Cardamom Tea','Masala Tea','Lemon Tea','Green Tea','Organic Darjeeling Tea']
soup = ['Hot and Sour Soup','Veg Corn Soup','Tomato Soup','Spicy Tomato Soup']
drink = ['Hot Chocolate Drink', 'Badam Drink','Badam-Pista Drink']

menu = input()
item_number = int(input())

if menu == "c":
    if item_number <= len(coffee):
        print("Welcome to CCD!")
        print("Enjoy your "+coffee[item_number-1])
    else:
        print("INVALID INPUT")
elif menu == "t":
    if item_number <= len(tea):
        print("Welcome to CCD!")
        print("Enjoy your "+tea[item_number-1])
    else:
        print("INVALID INPUT")
elif menu == "s":
    if item_number <= len(soup):
        print("Welcome to CCD!")
        print("Enjoy your "+soup[item_number-1])
    else:
        print("INVALID INPUT")
elif menu == "d":
    if item_number <= len(drink):
        print("Welcome to CCD!")
        print("Enjoy your "+drink[item_number-1])
    else:
        print("INVALID INPUT")
else:
    print("INVALID INPUT")
