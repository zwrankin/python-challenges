def merge(a, b):
    c = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            c.append(a[0])
            a = a[1:]
        else:
            c.append(b[0])
            b = b[1:]

    if len(a) == 0:
        c += b
    else:
        c += a

    return c


def merge_sort(mylist):
    if len(mylist) <= 1:
        return mylist

    else:
        mid = len(mylist) // 2

        a = merge_sort(mylist[:mid])
        b = merge_sort(mylist[mid:])

        return merge(a, b)
