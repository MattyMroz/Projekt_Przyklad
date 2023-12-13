"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 7.1
"""


def main() -> None:
    """
        ? Zadanie 3.
            Napisz program, aby znaleźć największy palindrom utworzony z iloczynu dwóch 4-cyfrowych liczb.

        * This function finds the largest palindrome made from the product of two 4-digit numbers.
    """
    print("\nZadanie 3 może chwilę potrwać...")
    try:
        max_palindrome: int = max(i*j                               # Nasz iloczyn
                                  # Pierwsza liczba
                                  for i in range(1000, 10000)
                                  # Druga liczba
                                  for j in range(1000, 10000)
                                  if str(i*j) == str(i*j)[::-1])    # Sprawdzamy, czy nasz iloczyn jest palindromem
        print(
            f"Największy palindrom utworzony z iloczynu dwóch 4-cyfrowych liczb wynosi: {max_palindrome}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
