import random
def mergesort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)
        i=0 
        j=0
        k=0
        while i<len(left) and j<len(right):
             if left[i]<right[j]: # < symobol is used for ascending order and > symbol for desceding order
                 arr[k]=left[i]
                 i=i+1
                 k=k+1
             else:
                 arr[k]=right[j]
                 j=j+1
                 k=k+1
        while i<len(left):
            arr[k]=left[i]
            i=i+1
            k=k+1
        while len(right)>j:
            arr[k]=right[j]
            j=j+1
            k=k+1
        return arr
            

        
       
x= int(input('what will be the size of the array : '))
arr=[int(random.randrange (0,x+1,1)) for i in range(x)]
arr=list(set(arr))
print(len(arr)-x)
mergesort(arr)
print (arr)
    