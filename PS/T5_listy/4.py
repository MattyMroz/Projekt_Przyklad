"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 5: Listy
"""


def main() -> None:
    """
        ? Zadanie 4.
            Dane są wyniki losowania w pewnej grze liczbowej: wynik=[12,1,45,76,50,23]
            Wiedząc, że wylosowane wartości mogą zawierać się w przedziale od 1 do 49 zastąp występujące w liście liczby nie spełniające tego kryterium na takie, które będą je spełniać.

        * This function replaces the numbers in the list that do not meet the criterion of being in the range from 1 to 49 with numbers that meet this criterion.
    """
    try:
        result: list = [12, 1, 45, 76, 50, 23]
        for i in range(len(result)):
            if not 1 <= result[i] <= 49:
                result[i] = 1 if result[i] < 1 else 49
        print(result)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
