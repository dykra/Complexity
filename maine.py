import timeit
import time
from random import randint
from copy import copy


def quickSort2(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort2(less)
        more = quickSort2(more)
        return less + pivotList + more


def sort(tab): #zwraca posortowaną tablicę
    for i in range(len(tab)):
        j=len(tab)-1 #od ostatniej komórki
        while j>i:   #do aktualnie szukanej jako najmniejsza
            if tab[j]<tab[j-1]: #jeśli komórka wcześniej jest mniejsza, zamienia
                tmp=tab[j]
                tab[j]=tab[j-1]
                tab[j-1]=tmp
            j-=1
    return tab

def insertionsort( aList ):
 for i in range( 1, len( aList ) ):
   tmp = aList[i]
   k = i
   while k > 0 and tmp < aList[k - 1]:
       aList[k] = aList[k - 1]
       k -= 1
   aList[k] = tmp
   return aList

def maine(a):
   # print(a)
    a = insertionsort(a)
    a = sort(a)
    a.reverse()
    a.reverse()
   # print(a)
    return a

def createList(N):
    A = []
    for i in range(1, N):
        A.append(randint(1, 100))
    return A

def cleane(a):
    print(a)

def quicksort(array):
    _quicksort(array, 0, len(array) - 1)


def _quicksort(array, start, stop):
    if stop - start > 0:
        pivot, left, right = array[start], start, stop
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        _quicksort(array, start, right)
        _quicksort(array, left, stop)

#print(timeit.timeit('sorted(A)', number=1000))



def jakas():
    N = 10
    counter1 = 0
    counter2 = 0
    for i in range(1, 10):
        N = 10 * i
        A = []
        for j in range(1, N):
            A.append(randint(1, 100))
        B = copy(A)
        time1a = time.time()
        sorted(B)
        time2a = time.time()
        #counter1 += (time2a-time1a)
        print(time2a -time1a)
        time1 = time.time()
        quicksort(B)
        time2 = time.time()
        #counter2 += (time2-time1)
        print(time2-time1)
        print("\n")

    print(counter1/N)
    print(counter2/N)

    print("\n")
    #100 000 sortowac normaly i rosetta
    #potem wykres

    #jeden co z miejscu drugi nie w miejsu


    A = []
    for j in range(1, N):
        A.append(3) # randint(1, 100))
    B = copy(A)
    time21a = time.time()
    sorted(B)
    time21b = time.time()
    print(time21b-time21a)
    time22a = time.time()
    quicksort(B)
    time22b = time.time()
    print(time22b-time22a)
