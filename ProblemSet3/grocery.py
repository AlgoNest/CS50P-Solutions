
lst ={}
while True:
    try:
        Item=input().upper()
        if Item in lst:
            lst[Item] += 1
        else:
            lst[Item] = 1

    except EOFError:
        for i in sorted(lst.keys()):
            print(lst[i], i)
        break


