test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

question_number = len(test_results)

correct_answer = 0
for answer in test_results:
   if answer == True:
      correct_answer += 1

incorrect_answer = 0
for answer in test_results:
   if answer == False:
      incorrect_answer += 1

percent = (correct_answer*100)/question_number

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answer)
print('Number of incorrect answers:', incorrect_answer)
print('Percent of correct answers:', percent)