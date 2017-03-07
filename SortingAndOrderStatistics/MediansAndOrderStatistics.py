from SortingAndOrderStatistics.QuickSort import RandomizedQuickSort


def minimum(lst):
    min = lst[0]
    for i in range(1,len(lst)):
        if min > lst[i]:
            min = lst[i]
    return min

def maximum(lst):
    max = lst[0]
    for i in range(1,len(lst)):
        if max < lst[i]:
            max = lst[i]
    return max

# randomized select return i th smallest element of array[p...r]
def randomizedSelect(lst,p,r,i):

    if p == r:
        return lst[p]
    qs = RandomizedQuickSort(lst)
    q = qs.randomizedPartition(p,r)
    k = q-p+1
    if i == k:
        return lst[q]
    elif i<k:
        return randomizedSelect(lst,p,q-1,i)
    else:
        return randomizedSelect(lst,q+1,r,i-k)
if __name__ == "__main__":
    c = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1, 34, 29, 100, 492, 43, 21, 3, 494, 99]
    # print(minimum(c))
    # print(maximum(c))
    print(randomizedSelect(c,0,5,2))