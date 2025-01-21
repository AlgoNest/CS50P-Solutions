import random

while True:
        try:
            n=int(input("Level: "))
            if n > 0:
                  break
        except:
            pass

result=random.randint(1,n)
while True:
        try:
            Guess=int(input("Guess: "))
            if Guess > 0 :
                if result > Guess:
                            print("Too small!")
                elif result < Guess:
                            print("Too large!")
                else:
                        print("Just right!")
                        break
        except:
                pass







