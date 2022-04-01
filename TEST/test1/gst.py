'''
Q5)a man goes for shopping.he buys 5 products.accept the price of all products
and display the total bill after adding 18% gst  
'''

product1= int(input("enter price= "))
product2= int(input("enter price= "))
product3= int(input("enter price= "))
product4= int(input("enter price= "))
product5= int(input("enter price= "))


total = product1 + product2 + product3 + product4 + product5

gst =total*0.18

total_bill= total + gst

print("total bill= ",total_bill)
    