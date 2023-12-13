"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 1: Wprowadzanie i Wyświetlanie Danych

    ? Zadanie 1.
        Napisz program, który poprosi użytkownika o podanie liczby rzeczywistej x a następnie wyznaczy i wyświetli wartość następującego wielomianu: y=3x^3-5x^2+3x-7.

    ? Zadanie 2.
        Napisz prosty kalkulator dla liczb całkowitych. Program ma pobierać od użytkownika dwie wartości liczbowe, a następnie wyświetlić ich sumę, iloczyn, iloraz oraz różnicę. Program powinien prosić o każdą liczbę indywidualnie. Wyniki należy wyświetlić w osobnych wierszach, w następującej kolejności: suma, różnica, iloczyn, iloraz.

    ? Zadanie 3.
        Napisz prosty kalkulator dla liczb zespolonych. Program ma pobierać od użytkownika dwie wartości liczbowe, a następnie wyświetlić ich sumę, iloczyn, iloraz oraz różnicę. Program powinien prosić o każdą liczbę indywidualnie. Wyniki należy wyświetlić w osobnych wierszach, w następującej kolejności: suma, różnica, iloczyn, iloraz.

    ? Zadanie 4.
        Napisz program, pobierający od użytkownika współrzędne dwóch punktów na płaszczyźnie,  a następnie wyznaczający i wyświetlający odległość między tymi punktami.

    ? Zadanie 5.
        Napisz program, który dla podanej przez użytkownika temperatury w stopniach Celsjusza, wyświetli w osobnych wierszach temperaturę w Kelwinach i następnie stopniach Fahrenheita.

    ! NOTATKA:
        Funkcje pełnią więcej niż jedną rolę, ponieważ były pisane z myślą, że każda to osobny program.
        W celu szybszego manualnego testowania, funkcje zostały połączone w jeden program, który pozwala wybrać zadanie do samodzielnego przetestowania.
