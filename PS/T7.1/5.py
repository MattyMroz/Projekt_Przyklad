"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 7.1
"""


def main() -> None:
    """
        ? Zadanie 5.
            Napisz program, który ma znaleźć różnicę między sumą kwadratów pierwszych dwustu liczb naturalnych a kwadratem sumy.

        * This function finds the difference between the sum of the squares of the first two hundred natural numbers and the square of the sum.
    """
    try:
        sum_of_squares: int = sum(i**2 for i in range(1, 201))
        square_of_sum: int = sum(range(1, 201))**2
        difference: int = square_of_sum - sum_of_squares
        print(
            f"Różnica między sumą kwadratów pierwszych dwustu liczb naturalnych a kwadratem sumy wynosi: {difference}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
