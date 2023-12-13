"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 3: Pętle
"""


def main() -> None:
    """
        ? Zadanie 9.
            Wyświetl na ekranie pusty kwadrat składający się z 16 znaków ‘#’.

        * This function displays an empty square consisting of 16 '#' characters.
    """
    # print('#' * 5)
    # for _ in range(3):
    #     print('#' + ' ' * 3 + '#')
    # print('#' * 5)
    for i in range(5):
        if i == 0 or i == 4:
            for _ in range(5):
                print('#', end='')
        else:
            print('#', end='')
            for _ in range(3):
                print(' ', end='')
            print('#', end='')
        print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
