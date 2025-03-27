def main():
    binary_string = input("Введите строку из 0 и 1: ")
    
    if not all(char in '01' for char in binary_string):
        print("Неправильно введены числа")
        return
    
    count_0 = 0
    count_1 = 0
    
    for char in binary_string:
        if char == '0':
            count_0 += 1
        elif char == '1':
            count_1 += 1
    
    if count_0 == count_1:
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()