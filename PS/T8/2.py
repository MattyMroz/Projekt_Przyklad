"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 8
"""


def main() -> None:
    try:
        n: int = int(input("Podaj liczbę dzielników n: "))

        def divisors(n):
            """
                * Zwraca liczbę dzielników danej liczby.
            """
            i: int = 1
            divisors: int = 0
            while i <= n**0.5:
                if n % i == 0:
                    if n / i == i:
                        divisors += 1
                    else:
                        divisors += 2
                i += 1
            return divisors

        i: int = 1
        while True:
            triangle_number = i*(i+1)//2
            if divisors(triangle_number) > n:
                print(
                    f"Pierwszy numer trójkąta, który ma ponad {n} dzielników to: {triangle_number}")
                break
            i += 1
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
