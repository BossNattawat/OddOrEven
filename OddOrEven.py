def main():
    numbers = []
    even = []
    odd = []

    times = int(input("How many number do you want to add : "))

    while times != 0:
        if times <= 0:
            return False
        times -= 1
        numberInput = int(input("Enter some number : "))
        numbers.append(numberInput)

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
