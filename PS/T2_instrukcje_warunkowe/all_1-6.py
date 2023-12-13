"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 2: Instrukcje Warunkowe

    ? Zadanie 1.
        Napisz program, który wyznaczy ocenę na podstawie punktów zdobytych za
        kolokwium według następujących reguł:
        0-10 pkt, ocena 2
        11-13 pkt, ocena 3
        14-16 pkt, ocena 4
        17-20 pkt, ocena 5
        Program powinien przyjmować z konsoli liczbę punktów w formie liczby całkowitej, a
        następnie wyświetlać ocenę.

    ? Zadanie 2.
        Napisz program wyznaczający rzeczywiste pierwiastki równania kwadratowego.
        Program ma oczekiwać od użytkownika podania współczynników a, b i c, a następnie
        wyświetlić informację słowną o liczbie pierwiastków rzeczywistych (“brak”, “jeden”,
        “dwa” oraz wartości wyliczonych pierwiastków.

    ? Zadanie 3.
        Napisz program, który obliczy koszt brutto zużytej energii elektrycznej, zgodnie z
        cennikiem:
        • 0.50 zł netto za pierwsze 50 kWh,
        • 0.75 zł netto za następne 100 kWh,
        • 1.20 zł netto za następne 100 kWh,
        • 1.50 zł netto za każdą kWh powyżej 250.
        Kwota netto to kwota bez podatku VAT. Kwota brutto to kwota netto powiększona o wartość
        podatku VAT. W programie należy przyjąć stawkę VAT równą 22% kwoty podstawowej
        (netto).
        Program powinien pobrać od użytkownika ilość zużytej energii, a następnie obliczyć i
        wyświetlić jej koszt brutto.

    ? Zadanie 4.
        Napisz program, który pobierze od użytkownika dwie liczby, a następnie sprawdzi czy
        pierwsza jest podzielna przez drugą. W przypadku podania błędnych danych przez
        użytkownika program powinien wyświetlić komunikat „Incorrect input”.

    ? Zadanie 5.
        Napisz program, który pobiera od użytkownika 5 liter. W przypadku gdy pobrana
        litera jest mała zamień ją na wielką, a następnie wyświetl. Jeśli litera jest wielka
        wyświetl ją bez zamiany.

    ? Zadanie 6.
        Napisz program, który pobierze od użytkownika pozycję pola na szachownicy, a
        następnie wyświetli komunikat "white" jeżeli pole jest białe lub "black" jeżeli kolor
        pola jest czarny. W przypadku podania błędnych danych program powinien
        wyświetlić komunikat "Incorrect input”.  Np. pole a2 -  white.

    ! NOTATKA:
        Funkcje pełnią więcej niż jedną rolę, ponieważ były pisane z myślą, że każda to osobny program.
        W celu szybszego manualnego testowania, funkcje zostały połączone w jeden program, który pozwala wybrać zadanie do samodzielnego przetestowania.
"""


from os import system, name
from msvcrt import getch


def calculate_grade() -> None:
    """
        ? Zadanie 1.
            Napisz program, który wyznaczy ocenę na podstawie punktów zdobytych za
            kolokwium według następujących reguł:
            0-10 pkt, ocena 2
            11-13 pkt, ocena 3
            14-16 pkt, ocena 4
            17-20 pkt, ocena 5
            Program powinien przyjmować z konsoli liczbę punktów w formie liczby całkowitej, a
            następnie wyświetlać ocenę.

        * This function asks the user to enter the number of points scored for the exam in the form of an integer, and then calculates and displays the grade according to the specified rules.
    """
    try:
        points: int = int(
            input("Podaj liczbę punktów zdobytych za kolokwium: "))
        if points >= 0:
            if points <= 10:
                grade: int = 2
            elif points <= 13:
                grade: int = 3
            elif points <= 16:
                grade: int = 4
            elif points <= 20:
                grade: int = 5
            else:
                print(
                    "Niepoprawna liczba punktów. Punkty powinny być w zakresie od 0 do 20.")
                return
        else:
            print(
                "Niepoprawna liczba punktów. Punkty powinny być w zakresie od 0 do 20.")
            return
        print(f"Ocena za kolokwium wynosi: {grade}")
    except ValueError:
        print("Incorrect input, please enter an integer.")
    except KeyboardInterrupt:
        print("Program interrupted by the user.")


def calculate_roots() -> None:
    """
        ? Zadanie 2.
            Napisz program wyznaczający rzeczywiste pierwiastki równania kwadratowego.
            Program ma oczekiwać od użytkownika podania współczynników a, b i c, a następnie
            wyświetlić informację słowną o liczbie pierwiastków rzeczywistych (“brak”, “jeden”,
            “dwa” oraz wartości wyliczonych pierwiastków.

        * This function asks the user to enter the coefficients a, b and c of a quadratic equation, then calculates and displays the real roots of the equation, if they exist.

        ! Podziękowania dla dr inż. Dariusza Brzezińskiego
    """
    try:
        a: float = float(input("Podaj współczynnik a: "))
        b: float = float(input("Podaj współczynnik b: "))
        c: float = float(input("Podaj współczynnik c: "))
        eps: float = 1e-6  # 1e-15

        if abs(a) < eps:
            print("To nie jest równanie kwadratowe.")
        else:
            delta: float = b**2 - 4*a*c

            if abs(delta) < eps:
                x: float = -b / (2*a)
                print(
                    f"Jest jeden pierwiastek rzeczywisty: {format(x, '.15g')}")
            elif delta > 0:
                if b > 0:
                    x1: float = (-b - delta**0.5) / (2*a)
                    x2: float = c / (a * x1)
                else:
                    x2: float = (-b + delta**0.5) / (2*a)
                    x1: float = c / (a * x2)
                print(
                    f"Są dwa pierwiastki rzeczywiste: {format(x1, '.15g')} i {format(x2, '.15g')}")
            else:
                print("Brak pierwiastków rzeczywistych.")
    except ValueError:
        print("Incorrect input, please enter a number.")
    except KeyboardInterrupt:
        print("Program interrupted by the user.")


def calculate_electricity_cost() -> None:
    """
        ? Zadanie 3.
            Napisz program, który obliczy koszt brutto zużytej energii elektrycznej, zgodnie z
            cennikiem:
            • 0.50 zł netto za pierwsze 50 kWh,
            • 0.75 zł netto za następne 100 kWh,
            • 1.20 zł netto za następne 100 kWh,
            • 1.50 zł netto za każdą kWh powyżej 250.
            Kwota netto to kwota bez podatku VAT. Kwota brutto to kwota netto powiększona o wartość
            podatku VAT. W programie należy przyjąć stawkę VAT równą 22% kwoty podstawowej
            (netto).
            Program powinien pobrać od użytkownika ilość zużytej energii, a następnie obliczyć i
            wyświetlić jej koszt brutto.

        * This function asks the user for the amount of electricity used, then calculates and displays the gross cost of the electricity used.
    """
    try:
        energy: float = float(input("Podaj ilość zużytej energii w kWh: "))
        vat: float = 0.22

        # if energy <= 50:
        #     cost: float = energy * 0.50
        # elif energy <= 150:
        #     cost: float = 50 * 0.50 + (energy - 50) * 0.75
        # elif energy <= 250:
        #     cost: float = 50 * 0.50 + 100 * 0.75 + (energy - 150) * 1.20
        # else:
        #     cost: float = 50 * 0.50 + 100 * 0.75 + \
        #         100 * 1.20 + (energy - 250) * 1.50

        # Bardziej zwięźle i czytelnie:
        cost: float = min(50, energy) * 0.50  # 50 * 0.50 lub energy * 0.50
        energy -= 50  # Zmnejszenie dla wygody liczenia dalej

        if energy > 0:
            cost += min(100, energy) * 0.75
            energy -= 100

        if energy > 0:
            cost += min(100, energy) * 1.20
            energy -= 100

        if energy > 0:
            cost += energy * 1.50

        cost += cost * vat
        print(f"Koszt brutto zużytej energii wynosi: {format(cost, '.2g')} zł")
        # print(f"Koszt brutto zużytej energii wynosi: {format(cost, '.6g')} zł")
        # print(f"Koszt brutto zużytej energii wynosi: {cost} zł")
    except ValueError:
        print("Incorrect input, please enter a number.")
    except KeyboardInterrupt:
        print("Program interrupted by the user.")


def check_divisibility() -> None:
    """
        ? Zadanie 4.
            Napisz program, który pobierze od użytkownika dwie liczby, a następnie sprawdzi czy
            pierwsza jest podzielna przez drugą. W przypadku podania błędnych danych przez
            użytkownika program powinien wyświetlić komunikat „Incorrect input”.

        * This function asks the user for two numbers, then checks if the first one is divisible by the second one.
    """
    try:
        num_a: float = float(input("Podaj pierwszą liczbę: "))
        num_b: float = float(input("Podaj drugą liczbę: "))

        if num_b == 0:
            print("Nie można dzielić przez zero.")
        elif num_a % num_b == 0:
            print(
                f"Liczba {format(num_a, '.6g')} jest podzielna przez {format(num_b, '.6g')}")
        else:
            print(
                f"Liczba {format(num_a, '.6g')} nie jest podzielna przez {format(num_b, '.6g')}")
    except ValueError:
        # print("Incorrect input, please enter a number.")
        print("Incorrect input")
    except KeyboardInterrupt:
        print("Program interrupted by the user.")


def convert_letters() -> None:
    """
        ? Zadanie 5.
            Napisz program, który pobiera od użytkownika 5 liter. W przypadku gdy pobrana
            litera jest mała zamień ją na wielką, a następnie wyświetl. Jeśli litera jest wielka
            wyświetl ją bez zamiany.

        * This function asks the user for 5 letters. If the letter is lowercase, it is converted to uppercase, otherwise it is displayed without conversion.
    """
    try:
        for _ in range(5):
            letter: str = input("Podaj literę: ")
            if not letter.isalpha() or len(letter) != 1:
                print("Niepoprawne dane, proszę podać pojedynczą literę.")
                continue
            print(letter.upper())
    except KeyboardInterrupt:
        print("Program interrupted by the user.")


def get_chessboard_color(column: str, row: int) -> str:
    if column < 'a' or column > 'h' or row < 1 or row > 8:
        return "Incorrect input"
    return "black" if (ord(column) - ord('a') + row) % 2 else "white"


def check_chessboard() -> None:
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


def main() -> None:
    """
        * This function displays the menu and allows the user to choose a task.
    """

    while True:
        if name == "nt":
            system("cls")
        else:
            system("clear")
        print("╔══════════ Temat 2: Instrukcje Warunkowe ══════════╗")
        print("  1. Zadanie - Ocena za kolokwium")
        print("  2. Zadanie - Pierwiastki równania kwadratowego")
        print("  3. Zadanie - Koszt zużytej energii elektrycznej")
        print("  4. Zadanie - Sprawdzenie podzielności")
        print("  5. Zadanie - Konwersja liter")
        print("  6. Zadanie - Kolor pola na szachownicy")
        print("  0. Wyjście\n")
        print("╚═════════════════ Wybierz zadanie: ════════════════╝")
        user_choice: str = input(">>> ")
        if user_choice == '0':
            break
        elif user_choice == '1':
            calculate_grade()
            print("\nKoniec zadania 1")
        elif user_choice == '2':
            calculate_roots()
            print("\nKoniec zadania 2")
        elif user_choice == '3':
            calculate_electricity_cost()
            print("\nKoniec zadania 3")
        elif user_choice == '4':
            check_divisibility()
            print("\nKoniec zadania 4")
        elif user_choice == '5':
            convert_letters()
            print("\nKoniec zadania 5")
        elif user_choice == '6':
            check_chessboard()
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
