def maximum_element(num):
    max=num[0]
    for i in range(1,len(num)):
        max=num[i]
    return max
if __name__=="__main__":
    n=int(input("enter the number of elements you need:"))
    number=[]
    for i in range(n):
        num=int(input())
        number.append(num)
    print(maximum_element(number))

