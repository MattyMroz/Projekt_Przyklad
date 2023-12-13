"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 1: Wprowadzanie i Wyświetlanie Danych
"""


def main() -> None:
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


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
