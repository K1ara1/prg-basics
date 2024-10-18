questions = [
    "Are you interested in computer science? (y/n): ",
    "Do you like playing computer games? (y/n):",
    "Do you have an Instagram account? (y/n):"
]

answers = []

for question in questions:
    while True:
        response = input(question)
        if response in ['y', 'n']:
            answers.append(response == 'y')
            break
        else:
            print("Invalid input. Please answer 'y' or 'n'.")

print("Survey Results:")
print(f"1. Do you like programming? {'Yes' if answers[0] else 'No'}")
print(f"2. Do you enjoy working in teams? {'Yes' if answers[1] else 'No'}")
print(f"3. Are you interested in learning new technologies? {'Yes' if answers[2] else 'No'}")