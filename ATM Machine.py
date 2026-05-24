balance = 50000
pin = "7860"

entered_pin = input("Enter ATM PIN: ")

if entered_pin == pin:

    while True:

        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current Balance:", balance)

        elif choice == "2":
            amount = int(input("Enter amount to deposit: "))
            
            if amount > 0:
                balance = balance + amount
                print("Amount Deposited Successfully")
                print("Updated Balance:", balance)
            else:
                print("Invalid Amount")

        elif choice == "3":
            amount = int(input("Enter amount to withdraw: "))

            if amount <= balance:
                balance = balance - amount
                print("Please collect your cash")
                print("Remaining Balance:", balance)
            else:
                print("Insufficient Balance")

        elif choice == "4":
            print("Thank You for using ATM")
            break

        else:
            print("Invalid Choice")

else:
    print("Incorrect PIN")