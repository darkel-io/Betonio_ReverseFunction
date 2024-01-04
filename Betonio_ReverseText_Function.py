def reverse(text):
    return text[::-1]

while True:
    input_text = input("Enter your a text: ")

    if not input_text.isalpha():
        print("Enter string type texts only. Please try again.")
    else:
        print(reverse(input_text))
        break
