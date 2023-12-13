"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 4: Stringi
"""


def main() -> None:
    """
        ? Zadanie 9.
            Wyrównaj dowolny napis do prawej w polu o podanej długości.

        * This function asks the user for any text and a field length, and then right-aligns the text in a field of the given length.
    """
    try:
        text: str = input("Podaj dowolny napis: ")
        length: int = int(input("Podaj długość pola: "))
        right_aligned_text: str = text.rjust(length)
        print(right_aligned_text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
