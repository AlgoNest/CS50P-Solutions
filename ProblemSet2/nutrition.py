Fruits ={
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit":60,
    "grapes": 90,
    "honeydew": 50,
    "kiwifruit":90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange":80,
    "peach": 60,
    "pear":100,
    "pineapple":50,
    "plums":70,
    "strawberries":50,
    "sweet cherries":100,
    "tangerine":50,
    "watermelon":80
    }
UserInput=input("Item : ")

if UserInput in ["apple","Apple"]:
    print(f"Calories : {Fruits.get("apple","Unknown")}")
elif UserInput in ["avocado","Avocado"]:
    print(f"Calories : {Fruits.get("avocado","Unknown")}")
elif UserInput in ["banana","Banana"]:
    print(f"Calories : {Fruits.get("banana","Unknown")}")
elif UserInput in ["cantaloupe","Cantaloupe"]:
    print(f"Calories : {Fruits.get("canttaloupe","Uknown")}")
elif UserInput in ["grapefruit","Grapefruit"]:
    print(f"Calories : {Fruits.get("grapefruit","Unkown")}")
elif UserInput in ["grapes","Grapes"]:
    print(f"Calories : {Fruits.get("grapes","Unknown")}")
elif UserInput in ["honeydew melon","Honeydew Melon"]:
    print(f"Calories : {Fruits.get("honeydew","Uknown")}")
elif UserInput in  ["kiwifruit","Kiwifruit"]:
    print(f"Calories : {Fruits.get("kiwifruit","Uknown")}")
elif UserInput in  ["lemon","Lemon"]:
    print(f"Calories : {Fruits.get("lemon","Unknown")}")
elif UserInput in  ["lime","Lime"]:
    print(f"Calories : {Fruits.get("lime","Unknown")}")
elif UserInput in  ["nectarine","Nectarine"]:
    print(f"Calories : {Fruits.get("nectarine","Unknown")}")
elif UserInput in ["orange","Orange"]:
    print(f"Calories : {Fruits.get("orange","Unknown")}")
elif UserInput in  ["peach","Peach"]:
    print(f"Calories : {Fruits.get("peach","Unknown")}")
elif UserInput in ["pear","Pear"]:
    print(f"Calories : {Fruits.get("pear","Unknown")}")
elif UserInput  in ["pineapple","Pineapple"]:
    print(f"Calories : {Fruits.get("pineapple","Unknown")}")
elif UserInput in  ["plums","Plums"]:
    print(f"Calories : {Fruits.get("plums","Unknown")}")
elif UserInput in ["strawberries","Strawberries"]:
    print(f"Calories : {Fruits.get("strawberries","Unknown")}")
elif UserInput in  ["sweet cherries","Sweet Cherries"]:
    print(f"Calories : {Fruits.get("sweet cherries","Unknown")}")
elif UserInput in ["tangerine","Tangerine"]:
    print(f"Calories : {Fruits.get("tangerine","Unknown")}")
elif UserInput in ["watermelon","Watermelon"]:
    print(f"Calories : {Fruits.get("watermelon","Unknown")}")



