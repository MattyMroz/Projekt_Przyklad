"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 8
"""


def main() -> None:
    """
        ? Zadanie 4.
            Napisz program do obliczenia sumy cyfr liczby 2^20.

        * This function calculates the sum of the digits of the number 2^20.
    """
    number = 2**20
    digit_sum = sum(int(digit) for digit in str(number))
    print(f"Suma cyfr liczby 2^20: {digit_sum}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
