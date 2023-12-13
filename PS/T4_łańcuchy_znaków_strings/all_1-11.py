"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 4: Stringi

    ? Zadanie 1.
        Wyświetl  na  ekranie  dowolny  tekst,  który  ma  co  najmniej  siedem  znaków. Wyświetl liczbę znaków, które on zawiera. Wyświetl pierwszy i ostatni znak tego tekstu. Wyświetl 3 środkowe znaki tego tekstu.

    ? Zadanie 2.
        Wyświetl zdanie “Ala ma 2 koty” wykorzystując konwersję liczby 2.

    ? Zadanie 3.
        Zmodyfikuj  zdanie  z  poprzedniego  zadania  tak,  aby  każde  słowo  było oddzielone przecinkiem.

    ? Zadanie 4.
        Wyświetl zdanie z poprzedniego zadania tak, by każde słowo znajdowało się w osobnej linijce.

    ? Zadanie 5.
        Zamień słowo DOM na DOMEK.

    ? Zadanie 6.
        W słowie DOM wyświetl literę znajdującą się najdalej i najbliżej w alfabecie.

    ? Zadanie 7.
        W zdaniu “Ala ma 2 koty”:
        o sprawdź, czy wszystkie litery są małe, jeśli nie, to je zamień je na małe,
        o zmień pierwszą literę zdania na wielką.

    ? Zadanie 8.
        Centruj dowolny napis w polu o podanej długości.

    ? Zadanie 9.
        Wyrównaj dowolny napis do prawej w polu o podanej długości.

    ? Zadanie 10.
        Wyświetl dowolny napis z usuniętymi wiodącymi białymi znakami.

    ? Zadanie 11.
        Utwórz  skrypt,  który  zapyta  użytkownika  o  imię,  nazwisko,  numer  telefonu. Sprawdź,  czy  imię  i  nazwisko  wprowadzone  jest  poprawnie  (tylko  litery, pierwsza litera duża). Sprawdź, czy numer telefonu składa się tylko z cyfr i usuń ewentualnie zbędne znaki.

    ! NOTATKA:
        Funkcje pełnią więcej niż jedną rolę, ponieważ były pisane z myślą, że każda to osobny program.
        W celu szybszego manualnego testowania, funkcje zostały połączone w jeden program, który pozwala wybrać zadanie do samodzielnego przetestowania.
