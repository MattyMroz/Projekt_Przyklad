"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 2: Instrukcje Warunkowe
"""


def get_chessboard_color(column: str, row: int) -> str:
    if column < 'a' or column > 'h' or row < 1 or row > 8:
        return "Incorrect input"
    return "black" if (ord(column) - ord('a') + row) % 2 else "white"


def main() -> None:
    """
        ? Zadanie 6.
            Napisz program, który pobierze od użytkownika pozycję pola na szachownicy, a
            następnie wyświetli komunikat "white" jeżeli pole jest białe lub "black" jeżeli kolor
            pola jest czarny. W przypadku podania błędnych danych program powinien
            wyświetlić komunikat "Incorrect input”.  Np. pole a2 -  white.

        * This function asks the user for the position of a field on the chessboard, then displays "white" if the field is white or "black" if the field is black.

        ! Podziękowania dla dr inż. Piotra Ducha - Dante 2.8 - Szachownica

        ! Notatki:
        Czarny, jeśli suma kolumny i wiersza jest parzysta

        8 a8 b8 c8 d8 e8 f8 g8 h8  ◻■◻■◻■◻■
        7 a7 b7 c7 d7 e7 f7 g7 h7  ■◻■◻■◻■◻
        6 a6 b6 c6 d6 e6 f6 g6 h6  ◻■◻■◻■◻■
        5 a5 b5 c5 d5 e5 f5 g5 h5  ■◻■◻■◻■◻
        4 a4 b4 c4 d4 e4 f4 g4 h4  ◻■◻■◻■◻■
        3 a3 b3 c3 d3 e3 f3 g3 h3  ■◻■◻■◻■◻
        2 a2 b2 c2 d2 e2 f2 g2 h2  ◻■◻■◻■◻■
        1 a1 b1 c1 d1 e1 f1 g1 h1  ■◻■◻■◻■◻
          a  b  c  d  e  f  g  h

        a1
        (column - 'a' + row) % 2)
        (('a' - 'a' + 1) % 2
        (0 + 1) % 2
        1 % 2
        1 -> true -> black

        a2
        (column - 'a' + row) % 2)
        (('a' - 'a' + 2) % 2
        (0 + 2) % 2
        2 % 2
        0 -> false -> white
    """
    try:
        position: str = input("Podaj pozycję pola na szachownicy: ")
        if len(position) != 2 or not position[0].isalpha() or not position[1].isdigit():
            print("Incorrect input")
            # print(
            #     "Incorrect input, please enter a valid chessboard position (e.g., 'a2').")
            return

        column: str = position[0].lower()
        row: int = int(position[1])
        print(get_chessboard_color(column, row))
    except ValueError:
        print("Incorrect input, please enter a valid chessboard position (e.g., 'a2').")
    except KeyboardInterrupt:
        print("Program interrupted by the user.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
