def tip(doll,percent):
    tip=""
    doll=input("how much was the mean")
    percent=input("waht is the percentage would you like to have")
    tip = float(doll) * float(percent)
    print(f"leave ${tip:.2f}")
