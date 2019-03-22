import numpy as np
def sum_array(array):
    sum_1 = 0
    for item in array:
        sum_1 += item
    return sum_1

def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

def reverse(word):
    reversed_word=''
    for j in word:
        reversed_word=j+reversed_word
    return reversed_word
