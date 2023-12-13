"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 4: Stringi
"""


def main() -> None:
    """
        ? Zadanie 5.
            Zamień słowo DOM na DOMEK.

        * This function replaces the word DOM with DOMEK.
    """
    word: str = "DOM"
    print(word)
    replaced_word: str = word.replace("DOM", "DOMEK")
    print(replaced_word)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
