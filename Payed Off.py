# Test Case 1:
balance = 420
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
max = balance
min = 0
perm = balance
x = True
while x:
    balance = perm
    payment = round((max + min) / 2,2)
    print(payment,max)
    for i in range(12):
        balance = round((balance - payment) * (1 + (annualInterestRate) / 12),2)
    if balance < 1 and balance > -1:
        x = False
    elif balance < 0:
        max = payment
    else:
        min = payment
print(payment)