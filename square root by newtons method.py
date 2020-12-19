"""#HINT
formula:
x=(x+n/x)/2
n=4
x0=4
x1=(x0+4/x0)/2=2.5
x2=(x1+4/x1)/2=2.05
x3=(x2+4/x2)/2=2.006
x4=(x3+4/x3)/2=2.00
square root of 4 = 2"""
def get_sqrt(number,precision):
    sqroot=number
    while abs(number-sqroot*sqroot) > precision:
        print(sqroot)
        sqroot=(sqroot+number/sqroot)/2
    return sqroot
number=int(input("Enter A Number To Find SquareRoot:64"))
precision=0.01
get_sqrt(number,precision)
