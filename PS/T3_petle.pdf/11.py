"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 3: Pętle
"""

import math


def main() -> None:
    """
        ? Zadanie 11.
                Napisz program, który wyznacza obwód i powierzchnię koła o promieniu podanym przez użytkownika. Użytkownik może podać wartość niecałkowitą. W przypadku, gdy użytkownik poda wartość ujemną, należy wyświetlić komunikat o błędzie i ponowić pytanie o promień, aż będzie możliwe obliczenie obwodu i powierzchni koła, wtedy program powinien zakończyć działanie.

        * This function calculates the circumference and area of a circle. It handles negative and non-integer input.
    """
    try:
        while True:
            try:
                radius = float(input("Podaj promień koła: "))
                if radius < 0:
                    print("Promień nie może być ujemny, proszę podać dodatnią wartość.")
                else:
                    circumference = 2 * math.pi * radius
                    area = math.pi * (radius ** 2)
                    print(
                        f"Obwód koła: {format(circumference, '.6g')}, Pole koła: {format(area, '.6g')}")
                    break
            except ValueError:
                print(
                    "Niepoprawne dane wejściowe, proszę wprowadzić wartość zmiennoprzecinkową.")
                # print("Invalid input, please enter a floating point value.")
    except KeyboardInterrupt:
        print("Program interrupted by the user.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
