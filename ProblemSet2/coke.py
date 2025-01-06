AmountDue = 50
while  AmountDue > 0 :
      print("Amount Due:",AmountDue)
      coin = int(input("Insert coin: "))
      if coin in [25,10,5]:
            AmountDue-=coin

Changeowed = abs(AmountDue)
print("Change Owed:",Changeowed)


#take until reach 50 cents
#and in the last show the amount owed for user
