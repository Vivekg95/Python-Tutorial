string=input("Enter string:")
vowels=0
consonant=0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
    
        vowels=vowels+1
    else:
        consonant=consonant+1

print("Number of vowels are:",vowels)
print("number of consonants are:",consonant)