"""


from os import system, name
from msvcrt import getch


def display_text_info() -> None:
    """
        ? Zadanie 1.
            Wyświetl  na  ekranie  dowolny  tekst,  który  ma  co  najmniej  siedem  znaków. Wyświetl liczbę znaków, które on zawiera. Wyświetl pierwszy i ostatni znak tego tekstu. Wyświetl 3 środkowe znaki tego tekstu.

        * This function asks the user for a text of at least seven characters, displays the number of characters it contains, the first and last character of this text, and the three middle characters of this text.
    """
    try:
        user_text: str = input(
            "Podaj dowolny tekst, który ma co najmniej siedem znaków: ")
        if len(user_text) < 7:
            print("Tekst jest za krótki. Spróbuj ponownie.")
        else:
            print(f"Liczba znaków: {len(user_text)}")
            print(f"Pierwszy znak: {user_text[0]}")
            print(f"Ostatni znak: {user_text[-1]}")
            middle_index: int = len(user_text) // 2
            print(
                f"Trzy środkowe znaki: {user_text[middle_index-1:middle_index+2]}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def display_sentence() -> None:
    """
        ? Zadanie 2.
            Wyświetl zdanie “Ala ma 2 koty” wykorzystując konwersję liczby 2.

        * This function displays the sentence "Ala ma 2 koty" using the conversion of the number 2.
    """
    number_of_cats: int = 2
    print(f"Ala ma {number_of_cats} koty")
    # print("Ala ma {} koty".format(number_of_cats))
    # print("Ala ma %d koty" % number_of_cats)
    # print("Ala ma", number_of_cats, "koty")
    # print("Ala ma " + str(number_of_cats) + " koty")
    # print("Ala ma", str(number_of_cats), "koty")


def modify_sentence() -> None:
    """
        ? Zadanie 3.
            Zmodyfikuj  zdanie  z  poprzedniego  zadania  tak,  aby  każde  słowo  było oddzielone przecinkiem.

        * This function modifies the sentence from the previous task so that each word is separated by a comma.
    """
    sentence: str = "Ala ma 2 koty"
    modified_sentence: str = ", ".join(sentence.split())
    print(modified_sentence)


def display_sentence_in_lines() -> None:
    """
        ? Zadanie 4.
            Wyświetl zdanie z poprzedniego zadania tak, by każde słowo znajdowało się w osobnej linijce.

        * This function displays the sentence from the previous task so that each word is on a separate line.
    """
    sentence: str = "Ala, ma, 2, koty"
    for word in sentence.split(", "):
        print(word)


def replace_word() -> None:
    """
        ? Zadanie 5.
            Zamień słowo DOM na DOMEK.

        * This function replaces the word DOM with DOMEK.
    """
    word: str = "DOM"
    print(word)
    replaced_word: str = word.replace("DOM", "DOMEK")
    print(replaced_word)


def display_alphabet_positions() -> None:
    """
        ? Zadanie 6.
            W słowie DOM wyświetl literę znajdującą się najdalej i najbliżej w alfabecie.

        * This function displays the letter in the word DOM that is furthest and closest in the alphabet.
    """
    word: str = "DOM"
    sorted_word: str = sorted(word)
    print(f"Najbliżej w alfabecie: {sorted_word[0]}")
    print(f"Najdalej w alfabecie: {sorted_word[-1]}")


def modify_sentence_case() -> None:
    """
        ? Zadanie 7.
            W zdaniu “Ala ma 2 koty”:
            o sprawdź, czy wszystkie litery są małe, jeśli nie, to je zamień je na małe,
            o zmień pierwszą literę zdania na wielką.

        * This function checks if all the letters in the sentence "Ala ma 2 koty" are lowercase, if not, it changes them to lowercase, and then changes the first letter of the sentence to uppercase.
    """
    sentence: str = "Ala ma 2 koty"
    if not sentence.islower():
        sentence = sentence.lower()
    sentence = sentence.capitalize()
    print(sentence)


def center_text() -> None:
    """
        ? Zadanie 8.
            Centruj dowolny napis w polu o podanej długości.

        * This function asks the user for any text and a field length, and then centers the text in a field of the given length.
    """
    try:
        text: str = input("Podaj dowolny napis: ")
        length: int = int(input("Podaj długość pola: "))
        centered_text: str = text.center(length)
        print(centered_text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def right_align_text() -> None:
    """
        ? Zadanie 9.
            Wyrównaj dowolny napis do prawej w polu o podanej długości.

        * This function asks the user for any text and a field length, and then right-aligns the text in a field of the given length.
    """
    try:
        text: str = input("Podaj dowolny napis: ")
        length: int = int(input("Podaj długość pola: "))
        right_aligned_text: str = text.rjust(length)
        print(right_aligned_text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def remove_leading_whitespace() -> None:
    """
        ? Zadanie 10.
            Wyświetl dowolny napis z usuniętymi wiodącymi białymi znakami.

        * This function asks the user for any text and then displays the text with leading whitespace removed.
    """
    try:
        text: str = input("Podaj dowolny napis: ")
        text_without_leading_whitespace: str = text.lstrip()
        print(text_without_leading_whitespace)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def validate_user_data() -> None:
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


def main() -> None:
    """
        * This function displays the menu and allows the user to choose a task.
    """

    while True:
        if name == "nt":
            system("cls")
        else:
            system("clear")
        print("╔═════════════════ Temat 4: Stringi ═════════════════╗")
        print("  1. Zadanie")
        print("  2. Zadanie")
        print("  3. Zadanie")
        print("  4. Zadanie")
        print("  5. Zadanie")
        print("  6. Zadanie")
        print("  7. Zadanie")
        print("  8. Zadanie")
        print("  9. Zadanie")
        print("  10. Zadanie")
        print("  11. Zadanie")
        print("  0. Wyjście\n")
        print("╚════════════════ Wybierz zadanie: ═════════════════╝")
        user_choice: str = input(">>> ")
        if user_choice == '0':
            break
        elif user_choice == '1':
            display_text_info()
            print("\nKoniec zadania 1")
        elif user_choice == '2':
            display_sentence()
            print("\nKoniec zadania 2")
        elif user_choice == '3':
            modify_sentence()
            print("\nKoniec zadania 3")
        elif user_choice == '4':
            display_sentence_in_lines()
            print("\nKoniec zadania 4")
        elif user_choice == '5':
            replace_word()
            print("\nKoniec zadania 5")
        elif user_choice == '6':
            display_alphabet_positions()
            print("\nKoniec zadania 6")
        elif user_choice == '7':
            modify_sentence_case()
            print("\nKoniec zadania 7")
        elif user_choice == '8':
            center_text()
            print("\nKoniec zadania 8")
        elif user_choice == '9':
            right_align_text()
            print("\nKoniec zadania 9")
        elif user_choice == '10':
            remove_leading_whitespace()
            print("\nKoniec zadania 10")
        elif user_choice == '11':
            validate_user_data()
            print("\nKoniec zadania 11")
        else:
            print("\nNiepoprawny wybór. Spróbuj ponownie.")

        print("\nNaciśnij dowolny klawisz, aby kontynuować...", end='')
        getch()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
