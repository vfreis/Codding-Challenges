def primo4(n):
    if n == 1: return False
    divisor = 2
    while n % divisor != 0:
        #print(f'{n} % {divisor} = {n % divisor}')
        divisor += 1
    #print(f'{n} % {divisor} = {n % divisor}')
    return divisor == n

def primo5(n):
    if n == 1: return False
    if n % 2 == 0: return n == 2
    divisor = 3
    while n % divisor != 0:
        #print(f'{n} % {divisor} = {n % divisor}')
        divisor += 2
    #print(f'{n} % {divisor} = {n % divisor}')
    return divisor == n