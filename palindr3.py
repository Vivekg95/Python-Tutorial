mystr=str(input("enter a string"))

revstr=reversed(mystr)
if list(mystr)==list(revstr):
    print("it is palindrome")
else:
    print("not palindrome")

