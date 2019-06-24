import re
matcher=re.finditer("[^abc]","aab92ababc@")  
for match in matcher:
    print(match.start(),"....",match.group())