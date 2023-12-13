"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 6: Krotki
"""


def main() -> None:
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


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
