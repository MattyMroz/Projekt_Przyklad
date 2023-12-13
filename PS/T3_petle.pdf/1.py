"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 3: Pętle
"""


def main() -> None:
    """
        ? Zadanie 1.
            Wyświetl sumę liczb nieparzystych od 1 do 21.

        * This function displays the sum of odd numbers from 1 to 21.
    """
    print(sum(i for i in range(1, 22) if i % 2 != 0))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
