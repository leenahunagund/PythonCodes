import random

account=0
lottery=random.randint(1,10)
while(1):
    bet=int(input("your bet from 1-10: "))
    if bet==lottery:
        account=account+900-100
    else:
        account=account-100
    print(account)
    
'''import random

account=0
lottery=random.randint(1,10)
for i in range(7):
    bet=random.randint(1,10)
    print("bet=", bet)
    if bet==lottery:
        account=account+900-100
    else:
        account=account-100
    print(account)
print("lottery number: ",lottery)''''
