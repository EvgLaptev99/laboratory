def check_numbers(numbers):
    if all(num == numbers[0] for num in numbers):
        print("Все числа равны")
    elif len(set(numbers)) == len(numbers):
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")

def main():
    input_data = input("Введите числа через пробел: ")
    numbers = list(map(int, input_data.split()))
    check_numbers(numbers)

if __name__ == "__main__":
    main()