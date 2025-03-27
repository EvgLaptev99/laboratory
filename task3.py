def main():
    input_data = input("Введите три целых числа через пробел: ")
    a, b, c = map(int, input_data.split())
    if (a <= b <= c) or (c <= b <= a):
        middle = b
    elif (a <= c <= b) or (b <= c <= a):
        middle = c
    else:
        middle = a
    print(middle)

if __name__ == "__main__":
    main()