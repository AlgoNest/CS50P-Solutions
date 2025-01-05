# playback.py

def main():
    # Prompt the user for input
    user_input = input("Enter your text: ")

    # Replace each space with three periods
    modified_input = user_input.replace(" ", "...")

    # Output the modified string
    print(modified_input)

if __name__ == "__main__":
    main()

