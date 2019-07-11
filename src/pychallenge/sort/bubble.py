def bubble_sort(mylist: list):
    swapped = True

    if len(mylist) <= 1:
        return mylist

    while swapped:
        swapped = False
        for i in range(0, len(mylist) - 1):
            if mylist[i] > mylist[i + 1]:
                mylist[i], mylist[i + 1] = mylist[i + 1], mylist[i]
                swapped = True

    return mylist
