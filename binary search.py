def binary_search(number,search_element):
    first=0
    last=len(number)-1
    while first<= last:
        middle=(first+last)//2
        if search_element==number[middle]:
            return middle
        elif search_element<number[middle]:
            last=middle-1
        elif search_element>number[middle]:
            first=middle+1
    return -1

if __name__=="__main__":
    n=int(input("enter the number of elements you need:"))
    number=[]
    for i in range(n):
        num=int(input())
        number.append(num)
    element=int(input("enter the element to be searched:"))
    index=binary_search(number,element)
    if index==-1:
        print(element,"it's not present")
    else:
        print(element,"is found at position",index)