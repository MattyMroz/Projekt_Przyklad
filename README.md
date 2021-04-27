# Projekt_Przyklad
Przykładowy projekt od nauki
xX Kroki_Poznania – Taksonomia_Blooma Xx https://bit.ly/3sD2XYA
1.Wiedza 2.Rozumienie 3.Zastosowanie 4.Analiza 5.Synteza 6.Ocenianie

#########################################################################

WSĘPNIE w Visual Studio Code:
INSTALACJA – MinGW i VSC:
https://tiny.pl/rs7xw
https://nuwen.net/mingw.html
https://code.visualstudio.com/

#########################################################################

ROZSZERZENIA PLIKÓW:
C++ -> plik.cpp / plik.c
Pliki nagłówkowe -> plik.hpp / plik.h

#########################################################################

URUCHAMIANIE PROGRAMU:
g++ program1.cpp -o p1 // Stworzenie pliku wykonującego p1.exe
g++ *.cpp -o p1 //Stworzenie pliku wykonującego p1.exe dla programu obiektowego, (wywołuje wszystkie pliki bieżącego folderu) – 1 folder (src) = jedna funkcja główna + pod funkcje i inne pliki
./p1 // Uruchomienie pliku p1.exe

#########################################################################

KOMENTARZE – notatka dla programisty:
// Komentarz jednoliniowy

/*
    Komentarz wieloliniowy
    Komentarz wieloliniowy
*/

#########################################################################

SZABLON PODSTAWOWEGO PROGRAMU:
#include <iostream>
using namespace std;

int main(){

    cout<<"Hello world!"<<endl;
    return 0;
}

#########################################################################

OMÓWIENIE:
#include <iostream> // Biblioteka – udostępnia różnorakie funkcje programowi – łatwość
using namespace std; // Użycie standardowej przestrzeni nazw

int main(){} // Funkcja główna – obowiązkowa do działania

    cout << "Hello world!" <<endl; // Komunikaty w terminalu + zakończenie linii
    cout << "Hello world! \n"; // Komunikaty w terminalu + zakończenie linii
    cout << zmienna; // Wyprowadzenie zmiennej w terminalu
    return 0; // Funkcja zwraca 0 – nic

#########################################################################

ZMIENNE:
– obiekt, który przechowuje różnego rodzaju dane które są niezbędne do działania programu,
– zmienna może zmienia swoją wartość podczas działania programu,
– tworząc zmienną musimy podać:
    – typ zmiennej (później)
    – nazwa zmiennej:
        – nazwa nie może być słowem kluczowym języka programowania
        – w nazwach nie używamy polskich liter, spacji (używanie_podkreślenia)
        – nazwa nie może zaczynać się od cyfry
        – nazwa powinna kojarzyć się z przeznaczeniem zmiennej
        – zmienne stałe zapisywane są z dużych liter

#########################################################################

TYPY ZMIENNYCH / DANYCH:

    Wielkość może różnić się w zależności od systemu
Typy całkowite -/+:
    Nazwa       Wielkość (bajty)        Zakres
    short	    2	    -2^15 ÷ 2^15 - 1, czyli przedział [-32768, 32767]
    int         4	    -2^31 ÷ 2^31 - 1, czyli przedział [-2147483648, 2147483647]
    long        4	    -2^31 ÷ 2^31 - 1, czyli przedział [-2147483648, 2147483647]
    long long	8	    -2^63 ÷ 2^63 - 1, czyli przedział [-9223372036854775808, 9223372036854775807]

Typy całkowite +:
    Nazwa       Wielkość (bajty)        Zakres
    unsigned short	    2	    0 ÷ 2^16 - 1, czyli przedział [0, 65535]
    unsigned int	    4	    0 ÷ 2^32 - 1, czyli przedział [0, 4294967295]
    unsigned long	    4	    0 ÷ 2^32 - 1, czyli przedział [0, 4294967295]
    unsigned long long	8   	0 ÷ 2^64 - 1, czyli przedział [0, 18446744073709551615]

