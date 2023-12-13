"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 5: Listy
"""


def main() -> None:
    """
        ? Zadanie 2.
            Napisz program, który wypisze listę wszystkich indeksów w łańcuchu x, na których zaczyna się podłańcuch s.

        * This function prints a list of all indices in the string x where the substring s begins.
    """
    try:
        x: str = input("Podaj łańcuch znaków: ")
        s: str = input("Podaj podłańcuch: ")
        indices: list = [i for i in range(len(x)) if x.startswith(s, i)]
        print(indices)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
