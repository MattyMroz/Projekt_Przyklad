"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 3: Pętle
"""


def main() -> None:
    """
        ? Zadanie 6.
            Wyświetl na ekranie poziomą kreskę składającą się z dziesięciu znaków ‘#’.

        * This function displays a horizontal line consisting of ten '#' characters.
    """
    # print('#' * 10)
    for _ in range(10):
        print('#', end='')
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
