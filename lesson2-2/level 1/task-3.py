"""
3 Write a function that takes a list and returns a new
list that contains all the elements of the first list minus all the duplicates:
"""
#def uniq(a):
def deduplication (a):
    return set(a)

if __name__ in "__main__":
    a = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5, 7, 8, 9, 7, 9, 9, 8]
    b = ['a', 'd', 'v', 'a', 'd', 'v', 's', 'f', 'g', 'b', 'n', 'b', 'n', 'b', 'n', 'b', 'n']
    print list(deduplication(a))
    print list(deduplication(b))