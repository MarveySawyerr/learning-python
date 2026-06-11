#Day 9: Building a secure bannking function that incorportates try and except blocks.
while True:
    try:
        account_number = input('Enter your account number: ')
        if not account_number.isdigit() or len(account_number) != 10:
            raise ValueError('Invalid account number. Please enter a 10-digit number.')
        deposit_amount = float(input('Enter deposit amount: '))
        if deposit_amount > 0:
            print(f'Success! Deposited ${deposit_amount:,.2f} to account {account_number}.')
        else:
            print('Deposit amount must be greater than zero. Try again.')
        break
    except ValueError as e:
        print(e)
        print('INVALID INPUT. Please try again.')