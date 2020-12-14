def get_factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
def get_factorial_recursion(n):
    if n==1:
        return 1
    else:
        return get_factorial_recursion(n-1)*n
num=int(input("enter a number to find a factorial:"))
print(get_factorial_recursion(num))