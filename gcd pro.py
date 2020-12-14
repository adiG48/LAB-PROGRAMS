#NORMAL WAY#

def GCD(x,y):
    if x>y:
        small=y
    else:
        small=x
    for i in range(1,small+1):
        if((x%i==0) and (y%i==0)):
            gcd=i
    return gcd

##EUCLIDIEAN WAY OF ALGORITHM##
#GENERAL IDEA:
#GCD(A,B)=GCD(B,A%B)
#GCD(40,60)=GCD(60,40)
#GCD(60,40)=GCD(40,20)
#GCD(40,20)=GCD(20,0)
#TERMINATE WHEN B BECOMES 0

def EUCLIDIEAN_GCD(x,y):
    while(y):
        x,y=y,x%y
    return x
#USING IN BUILT FUNCTIONS#

import math
def math_module(x,y):
    gcd=math.gcd(x,y)
    return gcd

#ANOTHER WAY SIMPLER #

def get_gcd(x,y):
    smallest=min(x,y)
    if x==0 or y==0:
        return max(x,y)
    for i in range(1,smallest+1):
        if((x%i==0) and (y%i==0)):
            gcd=i
    return gcd

# GCD FOR "N" NUMBERS
def find_gcd_n_numbers(x,y):
    while y:
        x,y=y,x%y
    return x
numbers=[40,80,120,160,200]
num1=numbers[0]
num2=numbers[1]
gcd=find_gcd_n_numbers(num1,num2)
for i in range(2,len(numbers)):
    gcd=find_gcd_n_numbers(gcd,numbers[i])
print("gcd is",gcd)

#a=int(input("enter the numbers you want to find gcd"))
#b=int(input("enter the numbers you want to find gcd"))
#print(EUCLIDIEAN_GCD(a,b))