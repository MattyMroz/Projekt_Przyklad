"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 1: Wprowadzanie i Wyświetlanie Danych
"""


def main() -> None:
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


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
