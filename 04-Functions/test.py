def f(detector):
    current = 0
    count = 0
    for action in detector:
        if action == '+':
            current += 1
            if current > count:
                count = max(count, current)
        elif action == '-':
            current -= 1
    return count >=3

if __name__ == "__main__":
    print(f("++-+----++++++"))