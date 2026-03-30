def display_main_menu():

    print("\nATM Main Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    try:
        choice = int(input("Please choose an option (1-4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please try again.")
            return None
        return choice
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        return None


def deposit(balance):

    try:
        amount = float(input("Enter the amount to deposit: $"))
        if amount <= 0:
            print("Deposit amount must be positive.")
            return balance
        balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${balance:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
    return balance


def withdraw(balance):

    try:
        amount = float(input("Enter the amount to withdraw: $"))
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return balance
        if amount > balance:
            print("Insufficient balance.")
            return balance
        balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
    return balance


def check_balance(balance):
    
    print(f"Your current balance is: ${balance:.2f}")
    return balance
def main():
    balance = 0.0

    while True:
        choice = display_main_menu()
        if choice is None:
            continue
        if choice == 1:
            balance = deposit(balance)
        elif choice == 2:
            balance = withdraw(balance)
        elif choice == 3:
            check_balance(balance)
        elif choice == 4:
            print("Thank you for Using ATM.")
            break

main()