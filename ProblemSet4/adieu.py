import inflect
lst=[]
i = inflect.engine()
while True:
    try:
        names=input("enter: ")
        lst.append(names)
    except EOFError:
        print()
        print(f"Adieu, adieu, to {i.join(lst)}")
        quit()

