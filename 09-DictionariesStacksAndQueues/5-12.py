def f(text):
    stack = []
    reversed_text = ''
    for char in text:
        stack.append(char)
    for _ in range(len(stack)):
        reversed_text += stack.pop()
    return reversed_text

if __name__ == "__main__":
    print(f('klara'))

