"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 1: Wprowadzanie i Wyświetlanie Danych
"""


def print_complex_or_real(result: complex, operation: str) -> None:
    """
        * This function displays the result of the complex number operation in the correct format.
    """
    if result.imag == 0:
        print(f"{operation}: {format(result.real, '.6g')}")
    else:
        print(
            f"{operation}: {format(result.real, '.6g')}+{format(result.imag, '.6g')}j")


def main() -> None:
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


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
