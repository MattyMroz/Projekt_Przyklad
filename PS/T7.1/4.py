"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 7.1
"""


def main() -> None:
    """
        ? Zadanie 4.
            Napisz program, aby znaleźć najmniejszą liczbę dodatnią, która jest równo podzielna przez wszystkie liczby od 1 do 30.

        * This function finds the smallest positive number that is evenly divisible by all of the numbers from 1 to 30.
    """
    try:
        def gcd(x: int, y: int) -> int:
            """
                * Największy wspólny dzielnik
            """
            while(y):
                x, y = y, x % y
            return x

        def lcm(x: int, y: int) -> int:
            """
                * Najmniejsza wspólna wielokrotność
            """
            lcm = (x*y)//gcd(x, y)
            return lcm

        # Dla każdej liczby obliczamy najmniejszą wspólną wielokrotność z aktualnym num
        # W ten sposób otrzymujemy najmniejszą wspólną wielokrotność dla wszystkich liczb od 1 do 30 czyli nasze szukaną liczbę podzielną przez wszystkie liczby od 1 do 30
        num: int = 1
        for i in range(1, 31):
            num = lcm(num, i)
        print(
            f"Najmniejsza liczba dodatnia, która jest równo podzielna przez wszystkie liczby od 1 do 30 wynosi: {num}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
