print('welcome to jio center bangalore...')

import time

def customerservice():
    print('connecting to customer care please be on line..')
    time.sleep(2)
    print("connected to customer service\nhow may i help you")

def prepaid():
    print('connecting to prepaid  care please be on line..')
    time.sleep(2)
    print("connected to prepaid service\nhow may i help you")

def recharge():
    print("199 rs for 28 days")
    print("2199 rs for 328 days")
    print("5000 rs for 520 days")

def balance():
    print('Balance is 150rs....')


def exitpoll():
    print('good bye have a nice day')
def jio():
    print('........')
    time.sleep(0.5)
    print('Calling')
    time.sleep(0.5)
    print('........')
    time.sleep(0.5)
    print('Connecting')
    time.sleep(0.5)
    print('Hello sir how may i help you?')
    print('Select the options..')
    print('1 : customer service')
    print('2 : pre-paid service')
    print('3 : recharge')
    print('4 : check balance')
    print('5 : exit')
    n=int(input('Select the option: \n'))
    if(n>0 and n<=5):
        if n==1:
            customerservice()
        elif n==2:
            prepaid()
        elif n==3:
            recharge()
        elif n==4:
            balance()
        else:
            exitpoll()
    else:
        print('select an correct option')
        jio()

jio()