Typy rzeczywiste / zmiennoprzecinkowe:
    Nazwa       Wielkość (bajty)        Zakres
    float	    4	    `pojedyncza precyzja – dokładność 6 - 7 cyfr po przecinku
    double	    8	    podwójna precyzja – dokładność 15 - 16 cyfr po przecinku
    long double	12	    liczby z ogromną dokładnością - 19 - 20 cyfr po przecinku

Typy logiczne – TAK lub NIE:
    Nazwa       Wielkość (bajty)        Zakres
    bool	    1                       true (1) lub false (0)

Typy znakowe – znaki z klawiatury:
    Nazwa       Wielkość (bajty)        Zakres
    char	        1	                -128 ÷ 127
    unsigned char	1	                0 ÷ 255

Typy łańcuchowe – łańcuch znaków – napisy – wielkość skalowalna:
    Nazwa       Wielkość (bajty)        Zakres
    string      *                       *
    #include <string>

#########################################################################

DEKLAROWANIE, INICJALIZOWANIE, DEFINICJA:
    – typ_zmiennej nazwa_zmiennej; // Deklaracja – przydzielenie pamięci
    – nazwa_zmiennej = wartość; // Inicjalizacja – nadanie wartości

    – typ_zmiennej nazwa_zmiennej = wartość; // Definicja = Deklaracja + Inicjalizacja
        int wiek;   ->   wiek = 7,
        int wiek, ile, itd;
        int wiek = 7;
        float wysokosc = 7.007; // Kropka .
        char znak = 't'; // Pojedynczy cudzysłów
        string nazwa = "Mateusz Mróz"; // Nie wyświetli polskich liter, ale przy wprowadzaniu cin>>x; wyświetli

#########################################################################

DZIAŁANIA i OPERATORY:
Operatory arytmetyczne:
    +	Dodanie	        2 + 2 = 4
    -	Odejmowanie	    5 - 2 = 3
    *	Mnożenie	    3 * 3 = 9
    /	Dzielenie	    22 / 8 = 2.75 // int 2, float 2.75
    %	Moduł / Reszta z dzielenie  22 % 8 = 6

       **  Wykładnik potęgowy  2 ** 3 = 8 // Python
       //	Dzielenie całkowite	22 // 8 = 2 // Python

Operatory przypisania wartości:
    =   Przypisanie wartości z lewej do prawej; znaczenie:  i=1;
    +=  Dodawanie; znaczenie:   x = x + y;
    -=  Odejmowanie; znaczenie: x = x - y;
    *=  Mnożenie; znaczenie:    x = x * y;
    /=  Dzielenie; znaczenie:   x = x / y;
    %=  Moduł / Reszta z dzielenie  x = x % y;

Operatory inkrementacji i dekrementacji:
    ++  Inkrementacja; znaczenie: i=i+1;
    --  Dekrementacja; znaczenie: i=i+1;

Operatory porównania:
    !   Zaprzeczenie; znaczenie:    x ! y;
    ==  Równy; znaczenie:           x == y;
    !=  Różny; znaczenie:           x != y;
    <   Mniejszy; znaczenie:        x < y;
    >   Większy; znaczenie:         x > y;
    <=  Mniejszy równy; znaczenie:  x <= y;
    >=  Większy równy; znaczenie:   x >= y;

Operatory logiczne:
    !   Zaprzeczenie / Negacja  NOT ("nie"); znaczenie: x ! y;
    &&  Koniunkcja  AND ("i"); znaczenie:       x && y;
    ||  Alternatywa OR  ("lub"); znaczenie:     x || y;

#########################################################################

WPROWADZANIE ZMIENNYCH:
int liczba1, liczba2;
cout << "Podaj liczbe: \n";
cin >> liczba1;
cin >> liczba2; // Wprowadzenie zmiennych
/*lub*/ cin >> liczba1 >> liczba2;
cout << "Liczba1 wynosi: " << liczba1 << endl;
cout << liczba1 <<" i "<< liczba2 << " to liczby \n";

#########################################################################

FUNKCJE MATEMATYCZNE PODSTAWOWE – istnieją biblioteki np.: do liczb zespolonuch itd...
>> http://www.algorytm.edu.pl/biblioteki/cmath.html
>> https://www.cplusplus.com/reference/cmath/
>> https://en.wikipedia.org/wiki/C_mathematical_functions#Overview_of_functions

FUNKCJONALNOŚĆI: Funkcje trygonometryczne, hiperboliczne, wykładnicze i logarytmiczne, mocy (potęgi), błędów i gamma, zaokrąglania i reszty, manipulacji zmiennoprzecinkowych, minimum, maksimum, różnicy i inne: wartoć bezwzględna, stałe matematyczne itp.

#include <cmath> // Standard C++
#include <math.h> // Standard C
// Działają tak samo w C++ - zaczynają się od <c*(nazwa)> lub bez c* i na końcu *.h <(nazwa).h>

#########################################################################

PODSTAWOWE:
Potęgowanie:
    pow(x,y)        Potęgowanie -> x^y
    sqrt(x)         Pierwiastek kwadratowy x^(1/2)
    cbrt(x)         Pierwiastek trzeciego stopnia x^(1/3)
    pow(x,1.0/n.0)  Pierwiastek n-tego stopnia -> x^(1/n) // W tej postaci bo zmienna double
    hypot(x,y)      Przeciwprostokątna trójkąta prostokątnego -> (a^2 + b^2 = c^2) -> c
        d = sqrt (pow(x_2 - x_1, 2) + pow(y_2 - y_1, 2));    Długość odcinka
Inne:
    abs(x)          Wartość bezwzględna z x
    div(x,y)        Iloraz i reszta z dzielenia
        div(x,y).quot   Część całkowita z dzielenia
        div(x,y).rem    Reszta z dzielenia
Logarytmy:
    log(x)          Logarytm naturalny z x
    log10(x)        Logarytm dziesiętny z x
Funkcje trygonometryczne w radianach:
    sin(x*M_PI/180.0)     Sinus x
    cos(x*M_PI/180.0)     Cosinus x
    tan(x*M_PI/180.0)     Tangens x
    1/tan(x*M_PI/180.0)   Cotangens x
Zaokrąglanie liczb:
    celi(x)     Zaokrąglenie w górę     celi(5.6) = 6
    floor(x)    Zaokrąglenie w dół      floor(5.6) = 5
    round(x)    Zaokrąglenie do najbliższej liczby całkowitej   round(5.6) = 6
    trunc(x)    Wycinanie po przecinku  trunc(5.6) = 5
Stałe matematyczne:
    M_PI        pi = 3.14
    M_E         e = 2.72
    M_LN2       Logarytm naturalny z 2
    M_ itd...   Inne stałe...
To były najważniejsze...

USTAWIENIE ZMIENNYCH STAŁYCH DLA PROGRAMU:
Typ zmiennej:
    const float pi = M_PI;  Zmienna pi stała się stałą i nie da się jej podnieść
    const float pi1 = 3.14; Zmienna pi stała się stałą i nie da się jej podnieść

USTAWIANIE PRECYZJI LICZB:
#include <iomanip>
>> https://www.cplusplus.com/reference/iomanip/
    setprecision(x)     Ustawia precyzje wyświetlania liczb !!!Wcałym programie!!!
        cout << setprecision(x) << 3.14131; -> wynik: 3.14

#########################################################################

FUNKCJA WARUNKOWA if ... else:

    – do warunków logicznych używa się – Operatorów porównywania i logicznych:
        ==,  !=,  <,  >,  <=,  >=,  !,  &&,  ||
    – instrukcje można zagnieżdżać (umieszczać jedna w drugiej)
    – w wypadku przedziałów zaczynamy do jednego z ekstremów i przesuwamy się spełniając kolejne warunki (wiek)


if – funkcja prosta – gdy jest spełniony warunek, wykona się blok kodu
    if ( warunek_logiczny )
    {
        /* code */
    }

if ... else – w zależności czy warunek jest spełniony wykonają się różne bloki kodu
    if ( warunek_logiczny )
    {
        /* code_1 */
    }
    else
    {
        /* code_2 */
    }

if ... else if (... else) – gdy else nie wystarczy i potrzebujemy sprawdzić kolejny warunek
    if ( warunek_logiczny_1 )
    {
        /* code1 */
    }
    else if ( warunek_logiczny_2 )
    {
        /* code_2 */
    }
    else
    {
        /* code_3 */
    }

PRZYKŁAD:
    if (wiek > 0)
    {   // Gdy blok kodu ma więcej niż 1 linijkę kodu { kod }
        // Funkcja zagnieżdżona
        if (wiek < 20) // Operatory logiczne i matematyczne
            cout << "młody"; // Gdy blok kodu ma 1 linijke – bez nawiasów {}
        else if (wiek < 60)
            cout << "dorosły";
        else if (wiek < 120)
            cout << "stary";
        else
            cout << "Ludzie tyle nie żyją";
    }
    else
        cout << "Ludzie tyle nie żyją";

#########################################################################

FUNKCJA WIELOKROTNEGO WYBORU switch:
    – pozwala dokonać jednego wyboru, co do wykonania pewnej części kodu (wielokrotnie w nieskończonej pętli)
    – warto zamieniać go z if ... else if, gdu warunki wyglądają tak: x == 1, x == 2, x == 3,

    switch ( zmienna )
    {
    case wartość_1: // char -> 'x':    int -> 1: // Przypadek 1
        /* code_1 */
        break;

    case wartość_2: // Przypadek 2
        /* code_2 */
        break;

    case wartość_n: // Przypadek n
        /* code_n */
        break;

    default: // Wartość domyślna, wykonywana, gdy wprowadzona zmienna nie zawiera się w poprzednich wyborach
        /* code_domuślny */
        break;
    }

PRZYKŁAD:
    switch (x)
    {
    case 1:
        {   // Gdy blok kodu ma więcej niż 1 linijka kodu { kod }
            cout << "To jest 1 \n";
            cout << "To na pewno jest 1 \n";
            break;
        }

    case 2:
        cout << "To jest 2 \n"; // Gdy blok kodu ma 1 linijkę – bez nawiasów {}
        break;

    default:
        cout << "Nie ma takiej opcji do wyboru \n";
        break;
    }

#########################################################################

TYP WYLICZENIOWY enum:
    – pozwala na zadeklarowanie stałych liczbowych
    – współgra z switch
    – przes funkcją main

    enum nazwa_wyliczenia
    {
        element_0,     // 0
        element_1,     // 1
        element_2 = 3, // 3
        element_n      // 4
    };

int main()
{
    int x;
    cin >> x;
    switch (x)
    {
    case element_0:
        /* code_1 */ cout << "LOL";
        break;
    case element_1:
        /* code_2 */
        break;
    case element_2:
        /* code_3 */
        break;
    case element_n:
        /* code_n */
        break;

    default:
        /* code_domuślny */
        break;
    }
    return 0;
}

#########################################################################

ZABEZPIECZENIE PRZED WPROWADZENIEM BŁĘDNYCH DANYCH DO PROGRAMU:
    – program użytkowniko odporny
    – sprawdzanie, czy odcieło dane i czy nie zaśmieca bufora
    – sprawdzenie, czy wprowadzane dane zgadzają się z typem zmiennej do których chcemy je przypisać

string -> koniec wprowadzenia po <SPACJA> lub <ENTER> – reszta zaśmieca bufor
char -> pobiera tylko jeden znak, reszta zaśmieca bufor

    string / char x;
    cin >> x;
    cin.sync();     // Czyszczenie buforu strumienia
    /*lub*/ cin.ignore(10000, '\n');    // Ignorowane (czyszczenie do dalszych) 10000 znaków z bufora aż do \n

char
    #include <>
        isdigit();  Czy znak jest cyfrą
        isalpha();  Czy znak jest literą


int -> błąd wprowadzenia tekstu zamiast liczby
float -> błąd wprowadzenia tekstu zamiast liczby, błąd napisania , zamiast .

    int / float x;
    cin >> x;
    // Jeśli cin napotka flage błędu, coś co nie jest liczbą
    if (!cin)  // = (cin.good() == false)
    {
        cout << "Nie wprowadzono liczby! \n";
        cin.clear(); // Czyszczenie flagi błędu
    }
    else
        cout << "Wszystko gra! " << x << endl;
    cin.sync(); /*lub*/ // cin.ignore(10000, '\n');


PRZYKŁAD:
    string / char x;
    cin >> x;
    cin.sync();  /*lub*/ // cin.ignore(10000, '\n');

    int / float x;
    do
    {
        cin.clear();
        cin.sync();
        cin >> x;
    } while (!cin);

    lub

    int / float x;
    cin >> x;
    cin.sync();
    while (!cin)
    {
        cin.clear();
        cin.sync();
        cin >> x;
    }

#########################################################################

PĘTLE:
    – stosowane przy powtarzaniu bloku kodu określoną liczbe razy
        – inicjalizacja – inicjalizuje zmienną – wykonywane tylko raz
        – warunek – spełniony = wykonanie, niespełniony = zakończenie
        – aktualizacja – aktualizuje wartość zainicjalizowanych zmiennych i ponownie sprawdza stan

for – pętla

    for( inicjalizacja; warunek; aktualizacj ) // warunek for (;;) pętla nieskończona
    {
        /* code */
    }

PRZYKŁAD:
    for (int i = 0; i <= 5; i++)
    {
        cout << i;
    }


while – pętla

    while( warunek )
    {
        instrukcja;
        aktualizaczja;
    }

PRZYKŁAD:
    int i = 0;
    while (i <= 5)
    {
        cout << i;
        i++;
    }


do...while – pętla

    do
    {
        /* code */
        aktualizaczja;
    } while ( warunek );

PRZYKŁAD:
    int i = 0;
    do
    {
        cout << i;
        i++;
    } while(i <= 5);

#########################################################################
