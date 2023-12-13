"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 7.2: Funkcje

    ? Zadanie 1.
        Napisz program do obliczenia odległości edycji między dwoma podanymi ciągami.
        Odległość edycji między dwoma ciągami odnosi się do minimalnej liczby wstawień, usunięć i podstawień znaków wymaganych do zamiany jednego ciągu na drugi. Na przykład odległość edycji między „kotkiem” a „siedzącym” wynosi trzy: zamień „k” na „s”, zamień „e” na „i” i dodaj „g”.

    ? Zadanie 2.
        Napisz program do generowania (z podaniem liczby całkowitej n) kwadratowej macierzy wypełnionej elementami od 1 do n2 w kolejności spiralnej.

    ? Zadanie 3.
        Napisz program który porówna dwie listy w sposób pokazany na rysunku.

    ? Zadanie 4.
        Napisz funkcję która sprawdzi czy dane liczby zawierają sekwencję addytywną, czy nie.

    ? Zadanie 5.
        Napisz program, aby znaleźć pierwszy numer trójkąta, który ma ponad n (podanych) dzielników.
        Liczba trójkątna to liczba, która jest sumą wszystkich liczb naturalnych do określonej liczby. Na przykład 10 jest liczbą trójkątną, ponieważ 1 + 2 + 3 + 4 = 10. Pierwsze 25 liczb trójkątnych to: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325 i 351.
        Liczbę trójkątną oblicza się za pomocą równania: n (n + 1) / 2

        Czynniki pierwszych pięciu liczb trójkątów:
        1: 1
        3: 1, 3
        6: 1, 2, 3, 6
        10: 1, 2, 5, 10
        15: 1, 3, 5, 15
        Na powyższej liście 6 jest pierwszym numerem trójkąta mającym ponad cztery dzielniki.


    ? Zadanie 6.
        Napisz program, aby znaleźć największy palindrom utworzony z iloczynu dwóch 4-cyfrowych liczb.
        Liczba palindromiczna lub palindrom liczbowy to liczba, która pozostaje taka sama, gdy jej cyfry zostaną odwrócone. Na przykład, podobnie jak 16461, jest „symetryczny”. Termin palindromic pochodzi od palindromu, który odnosi się do słowa (takiego jak rotor lub samochód wyścigowy), którego pisownia nie zmienia się, gdy jego litery są odwrócone. Pierwsze 30 liczb palindromowych (dziesiętnych) to: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101 , 111, 121, 131, 141, 151, 161, 171, 181, 191, 202,...

        Największy palindrom utworzony z iloczynu dwóch trzycyfrowych liczb to 913 * 993 = 906609.
        Uwaga: 9999 * 9901 = 99000099


    ! NOTATKA:
        Funkcje pełnią więcej niż jedną rolę, ponieważ były pisane z myślą, że każda to osobny program.
        W celu szybszego manualnego testowania, funkcje zostały połączone w jeden program, który pozwala wybrać zadanie do samodzielnego przetestowania.
"""

from os import system, name
from msvcrt import getch


def calculate_edit_distance() -> None:
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


def generate_spiral_matrix() -> None:
    """
        ? Zadanie 2.
            Napisz program do generowania (z podaniem liczby całkowitej n) kwadratowej macierzy wypełnionej elementami od 1 do n2 w kolejności spiralnej.

        * This function generates a square matrix filled with elements from 1 to n^2 in a spiral order.
    """
    try:
        n: int = int(input("Podaj liczbę całkowitą n: "))
        dx, dy = 0, 1
        x, y = 0, 0
        matrix: list = [[None]*n for _ in range(n)]  # Inicjalizacja macierzy
        for i in range(1, n**2+1):  # Dla każdego elementu od 1 do n^2
            matrix[x][y] = i  # Wypełniamy macierz
            nx, ny = x+dx, y+dy  # Obliczamy następny element
            # Jeśli potencjalny następny element jest w macierzy i jest pusty
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == None:
                x, y = nx, ny  # To przesuwamy się do niego
            else:
                # W przeciwnym razie zmieniamy kierunek i przesuwamy się o jeden element w nowym kierunku
                dx, dy = dy, -dx  # Obrót o 90 stopni w prawo
                x, y = x+dx, y+dy

        for x in matrix:
            for y in x:
                print(y, end=' ')
            print()

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def compare_lists() -> None:
    """
        ? Zadanie 3.
            Napisz program który porówna dwie listy w sposób pokazany na rysunku.
            Czy dwie listy są cyklicznie identyczne?

        * This function compares two lists in the way shown in the picture.

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


