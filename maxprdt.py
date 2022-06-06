# Maximum product of two integers
def produc(arr):
    temp = 0
    a = 0
    b = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i]*arr[j]) > temp:
                temp = (arr[i]*arr[j])
                a = i
                b = j
    return temp,a+1,b+1
lst = [1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21]
print(produc(lst))
