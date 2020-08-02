def quick_sort(array,l,r):
    if l<r:
        q = partion(array,l,r)
        quick_sort(array,l,q-1)
        quick_sort(array,q+1,r)

def partion(array,l,r):
    x = array[r]
    i = l-1
    for j in range(l,r):
        if array[j]<=x:
            i +=1
            array[i],array[j] = array[j],array[i]

    array[i+1],array[r] = array[r],array[i+1]
    return i+1


a = [2,4,5,1,67,39,2,2,10,9,11,8,3]
quick_sort(a,0,len(a)-1)
print(a)
