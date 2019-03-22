import numpy as np
def sum_array(array):
    sum_1 = 0
    for item in array:
        sum_1 += item
    return sum_1

def fibonacci(n):
    """
    the Fibonacci sequenceis characterized by the fact that every number 
    after the first two is the sum of the two preceding ones        
    """
    if n <= 1:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def reverse(word):
    reversed_word=''
    for j in word:
        reversed_word=j+reversed_word
    return reversed_word
