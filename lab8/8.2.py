def fibonacii(n):
    if n == 1 or n==0:
        return 1
    else:
        return fibonacii(n-1)+fibonacii(n-2)

print(fibonacii(3))