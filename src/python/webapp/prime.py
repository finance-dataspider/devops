from logging import raiseExceptions


def prime (num):

    #validate x
    if  (type(num) != int):
        raise Exception('Error,X must be a number')
    if  not ((num>=2)  and (num <= 100)):
        raise Exception('Error,X must be between 2 to 10')
    primes = []

    for i in range(2, num + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)

    print(primes)
        
prime(100)