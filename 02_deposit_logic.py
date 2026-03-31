#Day 2: Creating a deposit logic for a bank account
print('Welcome User')
opening_balance = 35399.59
print('Your current balance is $', opening_balance)
#User inputs deposit
deposit = input('How much would you like to deposit? ')
new_balance = float(opening_balance) + float(deposit)
print('Transaction complete. New balance: $', float(new_balance))
