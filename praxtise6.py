def main():
    ch='a'
    print(type(ch))
    #Dictionary merging
    a={1:"ab",2:"sa"}
    b={3:"abx",4:"san"}
    z={**a,**b}
    #print(main(a,b))
    print(z)
    c='''vive\'k
        ku'mar 
        gupta'''
    print(c)
    string=input("enter some string")
    i=0
    for x in string:
        print("the character present at positive index {} and at negative index {} is {}".format(i,i-len(string),x))
        i=i+1
    s="Good boy"
    print(s[1:7:1])#slicing =s[begin:end:step/increment]
    #CONCATENATION
    print("vivek"+" kumar")
    print("Vivek"*3)
    print(len(s))

    #PRINT CHARACTER IN BACKWARD AND FORWARD DIRECTION
    on="Rahul is boy"
    n=len(on)
    i=0
    print("forward direction is :")
    while (i<n):
        print(on[i],end='')
        i=i+1

    print("\nBacward direction is:")
    i=-1
    while(i>=-n):
        print(on[i],end='')
        i=i-1
#with for loop
    print("\nagain forward direction is : ")
    for i in on:
        print(i,end='')
    
    print("\nagain bacward direction is:\n")

    for i in on[::-1]:
        print(i,end='')
    print('\n')
    print('z' in on)

    sup=input("enter something:")
    sub=input("enter again:")
    if sub in sup:
        print(sub,"is in sup")
    else:
        print(sub,"is not in sup")






if __name__ == "__main__":main()
    