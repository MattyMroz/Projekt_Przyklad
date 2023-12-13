"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 4: Stringi
"""


def main() -> None:
    """
        ? Zadanie 2.
            Wyświetl zdanie “Ala ma 2 koty” wykorzystując konwersję liczby 2.

        * This function displays the sentence "Ala ma 2 koty" using the conversion of the number 2.
    """
    number_of_cats: int = 2
    print(f"Ala ma {number_of_cats} koty")
    # print("Ala ma {} koty".format(number_of_cats))
    # print("Ala ma %d koty" % number_of_cats)
    # print("Ala ma", number_of_cats, "koty")
    # print("Ala ma " + str(number_of_cats) + " koty")
    # print("Ala ma", str(number_of_cats), "koty")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
