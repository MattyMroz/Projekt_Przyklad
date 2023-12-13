"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 8
"""


def main() -> None:
    """
        ? Zadanie 1.
            Napisz program, aby znaleźć produkt xyz używając trójki pitagorajskiej

        * This function finds the product xyz using a Pythagorean triplet for which x + y + z = 1000.
    """
    for x in range(1, 1000):
        for y in range(x, 1000):
            z: int = 1000 - x - y
            if x * x + y * y == z * z:
                # print(f"Trójka pitagorejska: {x}, {y}, {z}") # 200, 375, 425
                print(f"Produkt xyz: {x*y*z}")
                return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
