"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 8

    ? Zadanie 1.
        Napisz program, aby znaleźć produkt xyz używając trójki pitagorajskiej
        Pitagorejska trójka składa się z trzech dodatnich liczb całkowitych a, b i c, takich, że a2 + b2 = c2. Taki potrójny jest powszechnie pisany (a, b, c), a dobrze znanym przykładem jest (3, 4, 5). Istnieje dokładnie jedna tripleta pitagorejska, dla której x + y + z = 1000.

    ? Zadanie 2.
        Napisz program, aby znaleźć pierwszy numer trójkąta, który ma ponad n (podanych) dzielników.
        Liczba trójkątna to liczba, która jest sumą wszystkich liczb naturalnych do określonej liczby. Na przykład 10 jest liczbą trójkątną, ponieważ 1 + 2 + 3 + 4 = 10. Pierwsze 25 liczb trójkątnych to: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325 i 351. Liczbę trójkątną oblicza się za pomocą równania: n (n + 1) / 2 Czynniki pierwszych pięciu liczb trójkątów: 1: 1 3: 1, 3 6: 1, 2, 3, 6 10: 1, 2, 5, 10 15: 1, 3, 5, 15 Na powyższej liście 6 jest pierwszym numerem trójkąta mającym ponad cztery dzielniki.

    ? Zadanie 3.
        Napisz program, aby znaleźć numer początkowy, poniżej dziesięciu tysięcy stworzy najdłuższy łańcuch.
        Hipoteza Collatza to hipoteza w matematyce, która dotyczy sekwencji zdefiniowanej w następujący sposób: zacznij od dowolnej dodatniej liczby całkowitej n. Następnie każdy termin jest uzyskiwany z poprzedniego terminu w następujący sposób: jeśli poprzedni termin jest parzysty, następny termin to połowa poprzedniego terminu. Jeśli poprzedni termin jest nieparzysty, następny jest trzy razy większy od poprzedniego plus 1. Przypuszczenie jest takie, że bez względu na wartość n, sekwencja zawsze osiągnie 1.

    ? Zadanie 4.
        Napisz program do obliczenia sumy cyfr liczby 220.

    ? Zadanie 5.
        Napisz program, aby znaleźć maksymalną sumę od góry do dołu trójkąta pokazanego poniżej.
        Rozpoczynając od góry trójkąta poniżej i przechodząc do sąsiednich liczb w rzędzie poniżej, maksymalna suma od góry do dołu wynosi 25.

    ? Zadanie 6.
        Napisz program, który pobiera ciąg znaków i koduje go tak, aby liczba symboli była reprezentowana przez liczbę całkowitą i symbol.
        Na przykład ciąg „AAAABBBCCDAAA” byłby zakodowany jako „4A3B2C1D3A”


    ! NOTATKA:
        Funkcje pełnią więcej niż jedną rolę, ponieważ były pisane z myślą, że każda to osobny program.
        W celu szybszego manualnego testowania, funkcje zostały połączone w jeden program, który pozwala wybrać zadanie do samodzielnego przetestowania.
