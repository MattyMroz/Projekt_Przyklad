"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 4: Stringi
"""


def main() -> None:
    """
        ? Zadanie 3.
            Zmodyfikuj  zdanie  z  poprzedniego  zadania  tak,  aby  każde  słowo  było oddzielone przecinkiem.

        * This function modifies the sentence from the previous task so that each word is separated by a comma.
    """
    sentence: str = "Ala ma 2 koty"
    modified_sentence: str = ", ".join(sentence.split())
    print(modified_sentence)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
