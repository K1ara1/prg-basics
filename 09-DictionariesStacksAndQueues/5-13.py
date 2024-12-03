def f(RPN):
    stack = []
    splitted = RPN.split()
    for value in splitted:
        if value.isdigit():
            stack.append(int(value))
        elif value == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif value == '-':
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif value == '*':
            b = stack.pop()
            a == stack.pop()
            stack.append(a*b)
        elif value == '/':
            b = stack.pop()
            a == stack.pop()
            stack.append(a/b)
    return stack[0]

if __name__ == "__main__":
    print(f('2 4 1 + *'))  
    print(f("2 3 + 4 5 + * "))  
    print(f("8 3 1 + / 3 2 - 4 + *")) 

