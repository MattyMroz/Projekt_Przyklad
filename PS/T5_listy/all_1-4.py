"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 5: Listy

    ? Zadanie 1.
        Napisz komendę w środowisku Python, która zamieni wartość x='Ala ma Asa' wspak.

    ? Zadanie 2.
        Napisz program, który wypisze listę wszystkich indeksów w łańcuchu x, na których zaczyna się podłańcuch s.

    ? Zadanie 3.
        Napisz program, który obliczy największy wspólny dzielnik liczb zapisanych w zmiennych a, b, wykorzystując algorytm Euklidesa.

    ? Zadanie 4.
        Dane są wyniki losowania w pewnej grze liczbowej: wynik=[12,1,45,76,50,23]
        Wiedząc, że wylosowane wartości mogą zawierać się w przedziale od 1 do 49 zastąp występujące w liście liczby nie spełniające tego kryterium na takie, które będą je spełniać.


    ! NOTATKA:
        Funkcje pełnią więcej niż jedną rolę, ponieważ były pisane z myślą, że każda to osobny program.
        W celu szybszego manualnego testowania, funkcje zostały połączone w jeden program, który pozwala wybrać zadanie do samodzielnego przetestowania.
"""


from os import system, name
from msvcrt import getch


def reverse_string() -> None:
    """
        ? Zadanie 1.
            Napisz komendę w środowisku Python, która zamieni wartość x='Ala ma Asa' wspak.

        * This function reverses the string 'Ala ma Asa'.
    """
    try:
        x: str = 'Ala ma Asa'
        reversed_x: str = x[::-1]
        print(reversed_x)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def find_substring_indices() -> None:
    """
        ? Zadanie 2.
            Napisz program, który wypisze listę wszystkich indeksów w łańcuchu x, na których zaczyna się podłańcuch s.

        * This function prints a list of all indices in the string x where the substring s begins.
    """
    try:
        x: str = input("Podaj łańcuch znaków: ")
        s: str = input("Podaj podłańcuch: ")
        indices: list = [i for i in range(len(x)) if x.startswith(s, i)]
        print(indices)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def calculate_gcd() -> None:
    """
        ? Zadanie 3.
            Napisz program, który obliczy największy wspólny dzielnik liczb zapisanych w zmiennych a, b, wykorzystując algorytm Euklidesa.

        * This function calculates the greatest common divisor of the numbers stored in variables a and b using the Euclidean algorithm.
    """
    try:
        a: int = int(input("Podaj pierwszą liczbę: "))
        b: int = int(input("Podaj drugą liczbę: "))
        while b != 0:
            a, b = b, a % b
        print(f"Największy wspólny dzielnik: {a}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def replace_out_of_range_numbers() -> None:
    """
        ? Zadanie 4.
            Dane są wyniki losowania w pewnej grze liczbowej: wynik=[12,1,45,76,50,23]
            Wiedząc, że wylosowane wartości mogą zawierać się w przedziale od 1 do 49 zastąp występujące w liście liczby nie spełniające tego kryterium na takie, które będą je spełniać.

        * This function replaces the numbers in the list that do not meet the criterion of being in the range from 1 to 49 with numbers that meet this criterion.
    """
    try:
        result: list = [12, 1, 45, 76, 50, 23]
        for i in range(len(result)):
            if not 1 <= result[i] <= 49:
                result[i] = 1 if result[i] < 1 else 49
        print(result)
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
        print("╔═════════════════ Temat 5: Listy ═════════════════╗")
        print("  1. Zadanie - Odwróć łańcuch znaków")
        print("  2. Zadanie - Wypisz indeksy podłańcucha")
        print("  3. Zadanie - Oblicz NWD")
        print("  4. Zadanie - Zastąp liczby spoza zakresu")
        print("  0. Wyjście\n")
        print("╚════════════════ Wybierz zadanie: ════════════════╝")
        user_choice: str = input(">>> ")
        if user_choice == '0':
            break
        elif user_choice == '1':
            reverse_string()
            print("\nKoniec zadania 1")
        elif user_choice == '2':
            find_substring_indices()
            print("\nKoniec zadania 2")
        elif user_choice == '3':
            calculate_gcd()
            print("\nKoniec zadania 3")
        elif user_choice == '4':
            replace_out_of_range_numbers()
            print("\nKoniec zadania 4")
        else:
            print("\nNiepoprawny wybór. Spróbuj ponownie.")

        print("\nNaciśnij dowolny klawisz, aby kontynuować...", end='')
        getch()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
