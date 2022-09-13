print('put on a number of numbers to be in a set')
a=int(input())
b=0
num = []
#узнали число n и создали пустой список 

"""Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму."""

print('please, put on numbers throught "enter"')
while b<a:
    num.append(input())
    b=b+1
print(num)
#заполнили список заданным (переменной n) кол-вом значений

z=0
t=0
while z<a:
    m=int(num[z])
    o=(1+1/m)**m+t
    t=o
    z=z+1
print(t)