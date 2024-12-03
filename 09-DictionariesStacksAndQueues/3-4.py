def f(number):

    stack = []
    while number > 0:
        remainder = number % 2  
        stack.append(remainder) 
        number //= 2 
    
    binary_number = ""
    for _ in range(len(stack)):
        binary_number += str(stack.pop()) 
    return binary_number

if __name__ == "__main__":
    print(f(18))
