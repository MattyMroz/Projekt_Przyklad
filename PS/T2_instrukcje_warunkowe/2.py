"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 2: Instrukcje Warunkowe
"""


def main() -> None:
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
                    x1: float = c / (a * x2)
                    x2: float = (-b + delta**0.5) / (2*a)
                print(
                    f"Są dwa pierwiastki rzeczywiste: {format(x1, '.15g')} i {format(x2, '.15g')}")
            else:
                print("Brak pierwiastków rzeczywistych.")
    except ValueError:
        print("Incorrect input, please enter a number.")
    except KeyboardInterrupt:
        print("Program interrupted by the user.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
