#to solve a fizzbuzz question with a unit test
'''
Write a program that prints the numbers from 1 to 100. But for multiples of three 
print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz
'''
#06/02/2022 DL

numbers = [i for i in range(1, 101)]
#numbers=[5]

def my_fizz(input_l):
    res = []
    for x in input_l:
        if x % 3 ==0 and x % 5 == 0:
            res.append("FizzBuzz")
        elif x % 3 == 0:
            res.append("Fizz")
        elif x % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(x))
    return res
var = my_fizz(numbers)
print(var)