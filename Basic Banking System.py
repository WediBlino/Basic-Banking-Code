acc = ["jonathan", "jeremy", "jenny", "james", "jonny"]
balance = [34, 4523, 1000000, 5, 134]
name = input("What is your name: ").lower()
present = False

def home():
  print("Simple Banking System\n1. Create an Account\n2. Deposit Money\n3. Withdraw Money\n4. Check Balance\n5. Exit")
  action = (input("Account Initialised... What would you like to do?(Enter Number 1-5) "))
  while int(action) < 1 or int(action) > 5 or action.isdigit() == False:
    action = (input("Account Initialised... What would you like to do?(Enter Number 1-5) "))
  return int(action)

def deposit():
  for i in range(len(acc)):
    if name == acc[i]:
      amt = int(input("How much would you like to deposit? "))
      balance[i] += amt
      print(f"${amt} deposited into account.")

def check():
  for i in range(len(acc)):
    if name == acc[i]:
      print(f"This is your balance: {balance[i]}")

def withdrawl():
  for i in range(len(acc)):
    if name == acc[i]:
      amt = int(input("How much would you like to withdraw? "))
      while amt > balance[i]:
        amt = int(input("Not Enough Remaining Balance, Please Input A Valid Amount: "))
      balance[i] -= amt
      print(f"${amt} withdrawn from account.")

def create(acc_name):
  acc.append(acc_name)
  balance.append(0)
  print(f"Welcome {name}!")

def cont():
  x = input("Would you like to continue? (Y/N) ").lower()
  while x != "y" and x != "n":
    x = input("Input Invalid, Please Answer With Either 'Y' or 'N' ").lower()
  if x == "y":
    return True
  elif x == "n":
    return False

action = 0
for i in range(len(acc)):
    if name == acc[i]:
      present = True
      while action!= 5:
        action = home()
        if action == 1:
          create(name)
          if cont() == False:
            break
        elif action == 2:
          deposit()
          print(f"This is your balance: {balance[i]}")
          if cont() == False:
            break
        elif action == 3:
          withdrawl()
          print(f"This is your balance: {balance[i]}")
          if cont() == False:
            break
        elif action ==4:
          check()
          if cont() == False:
            break
        elif action ==5:
          break
        else:
          action = int(input("Please input a valid action, 1-5"))

if present == False:
  y = input("You need to make a new account to continue. (Y/N) ").lower()
  if y == "y":
    create(name)
    if cont() == True:
      for i in range(len(acc)):
        if name == acc[i]:
          while action!= 5:
            action = home()
            if action == 1:
              create(name)
              if cont() == False:
                break
            elif action == 2:
              deposit()
              print(f"This is your balance: {balance[i]}")
              if cont() == False:
                break
            elif action == 3:
              withdrawl()
              print(f"This is your balance: {balance[i]}")
              if cont() == False:
                break
            elif action ==4:
              check()
              if cont() == False:
                break
            elif action ==5:
              break
          else:
            action = int(input("Please input a valid action, 1-5"))