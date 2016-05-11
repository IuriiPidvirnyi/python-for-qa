#6 Write a function that returns dictionary where keys are even numbers
# between 1 and n and values are keys in square, by default n = 100.

def dict(n=100):
    dic={}
    a=range(2,n+1,2)
    for elem in a:
        dic[elem]=elem**2
        print dic
    print ("\n Result: " + str(dic))


if __name__ in "__main__":
    dict(30)

