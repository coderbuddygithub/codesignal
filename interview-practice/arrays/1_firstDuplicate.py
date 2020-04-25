def firstDuplicate(a):
    tempSet = set();
    for element in a:
        if element in tempSet:
            return element
        tempSet.add(element)
    return -1