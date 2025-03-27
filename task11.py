def fast_power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_power = fast_power(a, n // 2)
        return half_power * half_power
    else:
        return a * fast_power(a, n - 1)

def main():
    input_data = input("Введите два числа a и n через пробел: ")
    a, n = map(int, input_data.split())
    result = fast_power(a, n)
    print(result)

if __name__ == "__main__":
    main()