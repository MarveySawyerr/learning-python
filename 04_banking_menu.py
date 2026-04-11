#Day 4: The main menu engine for a banking application
print('Welcome back, Marvellous!')
current_balance = 34050.00
while True:
    print ('1. Check Balance')
    print ('2. Deposit')
    print ('3. Withdraw')
    print ('4. Exit')
    #User input for menu selection
    user_choice = input('Please select an option: ')
    #Process user choice and perform corresponding action
    if user_choice == '1': #Check balance
        print(f'Your current balance is ${current_balance:,.2f}')
    elif user_choice == '2': #Deposit
        deposit_amount = float(input('Enter deposit amount: '))
        current_balance += deposit_amount
        print(f'Transaction complete. New balance: ${current_balance:.2f}')
    elif user_choice == '3': #Withdraw
        withdrawal_amount = float(input('Enter withdrawal amount: '))
        if withdrawal_amount > current_balance:
            print('Transaction Decline: Insufficient funds.')
            print(f'Current balance is ${current_balance:,.2f}')
            continue
        else:
            current_balance -= withdrawal_amount
            print('Transaction successful!')
            print(f'New balance: ${current_balance:.2f}')
    elif user_choice == '4': #Exit
        print('Thank you for banking with us. Goodbye!')
        break