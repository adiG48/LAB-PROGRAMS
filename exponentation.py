# my way of finding
def exponent_value(number,exponent):
    expo=number**exponent
    return expo
n=int(input("enter a number:"))
e=int(input("enter exponent value:"))
print(exponent_value(n,e))

#using for loop
def get_power(number,exponent):
    power=1
    for i in range(exponent):
        power=power*number
    return power
n=int(input("enter a number:"))
e=int(input("enter exponent value:"))
print( get_power(n,e))

#using recursion method
def get_expo_recursion(number,exponent):
    if exponent==0:
        return 1
    else:
        return number * get_expo_recursion(number,exponent-1)
n=int(input("enter a number:"))
e=int(input("enter exponent value:"))
print(get_expo_recursion(n,e))
