# Напишите функцию calculate_even_sum, которая принимает на вход список чисел и возвращает сумму всех четных чисел в этом
# списке.

def calculate_even_sum(list_numbers):
    def is_even(value):
        return (type(value) is int or type(value) is float) and (value % 2 == 0)
    return sum((number for number in list_numbers if is_even(number)))


def test_positive_numbers():
    list_numbers_tc = [2, 3, 4, 5, 6, 7, 8]
    assert calculate_even_sum(list_numbers_tc) == 20


def test_zero():
    list_numbers_tc = []
    assert calculate_even_sum(list_numbers_tc) == 0
    list_numbers_tc = [0, None, 0]
    assert calculate_even_sum(list_numbers_tc) == 0


def test_negative_numbers():
    list_numbers_tc = [-1, -2, -4, 0, -2]
    assert calculate_even_sum(list_numbers_tc) == -8


def test_mix_numbers():
    list_numbers_tc = [1, -2, 4, 0, 2]
    assert calculate_even_sum(list_numbers_tc) == 4

def test_char_and_numbers():
    list_numbers_tc = [1, -2, 4, 'k', 2]
    assert calculate_even_sum(list_numbers_tc) == 4

def test_char_and_numbers():
    list_numbers_tc = [1, -2, 4, 'k', 2, 0.1, 2.0]
    assert calculate_even_sum(list_numbers_tc) == 6
