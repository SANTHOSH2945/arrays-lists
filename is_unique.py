# Printing unique array
def Unique(arr):
    lst = []
    lst1 = []
    for i in arr:
        if i not in lst:
            lst.append(i)
        else:
            lst1.append(i)
    print("unique",lst)
    print("duplicated elements",lst1)
myList = [1,2,4,2,3,7,6,8,5,9,4,2,3,5,2,6]
Unique(myList)
