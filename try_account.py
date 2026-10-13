from account import Account
acc = Account("Ada")
print(acc.balance) # 0
acc.deposit(100)
acc.withdraw(30)
print(acc.balance) # 70
print(acc) # Ada: £70.00
for bad in [lambda: acc.deposit(-5), lambda: acc.deposit(0), lambda: acc.withdraw(500)]:
    try:
        bad()
    except ValueError as e:
        print("Rejected:", e)
print(acc.balance) # still 70: failed actions change nothing
bo = Account("Bo", 50)
print(bo.balance, acc.balance) # separate objects, separate balances