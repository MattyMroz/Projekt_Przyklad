"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 3: Pętle
"""


def main() -> None:
    """
        ? Zadanie 7.
            Wyświetl na ekranie pionową kreskę składającą się z dziesięciu znaków ‘#’.

        * This function displays a vertical line consisting of ten '#' characters.
    """
    for _ in range(10):
        print('#')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
