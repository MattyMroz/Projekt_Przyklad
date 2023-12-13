"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 7.1
"""


def main() -> None:
    """
        ? Zadanie 1.
            Napisz program, który obliczy sumę wszystkich wielokrotności 3 lub 5 poniżej 500.

        * This function calculates the sum of all multiples of 3 or 5 below 500.
    """
    try:
        sum_of_multiples: int = sum(
            i for i in range(500) if i % 3 == 0 or i % 5 == 0)
        print(
            f"Suma wszystkich wielokrotności 3 lub 5 poniżej 500 wynosi: {sum_of_multiples}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
