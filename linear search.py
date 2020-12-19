def linear_search(number,search_element):
    for i in range(len(number)):
        if number[i]==search_element:
            return i
    else:
        return -1
if __name__=="__main__":
    n=int(input("enter the number of elements you need:"))
    number=[]
    for i in range(n):
        num=int(input())
        number.append(num)
    element=int(input("enter the element to be searched:"))
    index=linear_search(number,element)
    if index==-1:
        print(element,"it's not present")
    else:
        print(element,"is found at position",index)