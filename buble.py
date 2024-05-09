import time
import numpy as np
import matplotlib.pyplot as plt
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)):
            if arr[i]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                

times=list()
arr=list()
numtimes=list()
for i in range(1,8):
    start=time.time()
    n=int(input("enter the no of element"))
    numtimes.append(n)
    for x in range(n):
        number=np.random.randint(10,99)
        arr.append(n)
    print("list before sorting",x+1,"elements")
    print(arr)
    bubbleSort(arr)
    end=time.time()
    times.append(end-start)
    print("list after bubblesort of",x+1,"elements")
    print(arr)
    print("time taken for bubble sort for",n,"elements is",end-start)
print(numtimes)
print(times)
plt.xlable("list length")
plt.ylable("time complexity")
plt.plot(numtimes,times,label="bubbleSortsort")
plt.grid()
plt.legend()
plt.show()
