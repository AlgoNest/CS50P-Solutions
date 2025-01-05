def main():
    user = input("Greeting: ").strip().lower()
    print(f"${value(user)}")
def value(user):
    if user.startswith("hello"):
        return 0
    elif user.startswith("h"):
        return 20
    else:
        return 100
if __name__ == "__main__":
    main()
