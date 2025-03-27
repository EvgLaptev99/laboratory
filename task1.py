def main():
    input_data = input("")
    input_data = input_data.replace(" ", "")
    comma_index = input_data.index(',')
    
    a = int(input_data[:comma_index])
    b = int(input_data[comma_index + 1:])

    if b == 0:
        print("число ровно нулю")
    else:
        ostatok = a % b
        print(f"{ostatok}")

if __name__ == "__main__":
    main()