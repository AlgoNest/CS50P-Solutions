def convert(text):
    """
    Convert :) to 🙂 and :( to 🙁 in the given text.

    Parameters:
    text (str): The input string to be converted.

    Returns:
    str: The converted string with emoticons replaced.
    """
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    """
    Main function to prompt the user for input and print the converted text.
    """
    user_input = input("Enter your text: ")
    converted_text = convert(user_input)
    print(converted_text)

if __name__ == "__main__":
    main()

