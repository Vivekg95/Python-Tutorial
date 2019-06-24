def main():
    a="""vicek""" 
    b="cat's" #this is string
    x=3 #multiassignment operator
    vk="ra h ul"
    name="Tom"
    lastname="mackenzie"
    vk.split(",")
    
    
    y=4
    o=x+y
    r=("abc","bfg",20,90,(92,12)) #immutable means cannot change 
    t=(23,34,4)
    v=(4,8,9)
    z=(23,65)+(45,87)+(56,76)
    z=z*2
    c=(1,2,3,0)
    w=dict(name="vivek",surname="kumar")
    
    w.update(name="rahul")
    
    
    
    b=list(c)
    print(vk)
    print(f"Hi MY name is {name} ,surname is {lastname}")

    
    
    
    
    
     

    print(b)
    print(o)
    print(w)
    
    
    
    print(z)
    
    print(t,v)
    print(23 not in t) #will return boolean value true or false
    print(r[-1])
    print(r[:])
    print(t)
    
    print(x)
    print(y)
    print(r)
    
    

    
    print(a)
    print(len(b))
    
    
if __name__=='__main__':main()
