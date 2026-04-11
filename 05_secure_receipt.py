#Day 5: Creating a secure receipt that hides customer account number
name = input('Enter your name: ').strip().title()
print(f'Welcome back, {name}!')
current_balance = 34050.00
#logic for preventing entering more or less than 10 digits
while True:
    account_number = input('Enter 10 digit number: ')
    if len(account_number) != 10 or not account_number.isdigit():
        print('Invalid account number. Try again.')
    else:
        break
#account number is masked
masked_account = ('****' + account_number[-4:])
#receipt details
print('-' * 30)
print(f'CUSTOMER NAME: {name}')
print(f'ACCOUNT NUMBER: {masked_account}')
print(f'BALANCE: {current_balance:,.2f}')
print('\nThank you for banking with us!')
print('-' * 30)
