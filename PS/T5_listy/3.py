"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 5: Listy
"""


def main() -> None:
    """
        ? Zadanie 3.
            Napisz program, który obliczy największy wspólny dzielnik liczb zapisanych w zmiennych a, b, wykorzystując algorytm Euklidesa.

        * This function calculates the greatest common divisor of the numbers stored in variables a and b using the Euclidean algorithm.
    """
    try:
        a: int = int(input("Podaj pierwszą liczbę: "))
        b: int = int(input("Podaj drugą liczbę: "))
        while b != 0:
            a, b = b, a % b
        print(f"Największy wspólny dzielnik: {a}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
