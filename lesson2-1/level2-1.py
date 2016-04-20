givstring = "Hi hi hi and hihi and one more hi"
print (givstring)
result = givstring.split()
print (result)
print ("\nThe total number of \"hi\" is: " + str(result.count("hi")))
#print (type(givstring), type(result), type(result.count(" ")))

givstring = givstring.lower()
print (givstring.replace("hi", "bye", 0))

result = givstring.split()
print (result)
print ("\nThe total number of \"hi\" is: " + str(result.count("hi")))