"""

from os import system, name
from msvcrt import getch


def find_pythagorean_triplet() -> None:
    """
        ? Zadanie 1.
            Napisz program, aby znaleźć produkt xyz używając trójki pitagorajskiej

        * This function finds the product xyz using a Pythagorean triplet for which x + y + z = 1000.
    """
    for x in range(1, 1000):
        for y in range(x, 1000):
            z: int = 1000 - x - y
            if x * x + y * y == z * z:
                # print(f"Trójka pitagorejska: {x}, {y}, {z}") # 200, 375, 425
                print(f"Produkt xyz: {x*y*z}")
                return


def find_triangle_number() -> None:
    """
        ? Zadanie 2.
            Napisz program, aby znaleźć pierwszy numer trójkąta, który ma ponad n (podanych) dzielników.

        * This function finds the first triangle number that has more than n (given) divisors.
    """
    try:
        n: int = int(input("Podaj liczbę dzielników n: "))

        def divisors(n):
            """
                * Zwraca liczbę dzielników danej liczby.
            """
            i: int = 1
            divisors: int = 0
            while i <= n**0.5:
                if n % i == 0:
                    if n / i == i:
                        divisors += 1
                    else:
                        divisors += 2
                i += 1
            return divisors

        i: int = 1
        while True:
            triangle_number = i*(i+1)//2
            if divisors(triangle_number) > n:
                print(
                    f"Pierwszy numer trójkąta, który ma ponad {n} dzielników to: {triangle_number}")
                break
            i += 1
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def find_longest_chain() -> None:
    """
        ? Zadanie 3.
            Napisz program, aby znaleźć numer początkowy, poniżej dziesięciu tysięcy stworzy najdłuższy łańcuch.

        * This function finds the starting number, under ten thousand, that produces the longest chain according to the Collatz hypothesis.
    """
    def collatz_chain_length(n: int) -> int:
        length: int = 1
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            length += 1
        return length

    max_length: int = 0
    max_start: int = 0
    for i in range(1, 10000):
        length = collatz_chain_length(i)
        if length > max_length:
            max_length = length
            max_start = i
    print(
        f"Numer początkowy, poniżej dziesięciu tysięcy, który tworzy najdłuższy łańcuch: {max_start}")


def calculate_sum_of_digits() -> None:
    """
        ? Zadanie 4.
            Napisz program do obliczenia sumy cyfr liczby 2^20.

        * This function calculates the sum of the digits of the number 2^20.
    """
    number = 2**20
    digit_sum = sum(int(digit) for digit in str(number))
    print(f"Suma cyfr liczby 2^20: {digit_sum}")


def find_max_sum() -> None:
    """
        ? Zadanie 5.
            Napisz program, aby znaleźć maksymalną sumę od góry do dołu trójkąta pokazanego poniżej.

        * This function finds the maximum sum from top to bottom of the triangle shown below.

        ! NOTATKA:
        [3],
        [4, 6],
        [2, 7, 6],
        [8, 5, 9, 3] <- tu zanczymay

        np dla 2 bierzemt max(8, 5) i dodajemy do 2 => 10
        np dla 7 bierzemy max(5, 9) i dodajemy do 7 => 16
        np  dla 6 bierzemy max(9, 3) i dodajemy do 6 => 15
        [3],
        [4, 6],
        [10, 16, 15], <- tu zanczymay
        [8, 5, 9, 3]

        [25], <- wynik
        [20, 21], <- tu zanczymay
        [10, 16, 15],
        [8, 5, 9, 3]
    """
    triangle: list = [
        # [3],
        # [4, 6],
        # [2, 7, 6],
        # [8, 5, 9, 3]

        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
    ]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # print(
            #     f"{triangle[i][j]} + max({triangle[i+1][j]}, {triangle[i+1][j+1]})")
            # Maximum sumy dwóch sąsiednich liczb w kolejnym rzędzie
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

    print(f"Maksymalna suma od góry do dołu trójkąta: {triangle[0][0]}")


def encode_string() -> None:
    """
        ? Zadanie 6.
            Napisz program, który pobiera ciąg znaków i koduje go tak, aby liczba symboli była reprezentowana przez liczbę całkowitą i symbol.

        * This function takes a string and encodes it so that the number of symbols is represented by an integer and a symbol.
    """
    string: str = input("Podaj ciąg znaków do zakodowania: ")
    encoded_string: str = ""
    i: int = 0

    while i < len(string):
        count: int = 1
        # Dopóki sąsiednie znaki są takie same, zwiększamy licznik
        while i + 1 < len(string) and string[i] == string[i+1]:
            i += 1
            count += 1
        encoded_string += f"{count}{string[i]}"
        i += 1

    print(f"Zakodowany ciąg znaków: {encoded_string}")


def main() -> None:
    """
        * This function displays the menu and allows the user to choose a task.
    """

    while True:
        if name == "nt":
            system("cls")
        else:
            system("clear")
        print("╔══════════════════════ Temat 8 ═══════════════════════╗")
        print("  1. Zadanie - Trójka pitagorejska")
        print("  2. Zadanie - Pierwszy numer trójkąta, który ma ponad n dzielników")
        print("  3. Zadanie - Numer początkowy, poniżej dziesięciu tysięcy stworzy najdłuższy łańcuch")
        print("  4. Zadanie - Suma cyfr liczby 2^20")
        print("  5. Zadanie - Maksymalna suma od góry do dołu trójkąta")
        print("  6. Zadanie - Zakodowany ciąg znaków")
        print("  0. Wyjście\n")
        print("╚════════════════ Wybierz zadanie: ════════════════════╝")
        user_choice: str = input(">>> ")
        if user_choice == '0':
            break
        elif user_choice == '1':
            find_pythagorean_triplet()
            print("\nKoniec zadania 1")
        elif user_choice == '2':
            find_triangle_number()
            print("\nKoniec zadania 2")
        elif user_choice == '3':
            find_longest_chain()
            print("\nKoniec zadania 3")
        elif user_choice == '4':
            calculate_sum_of_digits()
            print("\nKoniec zadania 4")
        elif user_choice == '5':
            find_max_sum()
            print("\nKoniec zadania 5")
        elif user_choice == '6':
            encode_string()
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
