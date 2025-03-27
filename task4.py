def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def decimal_to_octal(n):
    if n == 0:
        return "0"
    octal = ""
    while n > 0:
        octal = str(n % 8) + octal
        n //= 8
    return octal

def decimal_to_hexadecimal(n):
    if n == 0:
        return "0"
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    while n > 0:
        hexadecimal = hex_digits[n % 16] + hexadecimal
        n //= 16
    return hexadecimal

def main():
    user_input = input("Введите число: ")
    
    if not user_input.isdigit() or int(user_input) <= 0:
        print("Неверный ввод")
        return
    
    decimal_number = int(user_input)
    
    binary_representation = decimal_to_binary(decimal_number)
    octal_representation = decimal_to_octal(decimal_number)
    hexadecimal_representation = decimal_to_hexadecimal(decimal_number)
    
    print(f"Двоичное представление: {binary_representation}")
    print(f"Восьмеричное представление: {octal_representation}")
    print(f"Шестнадцатеричное представление: {hexadecimal_representation}")

if __name__ == "__main__":
    main()