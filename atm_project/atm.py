class ATM:
    def __init__(self):
        self.name = "Pentagon ATM"
        self.balance = 10000
        self.pin = 1234
atm = ATM()
print("Welcome to Pentagon ATM")
card = input("Insert your card (1.Yes / 2.No): ")
if card == "1":
    print("Select your Language: 1.English 2.Kannada 3.Hindi")

    # Select language
    language = input("Select 1 for English,2 for Kannada,3 for Hindi: ")
    if language == "1":
        print("You Selected: English")
    elif language == "2":
        print("You Selected: Kannada")
    elif language == "3":
        print("You Selected: Hindi")

    # PIN section
    pin=int(input("Enter your PIN: "))
    if pin == atm.pin:
        # Transaction
        money = input("Press 1 for Balance Enquiry, 2 for Withdrawal:")
        if money == "1":
            print("Current balance:", atm.balance)
        elif money == "2":
            amount = int(input("Enter your amount to withdraw:"))

            if amount <= 0:
                print("Please enter a valid amount.")
            elif amount > atm.balance:
                print("Insufficient balance.")
            else:
                atm.balance = atm.balance - amount
                
                print("Please collect your case:", amount)
                print("Current balance:", atm.balance)

        else:
            print("Invalid transaction.")
    else:
        print("Wrong PIN!")
else:
    print("Please insert your card.")