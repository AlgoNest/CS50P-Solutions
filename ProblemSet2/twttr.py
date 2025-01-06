def main():
   UserInput = input("Input:")
   print(shorten(UserInput))
def shorten(obj) :
    FinalWord = ""
    for i in obj:
     if i in ["a","e","i","o","u","A","E","I","O","U"]:
       pass
     else:
       FinalWord += i
    return FinalWord

if __name__ == "__main__":
  main()
