"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 7.2: Funkcje
"""


def main() -> None:
    """
        ? Zadanie 3.
            Napisz program który porówna dwie listy w sposób pokazany na rysunku.
            Czy dwie listy są cyklicznie identyczne?

        * This function compares two lists in the way shown in the picture - if two lists are cyclically identical.

        ! NOTATKA:
        Nie tak łatwo mnie zagiąć (*_*)
        list1 = [10, 10, 0, 0, 10]
        list2 = [10, 10, 10, 0, 0]
        list3 = [1, 10, 10, 0, 0]

        # Sprawdź, czy reprezentacja ciągu list2 jest obecna w reprezentacji ciągu list1 powtórzona dwa razy = True
        print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2))) => True

        # Sprawdź, czy reprezentacja ciągu list3 jest obecna w reprezentacji ciągu list1 powtórzona dwa razy = False
        print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2))) => False
    """
    try:
        list_a: list = list(
            map(int, input("Podaj elementy pierwszej listy oddzielone spacją: ").split()))
        list_b: list = list(
            map(int, input("Podaj elementy drugiej listy oddzielone spacją: ").split()))

        # Sprawdza, czy list_b jest podciągiem list_a
        is_subsequence = ' '.join(
            map(str, list_b)) in ' '.join(map(str, list_a * 2))

        if is_subsequence:
            print("Druga lista jest cyklicznie identyczna z pierwszą listą.")
        else:
            print("Druga lista nie jest cyklicznie identyczna z pierwszą listą.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
