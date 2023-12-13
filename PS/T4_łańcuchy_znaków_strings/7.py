"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 4: Stringi
"""


def main() -> None:
    """
        ? Zadanie 7.
            W zdaniu “Ala ma 2 koty”:
            o sprawdź, czy wszystkie litery są małe, jeśli nie, to je zamień je na małe,
            o zmień pierwszą literę zdania na wielką.

        * This function checks if all the letters in the sentence "Ala ma 2 koty" are lowercase, if not, it changes them to lowercase, and then changes the first letter of the sentence to uppercase.
    """
    sentence: str = "Ala ma 2 koty"
    if not sentence.islower():
        sentence = sentence.lower()
    sentence = sentence.capitalize()
    print(sentence)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
