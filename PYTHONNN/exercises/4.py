import time

items=[]
totalAmount=[]
qtyAmount=0
def Dosa(item,price):
    qty=int(input('enter the qty between 1 to 3:\n'))
    if(qty>0 and qty <=3):
        qtyAmount=qty*price
        items.append(item)
        totalAmount.append(qtyAmount)
        print("Added to Cart",item)
        time.sleep(2)
        Swiggy()
    else:
        print('add proper Quantity')
        Swiggy()
   

def Burger(item,price):
    items.append(item)
    totalAmount.append(price)
    print("Added to Cart",item)
    time.sleep(2)
    Swiggy()

def Pizza(item,price):
    items.append(item)
    totalAmount.append(price)
    print("Added to Cart",item)
    time.sleep(2)
    Swiggy()

def Chicken(item,price):
    items.append(item)
    totalAmount.append(price)
    print("Added to Cart",item)
    time.sleep(2)
    Swiggy()

def PlaceOrder():
    print("Your Order is Placed:")
    print("Ordered Items are:")
    for i in items:
        print(i)
    print("Total Amount to be Paid : ",sum(totalAmount))
   
def Swiggy():
    print("Select the Items Menu:")
    print("1. Dosa")
    print("2. Burger")
    print("3. Pizza")
    print("4. Chicken")
    print("5. Place Final Order")
    n=int(input("Select the Number: "))
    if(n>0 and n<=5):
        if(n==1):
            Dosa("Dosa",50)        
        elif(n==2):
            Burger("Burger",150)
        elif(n==3):
            Pizza("Pizza",250)
        elif(n==4):
            Chicken("Chicken",350)
        elif(n==5):
            PlaceOrder()
        else:
            pass
    else:
        print('give the valid input')


print("Welcome to Swiggy")
Swiggy()