string=input("Enter string:")
count=0
conso=0
for i in string:

      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            count=count+1
            #conso=len(string)-count
print("Number of vowels are:")
print(count)
print(len(string))
       