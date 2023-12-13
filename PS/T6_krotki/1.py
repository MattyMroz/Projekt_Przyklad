"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 6: Krotki
"""


def main() -> None:
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

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
