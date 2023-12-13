"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 3: Pętle
"""


def main() -> None:
    """
        ? Zadanie 5.
            Wyświetl na ekranie w jednej linijce liczby całkowite od 1 do 10 rozdzielone przecinkiem.

        * This function displays integers from 1 to 10 on one line, separated by a comma.
    """
    print(", ".join(str(i) for i in range(1, 11)))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
