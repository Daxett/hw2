""" Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N."""

n = int(input("Введите число: "))
a = []
for i in range(1, n+1):
    print(i, sep=" ",end=" ")
    if(i < n):
        print("+", sep=" ", end=" ")
    a.append(i)
print("=", sum(a))