def can_form_palindrome(s):
    char_count = {}
    for char in s:
        if char.isalnum():
            char = char.lower()
            char_count[char] = char_count.get(char, 0) + 1
    
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    
    if odd_count > 1:
        print("Невозможно составить палиндром")
        return
    
    half_palindrome = []
    middle_char = ""
    
    for char, count in char_count.items():
        if count % 2 != 0:
            middle_char = char
        half_palindrome.append(char * (count // 2))
    
    half_palindrome = ''.join(half_palindrome)
    palindrome = half_palindrome + middle_char + half_palindrome[::-1]
    print(palindrome)

def main():
    input_data = input("Введите слово: ")
    can_form_palindrome(input_data)

if __name__ == "__main__":
    main()