def filevk(x):
    try:
        print(x)                             #Execption handling

        return int(x)
    except Exception:
        print("Exception is found")

if __name__=="__main__":filevk("vk") #ValueError: invalid literal for int() with base 10: 'vk'