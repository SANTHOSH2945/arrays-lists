def pairSum(list,n,s):
    for i in range(n):
        k = list[i]
        for j in range(i+1,n):
            k = k + list[j]
            if k == s:
                return str(i)+str(j)
arr = [2,3,4,1,6]
k = 8
l = len(arr)
print(pairSum(arr,l,k))
