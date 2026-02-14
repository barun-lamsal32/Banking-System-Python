import time      # Used for delay (sleep)
import os        # Used to clear screen

# Dictionary to store all users' data
# Nested Dictionary
# Structure:
# accounts = {
#     "username": {
#         "password": "...",
#         "balance": amount,
#         "pins": pin_number
#     }
# }
accounts = {}

# ---------------- REGISTER CLASS ----------------
class Register:

    # Function to create a new account
    def account(self):

        # Take username input
        un = input("Create username: ")

        # Check if username already exists
        if un in accounts:
            print("Username already exists!\n")
            time.sleep(1)
            return   # Stop function if username exists

        # Take password and pin
        pw = input("Create password: ")
        pn = int(input("Create 4-digit pin: "))

        # Store user details inside accounts dictionary
        accounts[un] = {
            "password": pw,
            "balance": 0,   # Default balance is 0
            "pins": pn
        }

        


# ---------------- LOGIN CLASS ----------------
# Inherits Register class (not necessary but okay for learning)
class Login(Register):

    # -------- Deposit Money --------
    def deposit(self, usrname):

        self.usrname = usrname
        pinned = int(input("Enter 4-digit pin: "))

        # Verify username and pin
        if self.usrname in accounts and accounts[self.usrname]["pins"] == pinned:

            amt = int(input("Enter amount to deposit: "))

            # Add amount to user's balance
            accounts[self.usrname]["balance"] += amt

            print("Deposited successful ! ! ! !\n")

        else:
            print("Invalid pin ! ! ! !\n")
            return


    # -------- Withdraw Money --------
    def withdraw(self, usname):

        self.usname = usname
        pinn = int(input("Enter 4-digit pin: "))

        # Verify username and pin
        if self.usname in accounts and accounts[self.usname]["pins"] == pinn:

            amts = int(input("Enter amount to withdraw: "))

            # Check if sufficient balance exists
            if amts <= accounts[self.usname]["balance"]:

                # Subtract amount from balance
                accounts[self.usname]["balance"] -= amts
                print("Withdraw successful ! ! ! !\n")

            else:
                print("Insufficient amount ! ! ! !\n")

        else:
            print("Invalid pin\n")
            return


    # -------- View Balance --------
    def viewbalance(self, uname):

        self.uname = uname
        pns = int(input("Enter 4-digit pin: "))

        # Verify username and pin
        if self.uname in accounts and accounts[self.uname]["pins"] == pns:

            # Display current balance
            print(f"Your current bank balance is: {accounts[self.uname]['balance']}\n")

        else:
            print("Invalid pin ! ! ! !\n")


# Create objects
o1 = Register()
o2 = Login()


# ---------------- MAIN PROGRAM LOOP ----------------
while True:

    print("\n------Welcome to Bank Management System------\n")
    print("1) Register\n2) Login\n3) Exit")

    num = int(input("Enter Your choice: "))

    # -------- Register Option --------
    if num == 1:

        o1.account()   # Call register function
        print("Registered Succesfull ! ! ! !\n")
        time.sleep(2)

    # -------- Login Option --------
    elif num == 2:

        usernames = input("Enter a username: ")
        passwords = input("Enter a password: ")

        # Check if username and password match
        if usernames in accounts and accounts[usernames]["password"] == passwords:

            # After successful login → show bank menu
            while True:

                os.system('cls')   # Clear screen (Windows only)

                print("\n --------Bank Menu--------\n")
                print("1) Deposit\n2) Withdraw\n3) View Balance\n4) Exit")

                numm = int(input("Enter your choice: "))

                if numm == 1:
                    o2.deposit(usernames)
                    time.sleep(3)

                elif numm == 2:
                    o2.withdraw(usernames)
                    time.sleep(3)

                elif numm == 3:
                    o2.viewbalance(usernames)
                    time.sleep(4)

                else:
                    break   # Exit bank menu and go back to main menu

        else:
            print("Invalid username or password ! ! ! !")
            time.sleep(2)

    # -------- Exit Program --------
    else:
        print("------Thank You ! ! ! !------")
        exit()   # Stop entire program
