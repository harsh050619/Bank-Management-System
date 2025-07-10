import time
print('please enter your card')
time.sleep(5)
password=1234
pin=int(input('enter your pin:'))
balance=5000
if pin==password:
    while True:
        print('''
          1==balance
          2==withdraw amount
          3==deposite balance
          4==exit''')
        try:
            option=int(input('please enter your choise'))
        except:
            print('enter valid value')
        if option==1:
            print(f'your current balance is {balance}')
        if option==2:
            withdrawl_amount=int(input('please enter withdrawl_amount'))
            balance=balance-withdrawl_amount
            print(f'{withdrawl_amount} has been debited from your account')
            print(f'your current balance is {balance}')
        if option==3:
            deposite_amount=int(input('please enter your amount'))
            balance=balance+deposite_amount
            print(f'{deposite_amount} has been deposited to your account')
            print(f'your current balance is {balance}')
        if option==4:
            break
else:
    print('wrong pin please try again')
