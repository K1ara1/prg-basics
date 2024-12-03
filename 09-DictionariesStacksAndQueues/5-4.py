winter_semester = {
   "math":60,
   "programming":30,
   "history":15
}
total = 0
for count in winter_semester.values():
    total += count
print('The total number of hours in the winter semester is:',total)