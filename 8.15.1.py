
def findPrime(n):
    array = [True for _ in range(n + 1)]

    i = 1
    while 2 * i * (i + 1) < n:
        j = i
        while j <= (n - i) / (2 * i + 1):
            array[2 * i * j + i + j] = False
            j = j + 1
        i = i + 1

    for i in range(1, n + 1):
        elem = array[i]
        if elem:
            prime = 2 * i + 1
            if prime > n: break
            a = bin(prime)[2:]
            b = bin(prime)[2:][::-1]

            if a == b:
                print(prime, end=' ')
n = int(input("enter the numb: "))
findPrime(n)
