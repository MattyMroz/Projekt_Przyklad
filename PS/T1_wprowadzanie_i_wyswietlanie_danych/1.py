"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 1: Wprowadzanie i Wyświetlanie Danych
"""


def main() -> None:
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


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
