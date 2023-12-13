"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 5: Listy
"""


def main() -> None:
    """
        ? Zadanie 1.
            Napisz komendę w środowisku Python, która zamieni wartość x='Ala ma Asa' wspak.

        * This function reverses the string 'Ala ma Asa'.
    """
    try:
        x: str = 'Ala ma Asa'
        reversed_x: str = x[::-1]
        print(reversed_x)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
