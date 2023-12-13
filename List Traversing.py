# list = ['A','N','O','W','A','R']
list = []   #dynamic list(which is created by owner)
n = int(input("Enter input list size:"))
for i in range(n):
    val =(input("Enter a value:"))
    list.append(val)

length = len(list)
for i in range(length):
    print(i,list[i])