"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 7.2: Funkcje
"""


def main() -> None:
    """
        ? Zadanie 1.
            Napisz program do obliczenia odległości edycji między dwoma podanymi ciągami.

        * This function calculates the edit distance between two given strings.

        ! NOTATKA:
        1) Np.: 2 słowa: mati i kun

        1. Najpierw tworzymy macierz o wymiarach (len("mati") + 1) x (len("kun") + 1), czyli 5x4.
        2. Inicjalizujemy ją zerami.
        3. Inicjalizujemy pierwszy wiersz i pierwszą kolumnę od 0 do len("mati") i len("kun") odpowiednio od 0 do 4 i 0 do 3

        Stan macierzy po inicjalizacji:
        0 1 2 3
        1 0 0 0
        2 0 0 0
        3 0 0 0
        4 0 0 0

        4. Przechodzimy przez resztę macierzy, wypełniając każdą komórkę

        - Dla komórki (1,1) porównujemy "m" z "k". Ponieważ są różne, bierzemy minimum z komórek (0,0), (0,1) i (1,0) i dodajemy 1. Otrzymujemy 1.

        - Dla komórki (1,2) porównujemy "m" z "u". Ponieważ są różne, bierzemy minimum z komórek (0,1), (0,2) i (1,1) i dodajemy 1. Otrzymujemy 2.

        - Kontynuujemy ten proces dla reszty macierzy.

        5. Odległość edycji wynosi 4, co znajduje się w komórce (4,3).


        2) Tablice dla przykłądu mati i mat

        Inicjalizacja:
        0 1 2 3
        1 0 0 0
        2 0 0 0
        3 0 0 0
        4 0 0 0

        - Ponieważ (1,1) czyli "m" i "m" są takie same, bierzemy minimum z komórek (0,0), (0,1) i (1,0) i dodajemy 0. Otrzymujemy 0.

        - Dla (1,2) porównujemy "m" z "a". Ponieważ są różne, bierzemy minimum z komórek (0,1), (0,2) i (1,1) i dodajemy 1. Otrzymujemy 1.
        Kontunuujemy ten proces dla reszty macierzy.

        Końcowa wersja:
        0 1 2 3
        1 0 1 2
        2 1 0 1
        3 2 1 1
        4 3 2 2
    """
    try:
        string_a: str = input("Podaj pierwszy ciąg: ")
        string_b: str = input("Podaj drugi ciąg: ")

        size_x: int = len(string_a) + 1
        size_y: int = len(string_b) + 1
        matrix: list = [[0 for _ in range(size_y)]
                        for _ in range(size_x)]  # Wypełnienie zerami
        # print(matrix)
        for x in range(size_x):
            matrix[x][0] = x
        # print(matrix)
        for y in range(size_y):
            matrix[0][y] = y
        # print(matrix)

        for x in range(1, size_x):  # 1, 2, 3, ..., size_x - 1
            for y in range(1, size_y):  # 1, 2, 3, ..., size_y - 1
                if string_a[x-1] == string_b[y-1]:  # x-1, y-1, bo indeksujemy od 0
                    matrix[x][y] = min(  # min zwraca najmniejszą wartość z podanych
                        matrix[x-1][y] + 1,
                        matrix[x-1][y-1],
                        matrix[x][y-1] + 1
                    )
                else:
                    matrix[x][y] = min(
                        matrix[x-1][y] + 1,
                        matrix[x-1][y-1] + 1,  # zamiana
                        matrix[x][y-1] + 1
                    )

        # print(matrix)

        print("Odległość edycji to: ", matrix[size_x - 1][size_y - 1])
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
