def main():
    side_length = float(input("Введите длину стороны квадрата: "))
    perimeter = 4 * side_length
    area = side_length ** 2
    diagonal = (2 ** 0.5) * side_length
    result = f"{perimeter:.2f}, {area:.2f}, {diagonal:.2f}"
    print(result)

if __name__ == "__main__":
    main()