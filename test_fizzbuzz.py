# import fizzbuzz

from fizzbuzz import my_fizz


def test_my_fizz():
    input_l = range(1,11)
    answers = my_fizz(input_l)
    assert answers == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']