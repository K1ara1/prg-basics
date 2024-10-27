def f(detector):
    current_count = 0 
    max_count = 0 
    
    for action in detector:
        if action == '+':
            current_count += 1 
        elif action == '-':
            current_count -= 1 
        
    if current_count > max_count:
            max_count = current_count
            
    return max_count >= 3

people = (input('If people enter press + else press -: '))
print(f(people))