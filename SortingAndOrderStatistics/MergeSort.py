import sys
def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    left = []
    right = []

    for i in range(0,n1):
        left.append(A[p+i])
    for j in range(0,n2):
        right.append(A[q+j+1])
    i = 0
    j = 0
    left.append(sys.maxsize)
    right.append(sys.maxsize)

    for k in range(p,r+1):

        if(left[i]<= right[j]):
            A[k] = left[i]
            i +=1
        else:
            A[k] = right[j]
            j += 1

def mergeSort(A,p,r):
    if(p<r):
        q = int((p+r)/2)
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)

if __name__ == "__main__":
    a = [5,2,4,7,1,3,2,6,5,-1]
    mergeSort(a,0,len(a)-1)

    print(a)