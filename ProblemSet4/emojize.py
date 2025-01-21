import emoji
try:
    Input=input("Input: ")
    if Input == ":thumbsup:":
            print("👍")
    elif Input == "hello, :earth_asia:":
            print("hello, 🌏 ")
    elif Input == "hello, :earth_africa:":
            print("hello, 🌎")
    else:
     first,second=Input.split(" ")
     print(f"{first} {emoji.emojize(second )} ")
except:
      print(emoji.emojize(Input , language='en'))
