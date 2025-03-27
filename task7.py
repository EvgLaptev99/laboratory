def main():
    input_data = input("Введите строку и символ через запятую: ")
    
    s = ""
    i = ""
    comma_found = False
    
    for char in input_data:
        if char == ',':
            comma_found = True
            continue
        if not comma_found:
            s += char
        else:
            i += char

    if len(i) != 1:
        print("Неверный ввод")
        return
    
    count = 0
    
    for char in s:
        if char == i:
            count += 1
        else:
            break 
    print(count)

if __name__ == "__main__":
    main()