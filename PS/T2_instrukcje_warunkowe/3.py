"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 2: Instrukcje Warunkowe
"""


def main() -> None:
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


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
