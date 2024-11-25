def f(dice):
    count = 1
    max_count = 1
    max_digit = dice[0]  
    
    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_digit = dice[i - 1]
            count = 1  
    
    if count > max_count:
        max_digit = dice[-1]

    return int(max_digit)

if __name__ == '__main__':
    print(f('21337777'))