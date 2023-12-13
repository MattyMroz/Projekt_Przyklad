"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 7.2: Funkcje
"""


def main() -> None:
    """
        ? Zadanie 4.
            Napisz funkcję która sprawdzi czy dane liczby zawierają sekwencję addytywną, czy nie.

        * This function checks whether the given numbers contain an additive sequence or not.

        ! NOTATKA:
        Największym wyzwaniem było zaprogramowanie sekwencyjnego sprawdzania, czy suma dwóch liczb jest równa kolejnemu segmentowi sekwencji, który zaczyna się od indeksu następującego po ostatniej cyfrze drugiego składnika sumy (*_*)

        # 66121830
        # 6 6 12 18 30
        # 6 + 6 = 12
        # 6 + 12 = 18
        # 12 + 18 = 30
    """
    try:
        sequence: str = input("Podaj sekwencję liczb: ")
        num_a: str = sequence[0]
        num_b: str = sequence[1]
        i = 2

        while i < len(sequence):  # Dopuki i jest mniejsze od długości sekwencji
            sum: str = str(int(num_a) + int(num_b))  # Obliczamy sumę
            # Jeśli suma jest równa kolejnym elementom sekwencji
            if sequence[i:i+len(sum)] == sum:
                num_a, num_b = num_b, sum  # To przesuwamy się o dwa elementy
                i += len(sum)
            else:
                print("Sekwencja nie jest addytywna.")
                return

        print("Sekwencja jest addytywna.")
    except Exception as e:
        print(f"Wystąpił błąd: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
