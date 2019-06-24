'''import re
s=input("enter mobile number:")
m=re.fullmatch("(0|91)?[7-9][0-9]{9}",s)
if m!=None:
    print("its valid")
else:
    print("Invalid mobile number")''' # valid mobile no

import re
s=input("enter mail:")
m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
if m!=None:
    print("valid mail")
else:
    print("not valid")