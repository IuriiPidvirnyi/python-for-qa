"""
Write a function that takes a comma-separated string and returns the last element (separated by the last comma)
or the entire string, if there is no comma in it.
"""

def comsep(b):
    a = ","
    i = (len(b) -1) - b[::-1].index(a)
    j = i + 1
    #print (j)
    #print (b)
    #print (len(b) -1)
    #print b[::-1]
    #print ((len(b) -1) - b[::-1].index(a))
    if a in b:
        return b[j]
    else:
        return b


    # if str(a):
    #     if a.split(','):
    #         b= a.split(',')[-1]
    #         print b
    #     else: print a



if __name__ == "__main__":
    a = ","
    b = "fu n, c,ti ,o,n"
    c = "string,without,comma"
print (comsep(b))
print (comsep(c))
