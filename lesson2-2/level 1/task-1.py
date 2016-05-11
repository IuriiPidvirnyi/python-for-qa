#Write a function which takes a string and returns its first 10 characters concatenated with the last 10 characters.

def concat(s):
    if len(s)>=21:
        s = s[0:10]+'|'+s[-11:-1]
        return s
    else:
        print ("String contains less than 21 characters")
        s = raw_input("Please enter string with required length: ")
        print "Updated string is:", s
        return concat(s)

if __name__ in "__main__":
    s = "supposed to change"
    cs = concat(s)
    print "\n Concatenated string is:", cs