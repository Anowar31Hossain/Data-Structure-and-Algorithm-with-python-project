a = []
size = int(input("Enter size of the list:"))
for i in range(size):
    val=int(input("Enter list element:"))
    a.append(val)

print("Before Insertion element in list:",a)
a.append(None)
print(a)
item=int(input("Enter item what you want insert:"))
position = int (input("Enter position what you want position insert in the list:"))
for i in range(size,position,-1):
    print(i)

a[position]=item
print("After insertion in list:",a)


