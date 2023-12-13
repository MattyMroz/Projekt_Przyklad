"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 7.1
"""


def main() -> None:
    """
        ? Zadanie 6.
            Napisz program, aby znaleźć 1000-ną liczbę pierwszą.

        * This function finds the 1000th prime number.
    """
    try:
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        def nth_prime(n: int) -> int:
            count: int = 0
            num: int = 0
            while count < n:
                num += 1
                if is_prime(num):
                    count += 1
            return num

        print(f"1000-ną liczbą pierwszą jest: {nth_prime(1000)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
