"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 2: Instrukcje Warunkowe
"""


def main() -> None:
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


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
