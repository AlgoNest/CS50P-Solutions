x,y,z=input("Expression:").split()
nx=float(x)
nz=float(z)
match y:
    case "+":
        print(nx+nz)
    case "-":
        print(nx-nz)
    case "*":
        print(nx*nz)
    case "/":
        print(nx/nz)
    case _:
        print("not valid")