def check_additive_sequence() -> None:
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


def find_triangle_number() -> None:
    """
        ? Zadanie 5.
            Napisz program, aby znaleźć pierwszy numer trójkąta, który ma ponad n (podanych) dzielników.

        * This function finds the first triangle number that has more than n (given) divisors.
    """
    try:
        n: int = int(input("Podaj liczbę dzielników n: "))

        def divisors(n):
            """
                * Zwraca liczbę dzielników danej liczby.
            """
            i = 1
            divisors = 0
            while i <= n**0.5:
                if n % i == 0:
                    if n / i == i:
                        divisors += 1
                    else:
                        divisors += 2
                i += 1
            return divisors

        i = 1
        while True:
            triangle_number = i*(i+1)//2
            if divisors(triangle_number) > n:
                print(
                    "Pierwszy numer trójkąta, który ma ponad n dzielników to: ", triangle_number)
                break
            i += 1
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def find_largest_palindrome() -> None:
    """
        ? Zadanie 6.
            Napisz program, aby znaleźć największy palindrom utworzony z iloczynu dwóch 4-cyfrowych liczb.

        * This function finds the largest palindrome made from the product of two 4-digit numbers.
    """
    try:
        def is_palindrome(n):
            return str(n) == str(n)[::-1]

        max_palindrome = 0
        # W przeciwieństwie do tematu 7.1 zaczynamy od końca, wychodzi na to samo (*_*)
        for i in range(9999, 999, -1):
            for j in range(i, 999, -1):
                if is_palindrome(i*j) and i*j > max_palindrome:
                    max_palindrome = i*j
        print("Największy palindrom utworzony z iloczynu dwóch 4-cyfrowych liczb to: ", max_palindrome)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main() -> None:
    """
        * This function displays the menu and allows the user to choose a task.
    """

    while True:
        if name == "nt":
            system("cls")
        else:
            system("clear")
        print("╔═════════════════ Temat 7.2: Funkcje ═════════════════╗")
        print("  1. Zadanie - Odległość edycji")
        print("  2. Zadanie - Macierz spiralna")
        print("  3. Zadanie - Czy dwie listy są cyklicznie identyczne?")
        print("  4. Zadanie - Sprawdzenie, czy liczby zawierają sekwencję addytywną")
        print("  5. Zadanie - Pierwszy numer trójkąta, który ma ponad n dzielników")
        print("  6. Zadanie - Największy palindrom utworzony z iloczynu dwóch 4-cyfrowych liczb")
        print("  0. Wyjście\n")
        print("╚════════════════ Wybierz zadanie: ════════════════════╝")
        user_choice: str = input(">>> ")
        if user_choice == '0':
            break
        elif user_choice == '1':
            calculate_edit_distance()
            print("\nKoniec zadania 1")
        elif user_choice == '2':
            generate_spiral_matrix()
            print("\nKoniec zadania 2")
        elif user_choice == '3':
            compare_lists()
            print("\nKoniec zadania 3")
        elif user_choice == '4':
            check_additive_sequence()
            print("\nKoniec zadania 4")
        elif user_choice == '5':
            find_triangle_number()
            print("\nKoniec zadania 5")
        elif user_choice == '6':
            print("\nZadanie 6 może chwilę potrwać...")
            find_largest_palindrome()
            print("\nKoniec zadania 6")
        else:
            print("\nNiepoprawny wybór. Spróbuj ponownie.")

        print("\nNaciśnij dowolny klawisz, aby kontynuować...", end='')
        getch()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
