# Напишите функцию calculate_even_sum, которая принимает на вход список чисел и возвращает сумму всех четных чисел в этом
# списке.

def calculate_even_sum(list_numbers):
    return sum(numbers for numbers in list_numbers if numbers % 2 == 0)


def test_positive_numbers():
    list_numbers_tc = [2, 3, 4, 5, 6, 7, 8]
    assert calculate_even_sum(list_numbers_tc) == 20


def test_zero():
    list_numbers_tc = []
    assert calculate_even_sum(list_numbers_tc) == 0
    list_numbers_tc = [0, 0, 0]
    assert calculate_even_sum(list_numbers_tc) == 0


def test_negative_numbers():
    list_numbers_tc = [-1, -2, -4, 0, -2]
    assert calculate_even_sum(list_numbers_tc) == -8


def test_mix_numbers():
    list_numbers_tc = [1, -2, 4, 0, 2]
    assert calculate_even_sum(list_numbers_tc) == 4

