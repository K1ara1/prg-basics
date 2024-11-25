def f(array, number):
    count=0
    for item in array:
        if item > number:
            count+=1
    return count

array=[1,2,3,4,5,6,7,8,9]
number=int(input('what is number: '))

print(f(array,number))