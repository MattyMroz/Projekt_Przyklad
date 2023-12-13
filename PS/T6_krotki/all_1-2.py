"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 3: Pętle

    ? Zadanie 1.
        Utwórz listę, której elementy użytkownik będzie podawał wewnątrz pętli. Może to być imię, nazwisko i wiek. Następnie utwórz z powyższej listy krotkę i wyświetl jej zawartość. Proszę zwrócić uwagę, że wiek jest wartością typu integer.

    ? Zadanie 2.
        Zmodyfikować program z zadania 1, tak, aby można było określić, ile osób chcemy wpisać do listy: 2, 3, idt.

    ! NOTATKA:
        Funkcje pełnią więcej niż jedną rolę, ponieważ były pisane z myślą, że każda to osobny program.
        W celu szybszego manualnego testowania, funkcje zostały połączone w jeden program, który pozwala wybrać zadanie do samodzielnego przetestowania.
"""


from os import system, name
from msvcrt import getch


def create_tuple_from_list() -> None:
    """
        ? Zadanie 1.
            Utwórz listę, której elementy użytkownik będzie podawał wewnątrz pętli. Może to być imię, nazwisko i wiek. Następnie utwórz z powyższej listy krotkę i wyświetl jej zawartość. Proszę zwrócić uwagę, że wiek jest wartością typu integer.

        * This function asks the user for their name, surname, and age, creates a list from these elements, then creates a tuple from this list and displays its contents.
    """
    try:
        name: str = input("Podaj swoje imię: ")
        surname: str = input("Podaj swoje nazwisko: ")
        age: int = int(input("Podaj swój wiek: "))
        user_list: list = [name, surname, age]
        user_tuple: tuple = tuple(user_list)
        print(user_tuple)
    except ValueError:
        print("Incorrect input, age should be an integer.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def create_multiple_tuples_from_lists() -> None:
    """
        ? Zadanie 2.
            Zmodyfikować program z zadania 1, tak, aby można było określić, ile osób chcemy wpisać do listy: 2, 3, idt.

        * This function asks the user for the number of people they want to enter, then for each person asks for their name, surname, and age, creates a list from these elements, then creates a tuple from this list and displays its contents.
    """
    try:
        number_of_people: int = int(
            input("Ile osób chcesz wpisać do listy?: "))
        for i in range(number_of_people):
            name: str = input(f"Podaj imię osoby {i+1}: ")
            surname: str = input(f"Podaj nazwisko osoby {i+1}: ")
            age: str = int(input(f"Podaj wiek osoby {i+1}: "))
            user_list: list = [name, surname, age]
            user_tuple: tuple = tuple(user_list)
            print(user_tuple)
    except ValueError:
        print("Incorrect input, number of people and age should be integers.")
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
        print("╔═════════════════ Temat 6: Krotki ═════════════════╗")
        print("  1. Zadanie - Utwórz krotkę z listy")
        print("  2. Zadanie - Utwórz wiele krotek z list")
        print("  0. Wyjście\n")
        print("╚════════════════ Wybierz zadanie: ════════════════╝")
        user_choice: str = input(">>> ")
        if user_choice == '0':
            break
        elif user_choice == '1':
            create_tuple_from_list()
            print("\nKoniec zadania 1")
        elif user_choice == '2':
            create_multiple_tuples_from_lists()
            print("\nKoniec zadania 2")
        else:
            print("\nNiepoprawny wybór. Spróbuj ponownie.")

        print("\nNaciśnij dowolny klawisz, aby kontynuować...", end='')
        getch()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
