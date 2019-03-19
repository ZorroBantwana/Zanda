import numpy as np
def sum_array(array):
    sum = 0
    for item in array:
        sum+= item
    return sum

def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

    def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def reverse(word):
    reversed_word=''
    for j in word:
        reversed_word=j+reversed_word
    return reversed_word
