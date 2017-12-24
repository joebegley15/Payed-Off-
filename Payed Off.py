def payedOff(balance, timePeriod, iRte):
    max = balance
    min = 0
    balanceReset = balance
    payment = round((max + min) / 2, 2)
    conditional = True
    while conditional:
        balance = balanceReset
        payment = round((max + min) / 2, 2)
        for i in range(timePeriod):
            balance = round((balance - payment) * (1 + (iRte) / 12),2)
        if balance > -1 and balance < 0:
            conditional = False
        elif balance < 0:
            max = payment
        else: 
            min = payment
    return payment