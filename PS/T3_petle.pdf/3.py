"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 3: Pętle
"""


def main() -> None:
    """
        ? Zadanie 3.
            Wyświetl kwadrat sumy i sumę kwadratów liczb parzystych od 2 do 30.

        * This function displays the square of the sum and the sum of squares of even numbers from 2 to 30.
    """
    even_numbers: list = [i for i in range(2, 31) if i % 2 == 0]
    square_of_sum: int = sum(even_numbers) ** 2
    sum_of_squares: int = sum(i ** 2 for i in even_numbers)

    print(f"Kwadrat sumy liczb parzystych: {square_of_sum}")
    print(f"Suma kwadratów liczb parzystych: {sum_of_squares}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
