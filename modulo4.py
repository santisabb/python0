from  math import  factorial

print(factorial(5))

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
        i += 1
    return print(max_divisor)

def operation1(n):
  if n > 10:
    return 20
    return 15
  return 10
  return 25

def function(x):
    n = 3
    return not bool(x % 3)

def funcion(n):
  a = n ** 3
  b = a ** 2
  c = b + 100
  d = 5 * c
  return print(d)

d = funcion(2)

print(function(10))
resultado1 = operation1(8)
resultado2 = operation1(12)

print(resultado1)
print(resultado2)
sayHi()
sayHi2()
maxDivisor(10)