"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 3: Pętle

    ? Zadanie 1.
        Wyświetl sumę liczb nieparzystych od 1 do 21.

    ? Zadanie 2.
        Wyświetl wszystkie liczby parzyste do liczby 63.

    ? Zadanie 3.
        Wyświetl kwadrat sumy i sumę kwadratów liczb parzystych od 2 do 30.

    ? Zadanie 4.
        Wyświetl na ekranie liczby całkowite od 1 do 10, każda w nowej linii.

    ? Zadanie 5.
        Wyświetl na ekranie w jednej linijce liczby całkowite od 1 do 10 rozdzielone przecinkiem.

    ? Zadanie 6.
        Wyświetl na ekranie poziomą kreskę składającą się z dziesięciu znaków ‘#’.

    ? Zadanie 7.
        Wyświetl na ekranie pionową kreskę składającą się z dziesięciu znaków ‘#’.

    ? Zadanie 8.
        Wyświetl na ekranie wypełniony kwadrat składający się z 25 znaków ‘#’.

    ? Zadanie 9.
        Wyświetl na ekranie pusty kwadrat składający się z 16 znaków ‘#’.

    ? Zadanie 10.
        Wyświetl na ekranie wynik operacji 20!

    ? Zadanie 11.
        Napisz program, który wyznacza obwód i powierzchnię koła o promieniu podanym przez użytkownika. Użytkownik może podać wartość niecałkowitą. W przypadku, gdy użytkownik poda wartość ujemną, należy wyświetlić komunikat o błędzie i ponowić pytanie o promień, aż będzie możliwe obliczenie obwodu i powierzchni koła, wtedy program powinien zakończyć działanie.

    ? Zadanie 12.
        Napisz program, który wyznacza silnię dla dowolnej liczby naturalnej n, mniejszej od 21, wpisywanej z klawiatury. W przypadku podania przez użytkownika nieprawidłowych danych program ma wyświetlić komunikat o błędzie i ponowić pytanie o nową wartość n.


    ! NOTATKA:
        Funkcje pełnią więcej niż jedną rolę, ponieważ były pisane z myślą, że każda to osobny program.
        W celu szybszego manualnego testowania, funkcje zostały połączone w jeden program, który pozwala wybrać zadanie do samodzielnego przetestowania.
