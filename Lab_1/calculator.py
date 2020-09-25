#calculator.py

def sum(m,n):
    result = m
    if n < 0:
        for i in range(abs(n)):
            result -= 1
    else:
        for i in range(n):
            result += 1
    return result

def subtract(m,n):
    result = m
    if n < 0:
        for i in range(abs(n)):
            result += 1
    else:
        for i in range(n):
            result -= 1
            
    return result

def multiply(m,n):
    result =0
    
    if n != 0 or m !=0 :
        negativeResult = m > 0 and n < 0 or m < 0 and n > 0
        n = abs(n)
        m = abs(m)
        
        while ( n > 0):
            result += m
            n -= 1
            
        result = -result if negativeResult else result

    return result

def divide(m, n):
    result = 0
    negativeResult = m > 0 and n < 0 or m < 0 and n > 0
    n = abs(n)
    m = abs(m)

    if n == 0:
        raise ZeroDivisionError('You cannot divide by 0!')

    while (m - n >= 0):
        m -= n
        result += 1
    
    result = -result if negativeResult else result

    return result

def gcd(m, n):

    while n>0:
        r=m%n
        m,n=n,r

    return m