array = [15, 8, 31, 47, 2, 19]
stack = []
reversed = ''
for i in array:
    stack.append(i)

for _ in range(len(stack)):
    reversed += str(stack.pop()) + ' '

print(reversed)

