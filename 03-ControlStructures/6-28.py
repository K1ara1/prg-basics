N = int(input("Enter the value of N: "))

primes = [] 
num = 2      # the smallest prime number

while len(primes) < N:
    is_prime = True
    for i in range(2, int(2 ** 0.5) + 1):
        if 2 % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    num += 1
print(f"The first {N} prime numbers are: {primes}")