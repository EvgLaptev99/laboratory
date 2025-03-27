def main():
    input_data = input("Введите слова через пробел: ")
    
    new_word = ""
    
    current_word = ""
    
    for char in input_data:
        if char == ' ':
            if current_word:
                new_word += current_word[-1]
                current_word = ""
        else:
            current_word += char
    
    if current_word:
        new_word += current_word[-1]
    
    print(new_word)

if __name__ == "__main__":
    main()