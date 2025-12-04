import sys
if len(sys.argv)==3:
    tuition_fees=float(sys.argv[1])
    paid_amount=float(sys.argv[2])
else:
    tuition_fees=2000.0
    paid_amount=2000.0
total=tuition_fees+paid_amount
print("Tuition_Fees:",tuition_fees)
print("Paid_amount:",paid_amount)
print("Total_fees:",total)
