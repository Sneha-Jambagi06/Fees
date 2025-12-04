import sys
if len(sys.argv)==3:
    tuition_fees=float(sys.argv[1])
    paid_amount=float(sys.argv[2])
    balance=float(sys.argv[3])
else:
    tuition_fees=2000.0
    paid_amount=2000.0
    balance=2000.0
total=balance+paid_amount
print("Tuition_Fees:",tuition_fees)
print("Paid_amount:",paid_amount)
print("Balance:",balance)
print("Total_fees:",total)