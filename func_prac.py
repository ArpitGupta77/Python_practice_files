# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:04:31 2026

@author: arpit
"""

# def hello():
#     print("Hello World!")
    
# hello()

# def hi(name):
#     print(f"Hello {name}!")

# hi('Arpit')
# hi('Shikhar')

#  hi()

# def hi_2(name='Arpit'):
#     print(f"hello {name}!")

# hi_2('Rachel')


################# fibonacci


# def fib(n):
#     a=0
#     b=1
#     for i in range(n):
#         a,b = b,a+b
#     return a

# fib_num = fib(20)
# print(fib_num)

###################### calc mean

# def calc_mean(first,*remainder):
#     mean = (first + sum(remainder)) / (1 + len(remainder))
#     return mean

# print(calc_mean(23,43,56,76,45,34,65,78,975,3456,54))


''' recursion '''

'''fibonacci using recursion'''

def fib_2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_2(n-1) + fib_2(n-2)
    
x = fib_2(20)
print(x)
# y = fib_2(1000)
# print(y)

''' factorial of 5 using recusrion'''

def fact(n):
    if n == 0 or n==1:
        return n
    else:
        return n * fact(n-1)
    
result = fact(5)
print("factorial of 5 is ",result)





























