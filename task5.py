def main():
    domain_name = input("Введите доменное имя: ")
    
    if not domain_name:
        print("Неверный ввод")
        return
    
    parts = []
    current_part = ""
    
    for char in domain_name:
        if char == '.':
            if current_part:
                parts.append(current_part)
                current_part = ""
        else:
            current_part += char
   
    if current_part:
        parts.append(current_part)
    
    if len(parts) < 2:
        print("Неверный ввод")
        return
    
    for part in reversed(parts):
        print(part)

if __name__ == "__main__":
    main()