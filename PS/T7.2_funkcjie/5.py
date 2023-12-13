"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 7.2: Funkcje
"""


def main() -> None:
    """
        ? Zadanie 5.
            Napisz program, aby znaleźć pierwszy numer trójkąta, który ma ponad n (podanych) dzielników.

        * This function finds the first triangle number that has more than n (given) divisors.
    """
    try:
        n: int = int(input("Podaj liczbę dzielników n: "))

        def divisors(n):
            """
                * Zwraca liczbę dzielników danej liczby.
            """
            i = 1
            divisors = 0
            while i <= n**0.5:
                if n % i == 0:
                    if n / i == i:
                        divisors += 1
                    else:
                        divisors += 2
                i += 1
            return divisors

        i = 1
        while True:
            triangle_number = i*(i+1)//2
            if divisors(triangle_number) > n:
                print(
                    "Pierwszy numer trójkąta, który ma ponad n dzielników to: ", triangle_number)
                break
            i += 1
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
