"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 7.1
"""


def main() -> None:
    """
        ? Zadanie 2.
            Napisz program, aby znaleźć największy czynnik pierwszy dla danej liczby.

        * This function finds the largest prime factor for a given number.
    """
    try:
        number: int = int(input("Podaj liczbę: "))
        i: int = 2
        while i * i <= number:
            if number % i:
                i += 1
            else:
                number //= i
        print(
            f"Największy czynnik pierwszy dla podanej liczby wynosi: {number}")
    except ValueError:
        print("Incorrect input, please enter a number.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
