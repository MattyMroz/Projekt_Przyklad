"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 4: Stringi
"""


def main() -> None:
    """
        ? Zadanie 6.
            W słowie DOM wyświetl literę znajdującą się najdalej i najbliżej w alfabecie.

        * This function displays the letter in the word DOM that is furthest and closest in the alphabet.
    """
    word: str = "DOM"
    sorted_word: str = sorted(word)
    print(f"Najbliżej w alfabecie: {sorted_word[0]}")
    print(f"Najdalej w alfabecie: {sorted_word[-1]}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
