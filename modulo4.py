def sayHi():
    return print('Hola que tal :)')

def sayHi2():
    print('Otro saludooo buen diaaaa :D')
    #nota que aquí no uso return

def maxDivisor(n):
    max_divisor = 0
    i = 1
    while i < n:
        if n % i == 0:
            max_divisor = i
        i = i + 1
    return print(max_divisor)

sayHi()
sayHi2()
maxDivisor(10)