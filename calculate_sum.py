#Напишите функцию calculate_sum, которая принимает на вход одно целочисленное значение N и возвращает сумму всех чисел
# от 1 до N включительно.

def calculate_sum(N):
    ordinal_numbers = []
    if (N >= 0):
        for i in range(1, N + 1):
            ordinal_numbers.append(i)
        return sum(ordinal_numbers)
    else:
        for i in range(abs(N) + 1):
            ordinal_numbers.append(i)
        return (-abs(sum(ordinal_numbers)) + 1)

def test_calculate_sum_positive():
    assert calculate_sum(11) == 66

def test_calculate_sum_negative():
    assert calculate_sum(-10) == (-54)

def test_calculate_sum_zero():
    assert calculate_sum(0) == 0
