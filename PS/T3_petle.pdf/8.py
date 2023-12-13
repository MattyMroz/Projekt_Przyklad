"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 3: Pętle
"""


def main() -> None:
    """
        ? Zadanie 8.
            Wyświetl na ekranie wypełniony kwadrat składający się z 25 znaków ‘#’.

        * This function displays a filled square consisting of 25 '#' characters.
    """
    # for _ in range(5):
    #     print('#' * 5)
    for _ in range(5):
        for _ in range(5):
            print('#', end='')
        print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
