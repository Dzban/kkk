array = [2,7,3,1,5,3,3,3,3]
def qs(a):
    size = len(a)
    if size == 2:
        if a[0]>a[1]:
            return a[::-1]
    elif size == 1:
        return a
    elif size == 0:
        return []
    pivot = a[int(size/2)]
    a[int(size/2)], a[size-1] = a[size-1], a[int(size/2)]
    j = 0
    for i in range(size-1):
        if a[i]<pivot:
            a[i], a[j] = a[j], a[i]
            j+=1
    a[j], a[size-1] =  a[size-1], a[j]
    return qs(a[:j:]) + [pivot] + qs(a[j+1::])

print(qs(array))

def bs(a):
    i = {}
    r = []
    for element in a:
        if element not in i:
            i[element] = 0
        i[element]+=1
    indexes = qs([x for x in i])
    for index in indexes:
        for t in range(i[index]):
            r.append(index)
    return r

print(bs(array))

def bbs(a):
    for i in range(len(a)):
        for j in range(1, len(a)):
            if a[j]<a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
    return a

print(bbs(array))

def ss(a):
    sorted = []
    while(len(a)):
        minElement = min(a)
        a.pop(a.index(minElement))
        sorted.append(minElement)
    return sorted

print(ss(array))

def ins(a):
    sorted = []
    for element in a:
        index = 0
        for index in range(0, len(sorted)):
            if sorted[index]>element:
                break
            index+=1
        sorted.insert(index, element)
    return sorted

print(ins([2,7,3,1,5,3,3,3,3]))
