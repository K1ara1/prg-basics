all_students = {"Alice", "John", "Sara", "Bob"}
attended_students = {"Alice", "Bob"}

absent_students = set(all_students - attended_students)
print(absent_students)