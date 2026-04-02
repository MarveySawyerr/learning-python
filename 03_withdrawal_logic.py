#Day 3: Creating a withdrawal logic for a bank account
print('Welcome back, Marvellous!')
current_balance = 34050.00
print(f'Your current balance is ${current_balance:.2f}')
#User input withdrawal amount
withdrawal_amount = float(input('Enter withdrawal amount: '))
if withdrawal_amount > current_balance:
    print('Transaction Decline: Insufficient funds.')
    print(f'Current balance is {current_balance:.2f}')
else:
    current_balance -= withdrawal_amount
    print('Transaction succesful!')
    print(f'New balance: ${current_balance:.2f}')
