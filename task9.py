def main():
    phone_number = input("Введите номер телефона: ")
    allowed_characters = set("0123456789+")
    cleaned_number = ""
    for char in phone_number:
        if char in allowed_characters:
            cleaned_number += char
    print(cleaned_number)

if __name__ == "__main__":
    main()