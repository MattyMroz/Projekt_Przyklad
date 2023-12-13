"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 3: Stringi
"""


def main() -> None:
    """
        ? Zadanie 4.
            Wyświetl zdanie z poprzedniego zadania tak, by każde słowo znajdowało się w osobnej linijce.

        * This function displays the sentence from the previous task so that each word is on a separate line.
    """
    sentence: str = "Ala, ma, 2, koty"
    for word in sentence.split(", "):
        print(word)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
