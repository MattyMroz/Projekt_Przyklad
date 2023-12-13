"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 1: Wprowadzanie i Wyświetlanie Danych
"""

from math import sqrt


def main() -> None:
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


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
