def commonCharacterCount(s1, s2):
    common = [min(s1.count(i),s2.count(i)) for i in set(s1)]
    return sum(common)
    