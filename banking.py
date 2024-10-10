
class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, account_number, holder_name, initial_balance=0.0):
        if account_number in self.accounts:
            return False  # Account already exists
        else:
            self.accounts[account_number] = {
                "holder_name": holder_name,
                "balance": initial_balance
            }
            return True  # Account successfully opened

    def check_account_details(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account
        else:
            return None  # Account does not exist

    def get_account_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account["balance"]
        else:
            return None  # Account does not exist


def main():
    bank = Bank()

    while True:
        print("\nOptions:")
        print("1. Open New Account")
        print("2. Check Account Details")
        print("3. Exit")
        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            account_number = input("Enter Account Number: ")
            holder_name = input("Enter Holder Name: ")
            initial_balance = float(input("Enter Initial Balance: "))

            if bank.open_account(account_number, holder_name, initial_balance):
                print(f"Account {account_number} opened successfully!")
            else:
                print(f"Account {account_number} already exists!")

        elif choice == '2':
            account_number = input("Enter Account Number to check: ")
            account = bank.check_account_details(account_number)
            if account:
                print("\nAccount Details:")
                print(f"Account Number: {account_number}")
                print(f"Holder Name: {account['holder_name']}")
                print(f"Balance: ${account['balance']}")
            else:
                print(f"Account {account_number} does not exist.")

        elif choice == '3':
            print("Thank you for using the Bank Account System.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()



