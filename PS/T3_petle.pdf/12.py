"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 3: Pętle
"""

# import math


def main() -> None:
    """
        ? Zadanie 12.
            Napisz program, który wyznacza silnię dla dowolnej liczby naturalnej n, mniejszej od 21, wpisywanej z klawiatury. W przypadku podania przez użytkownika nieprawidłowych danych program ma wyświetlić komunikat o błędzie i ponowić pytanie o nową wartość n.

        * This function calculates the factorial for a natural number n, less than 21. It handles incorrect input.
    """
    # while True:
    #     num_n = int(input("Podaj liczbę naturalną mniejszą od 21: "))
    #     if num_n < 0 or num_n > 20:
    #         print("Nieprawidłowe dane. Podaj liczbę naturalną mniejszą od 21.")
    #     else:
    #         print(math.factorial(num_n))
    #         break
    try:
        while True:
            num_n: int = int(input("Podaj liczbę naturalną mniejszą od 21: "))
            if num_n < 0 or num_n > 20:
                print("Nieprawidłowe dane. Podaj liczbę naturalną mniejszą od 21.")
            else:
                result: int = 1
                for i in range(1, num_n + 1):
                    result *= i
                print(result)
                break
    except ValueError:
        print("Niepoprawne dane wejściowe, proszę wprowadzić liczbę naturalną.")
        # print("Invalid input, please enter a natural number.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
