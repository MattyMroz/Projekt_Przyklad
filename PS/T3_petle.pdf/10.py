"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 3: Pętle
"""

# import math


def main() -> None:
    """
        ? Zadanie 10.
            Wyświetl na ekranie wynik operacji 20!.

        * This function displays the result of the operation 20!.
    """
    # print(math.factorial(20))
    result: int = 1
    for i in range(1, 21):
        result *= i
    print(result)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
