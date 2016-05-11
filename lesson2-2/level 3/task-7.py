# Write a function to find out if the word is a palindrome.

def palindrome(a):
    if a[::1]==a[::-1]:
        print (a + " - is a palindrome")
    else:
        print (a + " - is not a palindrome")

if __name__ == "__main__":
    a="abuttuba"

palindrome(a)