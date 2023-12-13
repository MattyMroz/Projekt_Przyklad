"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 7.1

    ? Zadanie 1.
        Napisz program, który obliczy sumę wszystkich wielokrotności 3 lub 5 poniżej 500.

    ? Zadanie 2.
        Napisz program, aby znaleźć największy czynnik pierwszy dla danej liczby.

    ? Zadanie 3.
        Napisz program, aby znaleźć największy palindrom utworzony z iloczynu dwóch 4-cyfrowych liczb.

    ? Zadanie 4.
        Napisz program, aby znaleźć najmniejszą liczbę dodatnią, która jest równo podzielna przez wszystkie liczby od 1 do 30.

    ? Zadanie 5.
        Napisz program, który ma znaleźć różnicę między sumą kwadratów pierwszych dwustu liczb naturalnych a kwadratem sumy.

    ? Zadanie 6.
        Napisz program, aby znaleźć 1000-ną liczbę pierwszą.


    ! NOTATKA:
        Funkcje pełnią więcej niż jedną rolę, ponieważ były pisane z myślą, że każda to osobny program.
        W celu szybszego manualnego testowania, funkcje zostały połączone w jeden program, który pozwala wybrać zadanie do samodzielnego przetestowania.
"""

from os import system, name
from msvcrt import getch


def sum_of_multiples() -> None:
    """
        ? Zadanie 1.
            Napisz program, który obliczy sumę wszystkich wielokrotności 3 lub 5 poniżej 500.

        * This function calculates the sum of all multiples of 3 or 5 below 500.
    """
    try:
        sum_of_multiples: int = sum(
            i for i in range(500) if i % 3 == 0 or i % 5 == 0)
        print(
            f"Suma wszystkich wielokrotności 3 lub 5 poniżej 500 wynosi: {sum_of_multiples}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def largest_prime_factor() -> None:
    """
        ? Zadanie 2.
            Napisz program, aby znaleźć największy czynnik pierwszy dla danej liczby.

        * This function finds the largest prime factor for a given number.
    """
    try:
        number: int = int(input("Podaj liczbę: "))
        i: int = 2
        while i * i <= number:
            if number % i:
                i += 1
            else:
                number //= i
        print(
            f"Największy czynnik pierwszy dla podanej liczby wynosi: {number}")
    except ValueError:
        print("Incorrect input, please enter a number.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def largest_palindrome() -> None:
    """
        ? Zadanie 3.
            Napisz program, aby znaleźć największy palindrom utworzony z iloczynu dwóch 4-cyfrowych liczb.

        * This function finds the largest palindrome made from the product of two 4-digit numbers.
    """
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


def smallest_multiple() -> None:
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


def sum_square_difference() -> None:
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


def nth_prime_number() -> None:
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


def main() -> None:
    """
        * This function displays the menu and allows the user to choose a task.
    """

    while True:
        if name == "nt":
            system("cls")
        else:
            system("clear")
        print("╔════════════════════ Temat 7.1 ════════════════════╗")
        print("  1. Zadanie - Suma wielokrotności 3 lub 5 poniżej 500")
        print("  2. Zadanie - Największy czynnik pierwszy")
        print("  3. Zadanie - Największy palindrom")
        print(
            "  4. Zadanie - Najmniejsza liczba dodatnia podzielna przez liczby od 1 do 30")
        print("  5. Zadanie - Różnica między sumą kwadratów a kwadratem sumy")
        print("  6. Zadanie - 1000-ną liczba pierwsza")
        print("  0. Wyjście\n")
        print("╚════════════════ Wybierz zadanie: ════════════════╝")
        user_choice: str = input(">>> ")
        if user_choice == '0':
            break
        elif user_choice == '1':
            sum_of_multiples()
            print("\nKoniec zadania 1")
        elif user_choice == '2':
            largest_prime_factor()
            print("\nKoniec zadania 2")
        elif user_choice == '3':
            print("\nZadanie 3 może chwilę potrwać...")
            largest_palindrome()
            print("\nKoniec zadania 3")
        elif user_choice == '4':
            smallest_multiple()
            print("\nKoniec zadania 4")
        elif user_choice == '5':
            sum_square_difference()
            print("\nKoniec zadania 5")
        elif user_choice == '6':
            nth_prime_number()
            print("\nKoniec zadania 6")
        else:
            print("\nNiepoprawny wybór. Spróbuj ponownie.")

        print("\nNaciśnij dowolny klawisz, aby kontynuować...", end='')
        getch()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
