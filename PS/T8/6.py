"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 8
"""


def main() -> None:
    """
        ? Zadanie 6.
            Napisz program, który pobiera ciąg znaków i koduje go tak, aby liczba symboli była reprezentowana przez liczbę całkowitą i symbol.

        * This function takes a string and encodes it so that the number of symbols is represented by an integer and a symbol.
    """
    string: str = input("Podaj ciąg znaków do zakodowania: ")
    encoded_string: str = ""
    i: int = 0

    while i < len(string):
        count: int = 1
        # Dopóki sąsiednie znaki są takie same, zwiększamy licznik
        while i + 1 < len(string) and string[i] == string[i+1]:
            i += 1
            count += 1
        encoded_string += f"{count}{string[i]}"
        i += 1

    print(f"Zakodowany ciąg znaków: {encoded_string}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
