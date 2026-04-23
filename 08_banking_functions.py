#Day 8: Creating a banking funcion with Functions(no pun intended.)
#The engine for a banking application with functions to process deposits, withdrawals, and mask account numbers
def get_masked_account(account_no):
    return '****' + account_no[-4:]
def process_deposit(balance, amount):
    balance += amount
    return balance
def process_withdrawal(balance, amount):
    if amount > balance:
        print('Transaction Decline: Insufficient funds.')
        return balance
    else:
        balance -= amount
        print('Transaction successful!')
        return balance
account_number = '4845792797'
masked_account = get_masked_account(str(account_number))

# User information and welcome message
print('Welcome back, Marvellous!')
current_balance = 34050.00
print(f'Your current balance is ${current_balance:,.2f}')
print(f'Account Number: {masked_account}')

while True:
    print('\nPlease select a transaction type:')
    print('1. Deposit')
    print('2. Withdrawal')
    print('3. Exit')
    choice = input('Enter your choice (1, 2, or 3): ')

    if choice == '1':
        deposit_amount = float(input('Enter deposit amount: '))
        current_balance = process_deposit(current_balance, deposit_amount)
        print(f'NEW BALANCE: ${current_balance:,.2f}')
    elif choice == '2':
        withdrawal_amount = float(input('Enter withdrawal amount: '))
        current_balance = process_withdrawal(current_balance, withdrawal_amount)
        print(f'NEW BALANCE: ${current_balance:,.2f}')
    elif choice == '3':
        print('SESSION TERMINATED.')
        break
    else:
        print('Invalid choice. Please enter 1, 2, or 3.')

