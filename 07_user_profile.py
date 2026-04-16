#Day 7: Creating a user profile for a banking application
#user profile dictionary to store user information
user_profile = {
    'username' : 'Marvellous Sawyerr',
    'account_number' : '2428835190',
    'account_balance' : 153000.00,
    'currency' : 'USD',
    'is_active' : True
}
#pulling user data to determine account status
print(f'Checking account status for {user_profile["username"]}...')
print(f'Account status: {"Active" if user_profile["is_active"] else "Inactive"}')
#simulate deposit transaction
deposit_amount = 5450.00
user_profile['account_balance'] += deposit_amount
print(f'\nDeposit of ${deposit_amount:,.2f} successful!')
print(f'Updated balance: ${user_profile['account_balance']:,.2f} {user_profile['currency']}')
#account type assignment
user_profile['account_type'] = 'Premium Investment'
#summary of user profile details with masked account number
masked_account = '****' + user_profile['account_number'][-4:]
print('\n----USER PROFILE OVERVIEW----')
print(f'Username: {user_profile["username"]}')
print(f'Account number: {masked_account}')
print(f'Total balance: ${user_profile["account_balance"]:,.2f} {user_profile["currency"]}')
print(f'Account type: {user_profile["account_type"]}')
print('-----------------------------')
#dictonary overview
print('\nComplete user profile data:')
for x, y in user_profile.items():
    print(f'{x}: {y}')
