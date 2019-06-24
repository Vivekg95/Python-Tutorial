'''import re
import urllib
import urllib.request
u=urllib.request.urlopen("https://www.redbus.in/info/contactus")
text=u.read()
numbers=re.findall("[0-9]{7}[0-9-]+",str(text),re.l)
for n in numbers:
    print(n)'''

import urllib,re
import urllib.request
f = urllib.request.urlopen("https://www.redbus.in/info/contactus")
s = f.read()                       #error code
re.findall(r"\+\d{2}\s?0?\d{10}",s)
re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)
