def bubble_sort(arr):
    for i in range(len(arr)-1):
        swap= False
        for j in range(len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap= True
            if(swap==True):
                return

arr=[5,4,3,2,1,1,7,17,2]
bubble_sort(arr)
print(arr)