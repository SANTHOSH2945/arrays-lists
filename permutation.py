def permutation(lst1, lst2):
    temp=0
    if len(lst1) == len(lst2):
        for i in lst1:
            if i in lst2:
                temp +=1
        if temp == len(lst1):
            print('These lists are permutations of each other')
        else:
            print('These lists are not permutations of each other')

    else :
        print('These lists are not permutations of each other')
ls1=[2,1,6,3,4,5]
ls2 = [1,2,7,5,4,3]
permutation(ls1,ls2)
# this can also be done using sorting and equalising
