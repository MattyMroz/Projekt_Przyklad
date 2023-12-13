"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 2: Instrukcje Warunkowe
"""


def main() -> None:
    """
        ? Zadanie 5.
            Napisz program, który pobiera od użytkownika 5 liter. W przypadku gdy pobrana
            litera jest mała zamień ją na wielką, a następnie wyświetl. Jeśli litera jest wielka
            wyświetl ją bez zamiany.

        * This function asks the user for 5 letters. If the letter is lowercase, it is converted to uppercase, otherwise it is displayed without conversion.
    """
    try:
        for _ in range(5):
            letter: str = input("Podaj literę: ")
            if not letter.isalpha() or len(letter) != 1:
                print("Niepoprawne dane, proszę podać pojedynczą literę.")
                continue
            print(letter.upper())
    except KeyboardInterrupt:
        print("Program interrupted by the user.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
