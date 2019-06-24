import os
os.chdir('')#F:\\Blacklist
print(os.getcwd())
COUNT=1
def increment():
    global COUNT
    COUNT=COUNT+1

for f in os.listdir():
    f_name,f_ext=os.path.splitext(f)
    f_name="blok " + str(COUNT)
    increment()

    new_name='{} {}'.format(f_name,f_ext)
    os.rename(f,new_name)