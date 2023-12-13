"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 4: Stringi
"""


def main() -> None:
    """
        ? Zadanie 11.
            Utwórz  skrypt,  który  zapyta  użytkownika  o  imię,  nazwisko,  numer  telefonu. Sprawdź,  czy  imię  i  nazwisko  wprowadzone  jest  poprawnie  (tylko  litery, pierwsza litera duża). Sprawdź, czy numer telefonu składa się tylko z cyfr i usuń ewentualnie zbędne znaki.

        * This function asks the user for their name, surname, and phone number. It checks if the name and surname are entered correctly (only letters, the first letter is uppercase). It checks if the phone number consists only of digits and removes any unnecessary characters.
    """
    try:
        name: str = input("Podaj swoje imię: ")
        surname: str = input("Podaj swoje nazwisko: ")
        phone_number: str = input("Podaj swój numer telefonu: ")

        if not name.isalpha() or not name[0].isupper():
            print(
                "Niepoprawne imię. Powinno składać się tylko z liter, a pierwsza litera powinna być duża.")
        if not surname.isalpha() or not surname[0].isupper():
            print(
                "Niepoprawne nazwisko. Powinno składać się tylko z liter, a pierwsza litera powinna być duża.")

        phone_number: str = ''.join(filter(str.isdigit, phone_number))
        if not phone_number.isdigit():
            print("Niepoprawny numer telefonu. Powinien składać się tylko z cyfr.")
        else:
            print(f"Twój numer telefonu to: {phone_number}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
