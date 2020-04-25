def missingNumber(arr):
    l = len(arr)
    s = (l*(l+1))/2
    return s - sum(arr)