"""

from os import system, name
from msvcrt import getch
from math import sqrt


def calculate_polynomial() -> None:
    """
        ? Zadanie 1.
            Napisz program, który poprosi użytkownika o podanie liczby rzeczywistej x a następnie wyznaczy i wyświetli wartość następującego wielomianu: y=3x^3-5x^2+3x-7.

        * This function asks the user for a real number x and calculates and displays the value of the polynomial y=3x^3-5x^2+3x-7.
    """
    try:
        input_number: float = float(input("Podaj liczbę rzeczywistą x: "))
        polynomial_value: float = 3*input_number**3 - \
            5*input_number**2 + 3*input_number - 7
        print(
            f"Wartość wielomianu y = 3x^3-5x^2+3x-7 dla x = {format(input_number, '.6g')} wynosi: {format(polynomial_value, '.6g')}")
    except ValueError:
        print("Incorrect input, please enter a real number.")
    except KeyboardInterrupt:
        print("Program interrupted by the user.")
    except OverflowError:
        print("The number you entered is too large.")


def integer_calculator() -> None:
    """
        ? Zadanie 2.
            Napisz prosty kalkulator dla liczb całkowitych. Program ma pobierać od użytkownika dwie wartości liczbowe, a następnie wyświetlić ich sumę, iloczyn, iloraz oraz różnicę. Program powinien prosić o każdą liczbę indywidualnie. Wyniki należy wyświetlić w osobnych wierszach, w następującej kolejności: suma, różnica, iloczyn, iloraz.

        * This function asks the user for two integer values and displays their sum, product, quotient, and difference.
    """
    try:
        num_a: int = int(input("Podaj pierwszą liczbę całkowitą: "))
        num_b: int = int(input("Podaj drugą liczbę całkowitą: "))
        sum_ab: int = num_a + num_b
        diff_ab: int = num_a - num_b
        prod_ab: int = num_a * num_b
        print(f"Suma: {format(sum_ab, '.6g')}")
        print(f"Różnica: {format(diff_ab, '.6g')}")
        print(f"Iloczyn: {format(prod_ab, '.6g')}")
        if num_b != 0:
            quot_ab: float = num_a / num_b
            print(f"Iloraz: {format(quot_ab, '.6g')}")
        else:
            print("Nie można dzielić przez 0.")
    except ValueError:
        print("Incorrect input, please enter an integer.")


def print_complex_or_real(result: complex, operation: str) -> None:
    """
        * This function displays the result of the complex number operation in the correct format.
    """
    if result.imag == 0:
        print(f"{operation}: {format(result.real, '.6g')}")
    else:
        print(
            f"{operation}: {format(result.real, '.6g')}+{format(result.imag, '.6g')}j")


def complex_calculator() -> None:
    """
        ? Zadanie 3.
            Napisz prosty kalkulator dla liczb zespolonych. Program ma pobierać od użytkownika dwie wartości liczbowe, a następnie wyświetlić ich sumę, iloczyn, iloraz oraz różnicę. Program powinien prosić o każdą liczbę indywidualnie. Wyniki należy wyświetlić w osobnych wierszach, w następującej kolejności: suma, różnica, iloczyn, iloraz.

        * This function asks the user for two complex numbers and displays their sum, product, quotient, and difference.
    """
    try:
        num_a: complex = complex(input("Podaj pierwszą liczbę zespoloną: "))
        num_b: complex = complex(input("Podaj drugą liczbę zespoloną: "))
        sum_ab: complex = num_a + num_b
        diff_ab: complex = num_a - num_b
        prod_ab: complex = num_a * num_b
        quot_ab: complex = num_a / num_b if num_b != 0 else "Nie można dzielić przez 0."

        print_complex_or_real(sum_ab, "Suma")
        print_complex_or_real(diff_ab, "Różnica")
        print_complex_or_real(prod_ab, "Iloczyn")
        print_complex_or_real(quot_ab, "Iloraz")
    except ValueError:
        print("Incorrect input, please enter a complex number.")


def calculate_distance() -> None:
    """
        ? Zadanie 4.
            Napisz program, pobierający od użytkownika współrzędne dwóch punktów na płaszczyźnie,  a następnie wyznaczający i wyświetlający odległość między tymi punktami.

        * This function asks the user for the coordinates of two points on the plane and calculates and displays the distance between these points.
    """
    try:
        x1, y1 = map(float, input(
            "Podaj współrzędne pierwszego punktu (x y): ").split())
        x2, y2 = map(float, input(
            "Podaj współrzędne drugiego punktu (x y): ").split())
        distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        print(f"Odległość między punktami: {format(distance, '.15g')}")
    except ValueError:
        print("Incorrect input, please enter the coordinates of two points.")


def convert_temperature() -> None:
    """
        ? Zadanie 5.
            Napisz program, który dla podanej przez użytkownika temperatury w stopniach Celsjusza, wyświetli w osobnych wierszach temperaturę w Kelwinach i następnie stopniach Fahrenheita.

        * This function asks the user for a temperature in Celsius degrees and displays the temperature in Kelvin and then in Fahrenheit degrees.
    """
    try:
        celsius = float(input("Podaj temperaturę w stopniach Celsjusza: "))
        kelvin = celsius + 273.15
        fahrenheit = celsius * 9/5 + 32
        print(f"Temperatura w Kelwinach: {format(kelvin, '.6g')}")
        print(
            f"Temperatura w stopniach Fahrenheita: {format(fahrenheit, '.6g')}")
    except ValueError:
        print("Incorrect input, please enter a temperature in Celsius degrees.")


def main() -> None:
    """
        * This function displays the menu and allows the user to choose a task.
    """

    while True:
        if name == "nt":
            system("cls")
        else:
            system("clear")
        print("╔═══ Temat 1: Wprowadzanie i Wyświetlanie Danych ═══╗\n")
        print("  1. Zadanie - Wielomian 3 stopnia y=3x^3-5x^2+3x-7")
        print("  2. Zadanie - Kalkulator dla liczb całkowitych")
        print("  3. Zadanie - Kalkulator dla liczb zespolonych")
        print("  4. Zadanie - Odległość między punktami")
        print("  5. Zadanie - Konwerter temperatury")
        print("  0. Wyjście\n")
        print("╚═════════════════ Wybierz zadanie: ════════════════╝")
        user_choice: str = input(">>> ")
        if user_choice == '0':
            break
        elif user_choice == '1':
            calculate_polynomial()
            print("\nKoniec zadania 1")
        elif user_choice == '2':
            integer_calculator()
            print("\nKoniec zadania 2")
        elif user_choice == '3':
            complex_calculator()
            print("\nKoniec zadania 3")
        elif user_choice == '4':
            calculate_distance()
            print("\nKoniec zadania 4")
        elif user_choice == '5':
            convert_temperature()
            print("\nKoniec zadania 5")
        else:
            print("\nNiepoprawny wybór. Spróbuj ponownie.")

        print("\nNaciśnij dowolny klawisz, aby kontynuować...", end='')
        getch()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
