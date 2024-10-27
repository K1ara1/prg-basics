def f(dice):
    if not dice:
        return 0  
    
    max_streak = 1
    current_streak = 1
    
    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            current_streak += 1
        else:
            max_streak = max(max_streak, current_streak) 
            current_streak = 1
    
    max_streak = max(max_streak, current_streak)
    
    return max_streak

result = input('Enter dice scores: ')
print(f(result))