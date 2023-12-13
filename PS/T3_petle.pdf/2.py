"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 3: Pętle
"""


def main() -> None:
    """
        ? Zadanie 2.
            Wyświetl wszystkie liczby parzyste do liczby 63.
            ! Polecenie jest nie prezyzyjne licząc od 0 do 63, czy od 2 do 63, a może od -nieskończoności do 63 hmmm...?

        * This function displays all even numbers up to 63.
    """
    for i in range(0, 64, 2):
        print(i, end=' ')

    # for i in range(2, 64, 2):
    #     print(i, end=' ')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
