###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    for line in file:
        for i in range(1,5):
            i += 1
        print(i,line, end="")