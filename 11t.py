# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи (число, которое равно сумме двух предыдущих), выведите число -1.

a = int(input('введите число '))
x = 0 #первая сумма фиб
y = 1 #вторая сумма фиб
n = 2
while y < a:
    x, y = y, x + y
    n += 1
if y == a :
    print(n)
else:
    print('-1')    
    
    

    