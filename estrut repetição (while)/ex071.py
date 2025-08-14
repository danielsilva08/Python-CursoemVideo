from bisect import bisect_left

def binary_search(an_interable, target):
    index = bisect_left(an_interable, target)
    if index <= len(an_interable) and an_interable[index] == target:
        return True
    return False