"""


from os import system, name
from msvcrt import getch
import math


def display_odd_numbers_sum() -> None:
    """
        ? Zadanie 1.
            Wyświetl sumę liczb nieparzystych od 1 do 21.

        * This function displays the sum of odd numbers from 1 to 21.
    """
    print(sum(i for i in range(1, 22) if i % 2 != 0))


def display_even_numbers() -> None:
    """
        ? Zadanie 2.
            Wyświetl wszystkie liczby parzyste do liczby 63.
            ! Polecenie jest nie prezyzyjne licząc od 0 do 63, czy od 2 do 63, a może od -nieskończoności do 63 hmmm...?

        * This function displays all even numbers up to 63.
    """
    for i in range(0, 64, 2):
        print(i, end=' ')

    # for i in range(2, 64, 2):
    #     print(i, end=' ')


def display_square_sum_and_sum_of_squares() -> None:
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


def display_numbers() -> None:
    """
        ? Zadanie 4.
            Wyświetl na ekranie liczby całkowite od 1 do 10, każda w nowej linii.

        * This function displays integers from 1 to 10, each on a new line.
    """
    for i in range(1, 11):
        print(i)


def display_numbers_inline() -> None:
    """
        ? Zadanie 5.
            Wyświetl na ekranie w jednej linijce liczby całkowite od 1 do 10 rozdzielone przecinkiem.

        * This function displays integers from 1 to 10 on one line, separated by a comma.
    """
    print(", ".join(str(i) for i in range(1, 11)))


def display_horizontal_line() -> None:
    """
        ? Zadanie 6.
            Wyświetl na ekranie poziomą kreskę składającą się z dziesięciu znaków ‘#’.

        * This function displays a horizontal line consisting of ten '#' characters.
    """
    # print('#' * 10)
    for _ in range(10):
        print('#', end='')
    print()


def display_vertical_line() -> None:
    """
        ? Zadanie 7.
            Wyświetl na ekranie pionową kreskę składającą się z dziesięciu znaków ‘#’.

        * This function displays a vertical line consisting of ten '#' characters.
    """
    for _ in range(10):
        print('#')


def display_filled_square() -> None:
    """
        ? Zadanie 8.
            Wyświetl na ekranie wypełniony kwadrat składający się z 25 znaków ‘#’.

        * This function displays a filled square consisting of 25 '#' characters.
    """
    # for _ in range(5):
    #     print('#' * 5)
    for _ in range(5):
        for _ in range(5):
            print('#', end='')
        print()


def display_empty_square() -> None:
    """
        ? Zadanie 9.
            Wyświetl na ekranie pusty kwadrat składający się z 16 znaków ‘#’.

        * This function displays an empty square consisting of 16 '#' characters.
    """
    # print('#' * 5)
    # for _ in range(3):
    #     print('#' + ' ' * 3 + '#')
    # print('#' * 5)
    for i in range(5):
        if i == 0 or i == 4:
            for _ in range(5):
                print('#', end='')
        else:
            print('#', end='')
            for _ in range(3):
                print(' ', end='')
            print('#', end='')
        print()


def display_factorial() -> None:
    """
        ? Zadanie 10.
            Wyświetl na ekranie wynik operacji 20!.

        * This function displays the result of the operation 20!.
    """
    # print(math.factorial(20))
    result: int = 1
    for i in range(1, 21):
        result *= i
    print(result)


def calculate_circle() -> None:
    """
        ? Zadanie 11.
                Napisz program, który wyznacza obwód i powierzchnię koła o promieniu podanym przez użytkownika. Użytkownik może podać wartość niecałkowitą. W przypadku, gdy użytkownik poda wartość ujemną, należy wyświetlić komunikat o błędzie i ponowić pytanie o promień, aż będzie możliwe obliczenie obwodu i powierzchni koła, wtedy program powinien zakończyć działanie.

        * This function calculates the circumference and area of a circle. It handles negative and non-integer input.
    """
    try:
        while True:
            try:
                radius = float(input("Podaj promień koła: "))
                if radius < 0:
                    print("Promień nie może być ujemny, proszę podać dodatnią wartość.")
                else:
                    circumference = 2 * math.pi * radius
                    area = math.pi * (radius ** 2)
                    print(
                        f"Obwód koła: {format(circumference, '.6g')}, Pole koła: {format(area, '.6g')}")
                    break
            except ValueError:
                print(
                    "Niepoprawne dane wejściowe, proszę wprowadzić wartość zmiennoprzecinkową.")
                # print("Invalid input, please enter a floating point value.")
    except KeyboardInterrupt:
        print("Program interrupted by the user.")


def calculate_factorial() -> None:
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


def main() -> None:
    """
        * This function displays the menu and allows the user to choose a task.
    """

    while True:
        if name == "nt":
            system("cls")
        else:
            system("clear")
        print("╔═════════════════ Temat 3: Pętle ═════════════════╗")
        print("  1. Zadanie - Suma nieparzystych od 1 do 21")
        print("  2. Zadanie - Liczby parzyste do 63")
        print("  3. Zadanie - Kwadrat sumy i suma kwadratów liczb parzystych od 2 do 30")
        print("  4. Zadanie - Liczby całkowite od 1 do 10")
        print("  5. Zadanie - Liczby całkowite od 1 do 10 w jednej linii")
        print("  6. Zadanie - Pozioma kreska z dziesięciu znaków '#'")
        print("  7. Zadanie - Pionowa kreska z dziesięciu znaków '#'")
        print("  8. Zadanie - Wypełniony kwadrat z 25 znaków '#'")
        print("  9. Zadanie - Pusty kwadrat z 16 znaków '#'")
        print("  10. Zadanie - 20!")
        print("  11. Zadanie - Obwód i powierzchnia koła")
        print("  12. Zadanie - Silnia")
        print("  0. Wyjście\n")
        print("╚════════════════ Wybierz zadanie: ════════════════╝")
        user_choice: str = input(">>> ")
        if user_choice == '0':
            break
        elif user_choice == '1':
            display_odd_numbers_sum()
            print("\nKoniec zadania 1")
        elif user_choice == '2':
            display_even_numbers()
            print("\nKoniec zadania 2")
        elif user_choice == '3':
            display_square_sum_and_sum_of_squares()
            print("\nKoniec zadania 3")
        elif user_choice == '4':
            display_numbers()
            print("\nKoniec zadania 4")
        elif user_choice == '5':
            display_numbers_inline()
            print("\nKoniec zadania 5")
        elif user_choice == '6':
            display_horizontal_line()
            print("\nKoniec zadania 6")
        elif user_choice == '7':
            display_vertical_line()
            print("\nKoniec zadania 7")
        elif user_choice == '8':
            display_filled_square()
            print("\nKoniec zadania 8")
        elif user_choice == '9':
            display_empty_square()
            print("\nKoniec zadania 9")
        elif user_choice == '10':
            display_factorial()
            print("\nKoniec zadania 10")
        elif user_choice == '11':
            calculate_circle()
            print("\nKoniec zadania 11")
        elif user_choice == '12':
            calculate_factorial()
            print("\nKoniec zadania 12")
        else:
            print("\nNiepoprawny wybór. Spróbuj ponownie.")

        print("\nNaciśnij dowolny klawisz, aby kontynuować...", end='')
        getch()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
