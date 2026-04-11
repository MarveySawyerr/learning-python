#Day 6: Creating a transaction history logic for a banking application
transaction_history = []
print('----Welcome to your transaction history!----')
for i in range(5):
    amount = float(input(f'Enter amount for transaction {i + 1}: '))
    transaction_history.append(amount)
    print(f'Recorded: ${amount:,.2f}')
print('*' * 6)
print('=' * 30)
print('     OFFICIAL STATEMENT     ')
print('=' * 30)
print(f'TOTAL TRANSACTIONS: {len(transaction_history)}')
print(f'TRANSACTION HISTORY:')
for tx in transaction_history:
    print(f' - ${tx:,.2f}')
print(f'TOTAL AMOUNT: ${sum(transaction_history):,.2f}')
print(f'MOST RECENT: ${transaction_history[-1]:,.2f}')
print('=' * 30)
print('*' * 6)
