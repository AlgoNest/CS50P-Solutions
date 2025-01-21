def main():
      while True:
          fuel = input("Enter: ")
          try:
              result = gauge(convert(fuel))
              print(result)

          except (ValueError, ZeroDivisionError):
            pass
          else:
              break
def convert(fraction):
         numerator,denominator = fraction.split("/")
         NewNum = int(numerator)
         NewDen = int(denominator)
         Result = NewNum / NewDen

         FinalResult = int(Result * 100)
         return FinalResult


def gauge(percentage):
      if  percentage <= 1 :

         return "E"

      elif percentage >= 99 :

         return "F"
      else:

        return f"{percentage}%"
if __name__ == "__main__":
    main()
