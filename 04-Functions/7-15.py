def f(detector):
    current_count = 0
    count = 0

    for action in detector:
        if action == '+':
            current_count += 1
            count = current_count
        elif action == '-':
            current_count -= 1

        if count >= 3:
            return True
        
    return False

if __name__ == '__main__':
    print(f("+-+-+---"))