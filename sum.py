#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in June 2022
# This is the math program, calculating the sum of numbers in the list


def total(number_list):
    # This function calculates the sum
    total = 0
    for a_number in number_list:
        total = total + a_number
    return total


def main():
    # This function does try and catch
    number_list = []
    a_number_string = None

    # input
    print("This program calculates the sum of the numbers you entered.")
    print("Please enter 1 number at a time. Enter -1.0 to end.")

    # process & output
    print
    while True:
        a_number_string = input("Please enter a number: ")
        try:
            a_number = float(a_number_string)
            if a_number_string != "-1.0":
                number_list.append(a_number)
            else:
                break
        except Exception:
            print("Invalid number!")
    # call functions
    answer = total(number_list)
    print("\nThe sum of all numbers is {}.".format(answer))
    print("\nDone.")


if __name__ == "__main__":
    main()
