"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 3: Pętle
"""


def main() -> None:
    """
        ? Zadanie 4.
            Wyświetl na ekranie liczby całkowite od 1 do 10, każda w nowej linii.

        * This function displays integers from 1 to 10, each on a new line.
    """
    for i in range(1, 11):
        print(i)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
