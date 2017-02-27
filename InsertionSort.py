
def insertionSort(lst):
    #increasing order
    for i in range(1,len(lst)):
        key = lst[i]
        j = i-1
        while j>=0 and lst[j]>key:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key

    return lst
def insertionSortD(lst):
    #drerasing order
    for i in range(1,len(lst)):
        key = lst[i]
        j = i - 1
        while j>=0 and lst[j]<key:
            lst[j+1] = lst[j]
            j-=1
        lst[j+1] = key


if __name__ == "__main__":
    lst = [3,4,7,1,5,2,3]

    # insertionSort(lst)
    insertionSortD(lst)
    print(lst)