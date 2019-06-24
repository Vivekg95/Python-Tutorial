def main():
    def at(func,arg):
        return func(func(func(arg))) #af(af(10))=af(10+5)=af(15)=5+15=20
    def af(x):
        return x+5

    print(at(af,10))
if __name__ == "__main__":main()
    