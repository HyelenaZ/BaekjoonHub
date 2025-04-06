import sys
input = sys.stdin.readline

def factorize(number):
    divisor = 2
    while divisor * divisor <= number:  
        while number % divisor == 0:  
            print(divisor) 
            number //= divisor  
        divisor += 1  
    if number > 1: 
        print(number)

N = int(input())

if N != 1:
    factorize(N)
