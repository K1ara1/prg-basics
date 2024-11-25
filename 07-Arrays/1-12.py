categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_expenses = expenses.index(max(expenses))
max_categories = categories[max_expenses]

print(max_categories)