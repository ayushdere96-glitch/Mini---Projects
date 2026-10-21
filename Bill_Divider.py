Bill = float(input('Enter Bill Amount :'))
People = int(input('Number Of People :'))
tip = float(input('Tip Percentage :'))
tip_amount = Bill*tip/100
Total = Bill+tip_amount
share = Total/People
print('\n BILL SUMMARY')
print(f'Toatl : {Total:.2f}')
print(f'Each Person Pays : {share:.2f}')
