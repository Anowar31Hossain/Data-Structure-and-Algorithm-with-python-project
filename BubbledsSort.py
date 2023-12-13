import sys
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr


if __name__ == '__main__':
    arr=[30,20,10,70,40,5,15]
    print("Sorted Array in python:")
    print(bubble_sort(arr))









