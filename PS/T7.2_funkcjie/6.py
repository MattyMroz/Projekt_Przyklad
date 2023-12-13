"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 7.2: Funkcje
"""


def main() -> None:
    """
        ? Zadanie 6.
            Napisz program, aby znaleźć największy palindrom utworzony z iloczynu dwóch 4-cyfrowych liczb.

        * This function finds the largest palindrome made from the product of two 4-digit numbers.
    """
    try:
        def is_palindrome(n):
            return str(n) == str(n)[::-1]

        max_palindrome = 0
        # W przeciwieństwie do tematu 7.1 zaczynamy od końca, wychodzi na to samo (*_*)
        for i in range(9999, 999, -1):
            for j in range(i, 999, -1):
                if is_palindrome(i*j) and i*j > max_palindrome:
                    max_palindrome = i*j
        print("Największy palindrom utworzony z iloczynu dwóch 4-cyfrowych liczb to: ", max_palindrome)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
