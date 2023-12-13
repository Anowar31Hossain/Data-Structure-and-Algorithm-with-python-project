def linear_search(list,item):
    count=0
    h=0
    length=len(list)
    for i in range(length):
        if item==list[i]:
            count=count+1
            h=i
            break
    return count,h
            
if __name__ == '__main__':
    list=[]
    n=int(input("Enter list length what to you want:"))
    for i in range(n):
        val=int(input(f"Enter {i+1} value for list:"))
        list.append(val)
    print(list)
    item=int(input("Enter item what you want to search:"))
    count,h=linear_search(list,item)
    if count==1:
        print(f"your item found in position: {h}")

    else:
        print("your item is not found in list.")

