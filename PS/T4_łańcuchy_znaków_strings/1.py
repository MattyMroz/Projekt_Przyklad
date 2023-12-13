"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 4: Stringi
"""


def main() -> None:
    """
        ? Zadanie 1.
            Wyświetl  na  ekranie  dowolny  tekst,  który  ma  co  najmniej  siedem  znaków. Wyświetl liczbę znaków, które on zawiera. Wyświetl pierwszy i ostatni znak tego tekstu. Wyświetl 3 środkowe znaki tego tekstu.

        * This function asks the user for a text of at least seven characters, displays the number of characters it contains, the first and last character of this text, and the three middle characters of this text.
    """
    try:
        user_text: str = input(
            "Podaj dowolny tekst, który ma co najmniej siedem znaków: ")
        if len(user_text) < 7:
            print("Tekst jest za krótki. Spróbuj ponownie.")
        else:
            print(f"Liczba znaków: {len(user_text)}")
            print(f"Pierwszy znak: {user_text[0]}")
            print(f"Ostatni znak: {user_text[-1]}")
            middle_index: int = len(user_text) // 2
            print(
                f"Trzy środkowe znaki: {user_text[middle_index-1:middle_index+2]}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
