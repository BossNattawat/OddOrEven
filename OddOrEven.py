def main():
    numbers = []
    even = []
    odd = []
    i = 0

    times = int(input("How many number do you want to add : "))

    while True:
        if times <= 0:
            return False
        i += 1
        numberInput = int(input("Enter some number : "))
        numbers.append(numberInput)
        if i >= times:
            break

    for number in numbers:
        if (number % 2) == 0:
            even.append(number)
        else:
            odd.append(number)

    print("-------------------------")
    print(f"Even number : {even}")
    print(f"Odd number : {odd}")
    print("-------------------------")


if __name__ == "__main__":
    main()
