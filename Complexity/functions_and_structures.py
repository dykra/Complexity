from random import randint


def sort(tab):
    for i in range(len(tab)):
        j = len(tab)-1
        while j > i:
            if tab[j] < tab[j-1]:
                tmp = tab[j]
                tab[j] = tab[j-1]
                tab[j-1] = tmp
            j -= 1
    return tab


def create_list(n):
    A = []
    for i in range(1, n):
        A.append(randint(1, 100))
    return A


def clean(a):
    print(a)
