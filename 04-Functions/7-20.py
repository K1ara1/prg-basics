def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(n):
    count = 0  
    current = 1  
    nth_prime = None  
    
    while count < n:
        current += 1  
        if is_prime(current):
            count += 1 
            nth_prime = current  
    
    return nth_prime

if __name__ == '__main__':
    print(f(5))