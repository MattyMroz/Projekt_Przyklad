"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 4: Stringi
"""


def main() -> None:
    """
        ? Zadanie 10.
            Wyświetl dowolny napis z usuniętymi wiodącymi białymi znakami.

        * This function asks the user for any text and then displays the text with leading whitespace removed.
    """
    try:
        text: str = input("Podaj dowolny napis: ")
        text_without_leading_whitespace: str = text.lstrip()
        print(text_without_leading_whitespace)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
