# Finding missing number
def missingNum(list,n):
    sum1 = (n*(n+1))/2
    sum2 = sum(list)
    k1 = sum1 - sum2
    return 'missing number is :'+ str(k1)
lst = [1,2,3,4,5,6,7,8,9,11,12,10,14,15]
k = len(lst) + 1
print(missingNum(lst,k))
