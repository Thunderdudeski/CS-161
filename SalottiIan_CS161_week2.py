def main():
    x = 10
    y = 0xa
    z = 0b1111

    #when x is changed to a floating point number the bin function gives a TypeError because it requires an int
    print(x, bin(x), hex(x))
    print(f"the sum is: {x + y + z}")

    original_size = int(input("Original size: "))
    dictionary_size = int(input("Dictionary size: "))
    compressed_size = int(input("Compressed size: "))
    percent_of_compression = round((1 - ((compressed_size + dictionary_size) / original_size)) * 100, 2)

    print(f"Original size: {original_size} characters\n"
          f"Dictionary size: {dictionary_size} characters\n"
          f"Compressed size: {compressed_size} characters\n"
          f"Percent of compression: {percent_of_compression}%\n\n")

    if input("Would you like to view the extra credit? (y/n)") == 'y':
        number = input("Please enter an integer between -128 and 127: ")
        try:
            int(number)
        except ValueError:
            print("You didn't enter an integer!!")
        else:
            extra_credit(int(number))


def extra_credit(num: int):
    """Finds the two's complement of the given number within range -128,127
    :param num: The number to find the two's complement of"""
    if -128 <= num <= 127:
        #find remainder using modulo which is then used to find the proper binary to print
        new_num = bin(num % 256)[2:]
        if len(new_num) < 8:
            #adds leading 0's for positive numbers and formats number to look like binary
            new_num = f"0b{'0 ' * (8 - len(new_num)) + new_num}"
        print("The 2's complement binary for this number is:  " + new_num)
    else:
        print("Number is out of scope.")


if __name__ == '__main__':
    main()
