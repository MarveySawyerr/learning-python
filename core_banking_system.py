#Final stage: Creating the core banking system
#This is the final stage of our banking application, where we will integrate all the functions and features we have developed in the previous stages.

#Sample database of users and account information
user = {
    'username': 'Marvellous',
    'account_number': '1122334455',
    'balance': 50000.00,
    'history': ['Initial deposit: $50,000.00'] # type: ignore
}

#------The Engines for the banking system------
def get_masked_account(account_no):
    return '****' + account_no[-4:]

def deposit(balance, amount):
    balance += amount
    return balance

def withdraw(balance, amount):
    if amount > balance:
        print('\nTransaction Declined: Insufficient funds.')
        return balance
    else:
        balance -= amount
        print('Transaction successful!')
        return balance
    
def display_balance(balance):
    print(f'\nYour current balance is: ${balance:,.2f}')

def display_transaction_history(history):
    print('\nTransaction History:')
    for transaction in history:
        print(f'- {transaction}')

def get_secure_float(prompt):
    """Bulletproof number input handling using Try/Except"""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("[ERROR]: Amount must be greater than zero.")
        except ValueError:
            print("\n[SECURITY ERROR]: Invalid input! Numbers only (e.g., 100.50).\n")

#------The User Interface------
print('\n==========================================')
print('    WELCOME TO THE CORE BANKING SYSTEM    ')
print('==========================================')

#validating account number format
while True:
    account_no = input("\nEnter account number (10 digits) or 'exit' to quit: ")
    if account_no.lower() == 'exit':
        print('Exiting the system.')
        break

    # account number validation
    if not account_no.isdigit() or len(account_no) != 10:
        print('Invalid account number format. Please enter a 10-digit number.')
        continue

    # account lookup (single-user demo)
    if account_no == user['account_number']:
        print('\nLogin successful!')
        print(f'Welcome back, {user["username"].upper()}!')

        # Inner account menu for logged-in user
        while True:
            print(f'Account number: {get_masked_account(user["account_number"]) }')
            print('\nPlease select a transaction type:')
            print('1. Deposit')
            print('2. Withdrawal')
            print('3. View Balance')
            print('4. View Transaction History')
            print('5. Logout')

            choice = input('Enter choice (1-5): ').strip()

            if choice == '1':
                amount = get_secure_float('\nEnter deposit amount: ')
                user['balance'] = deposit(user['balance'], amount)
                user['history'].append(f'Deposit: ${amount:,.2f}')
                print('Deposit completed.')
                display_balance(user['balance'])

            elif choice == '2':
                amount = get_secure_float('\nEnter withdrawal amount: ')
                old_balance = user['balance']
                user['balance'] = withdraw(user['balance'], amount)
                if user['balance'] != old_balance:
                    user['history'].append(f'Withdrawal: -${amount:,.2f}')

            elif choice == '3':
                display_balance(user['balance'])

            elif choice == '4':
                display_transaction_history(user['history'])

            elif choice == '5':
                print('\nLogging out...')
                break

            else:
                print('Invalid selection. Please choose a number 1-5.')

    else:
        print('Account not found. Please try again.')