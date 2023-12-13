"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 2: Instrukcje Warunkowe
"""


def main() -> None:
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


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
