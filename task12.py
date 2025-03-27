def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    input_data = input("Введите два числа через пробел: ")
    a, b = map(int, input_data.split())
    result = gcd(a, b)
    print(result)

if __name__ == "__main__":
    main()