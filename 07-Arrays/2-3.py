monthly_expenses = [
   [200, 50, 100], 
   [180, 60, 110],  
   [220, 55, 105],  
   [210, 65, 95]    
]

category_totals = [0, 0, 0]
week_totals = []
total_expenses = 0

for week in monthly_expenses:
    week_total = 0
    for i, expense in enumerate(week):
        category_totals[i] += expense
        week_total += expense
    week_totals.append(week_total)
    total_expenses += week_total

print('MONTHLY EXPENSES')
print('----------------')
print('Food:', category_totals[0])
print('Transport:',category_totals[1])
print('Utilities:',category_totals[2])
print('Week 1:',week_totals[0])
print('Week 2:',week_totals[1])
print('Week 3:',week_totals[2])
print('Week 4:',week_totals[3])
print('---------------')
print('TOTAL:',total_expenses)