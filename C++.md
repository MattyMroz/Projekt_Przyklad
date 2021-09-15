# C++ składnia + biblioteki

> Kroki\_Poznania – Taksonomia_Blooma https://bit.ly/3sD2XYA  1.Wiedza 2.Rozumienie 3.Zastosowanie 4.Analiza 5.Synteza 6.Ocenianie


## Konfiguracja IDE 

INSTALACJA – MinGW i Visual Studio Code  
https://youtu.be/jla3qEnAFx0  
https://nuwen.net/mingw.html  
https://code.visualstudio.com/


## Rozszerzenia plików
>**C++** -> plik`.cpp` / (plik`.c` język C)  
**Pliki nagłówkowe** -> plik`.hpp` / (plik`.h`język C, działa też z C++)


## Uruchamianie programu
>`g++ program1.cpp -o p1` - Stworzenie pliku wykonującego `p1.exe`

>`g++ *.cpp -o p1` - Stworzenie pliku wykonującego `p1.exe` dla programu obiektowego, (wywołuje wszystkie pliki bieżącego folderu, (przejdź do niego poleceniem **cd**)) – 1 folder (`src`) = jedna funkcja główna + pod funkcje i inne pliki

>`./p1`  - Uruchomienie pliku `p1.exe`


## Szablon podstawowy !!!

```C++
#include <iostream>
using namespace std;

int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
```
```C++
OMÓWIENIE:
#include <iostream> // Biblioteka – udostępnia różnorakie funkcje programowi – łatwość
using namespace std; // Użycie standardowej przestrzeni nazw bo inaczej trzeba ciągle powtarzać std::cout itp.

int main(){} // Funkcja główna – obowiązkowa do działania

    cout << "Hello world!" <<endl; // Komunikaty w terminalu + zakończenie linii
    cout << "Hello world! \n"; // Komunikaty w terminalu + zakończenie linii
    cout << zmienna; // Wyprowadzenie zmiennej w terminalu
    return 0; // Funkcja zwraca 0 – nic
```

## Szablon plików projektu !!!
```C++
main.cpp - główny:

#include <iostream>
#include "projekt.hpp"
using namespace std;

int main()
{
	// Code wywołanie funkcji
    return 0;
}
```
```C++

projekt.hpp - nagłówkowy:

#if !defined(_PROJEKT_HPP_)
#define _PROJEKT_HPP_

// Code klasy

#endif // _PROJEKT_HPP_
```
```C++
projekt.cpp = źródłowy:

#include <iostream>
#include "projekt.hpp"
using namespace std;

// Code metody klas

```

## Wprowadzenie C ++

#### Komentarze
>Komentarze - notatka dla programisty - narzędzie debugujące  
>Można za/odkomentować skryptem -> Zaznaczenie -> `Ctrl + /`
```C++
// Komentarz jednoliniowy

/*
	Komentarz wielowierszowy
	Komentarz wielowierszowy
*/
```



### Zmienne, literały i stałe
#### Zmienne
>**Zmienna** - kontener do przechowywania danych.<br>Aby wskazać obszar przechowywania, każdej zmiennej należy **nadać niepowtarzalną nazwę** (identyfikator).<br>
Wartość zmiennej można zmienić, stąd nazwa **zmiennej** .

>**Zasady nazywania zmiennej**
>- Nazwa zmiennej może zawierać tylko litery, cyfry i podkreślenie `_`.
>- Nazwa zmiennej nie może zaczynać się od liczby.
>- Nazwy zmiennych nie powinny zaczynać się wielką literą.
>- Nazwa zmiennej nie może być słowem kluczowym . Na przykład `int` to słowo kluczowe używane do oznaczania liczb całkowitych.
>- Nazwa zmiennej może zaczynać się od podkreślenia. Jednak nie jest to uważane za dobrą praktykę.


#### Literały języka

>**Literały** to dane używane do przedstawiania stałych wartości. Można ich używać bezpośrednio w kodzie. Np.: `1`, `2.5`, `'c'`itd.

>1. Liczby całkowite `1` - w różnych układach liczbowych
>2. Liczby zmiennoprzecinkowe `2.5`- w różnych układach liczbowych
>3. Znaki `F` `}` `a` itd. 
>```C++
>\b	- Backspace - usunięcie ostatniego znaku
>\f	- Form feed - wysuw strony - ?Linux? - przenosi aktywną pozycję do pozycji początkowej na początku następnej strony logicznej - cokolwiek to znaczy
>\n	- Nowa linia
>\r	- Powrót do początku linii
>\t	- Tabulator
>\v	- Zakładka pionowa - ?Linux? -niedziałan na wszystkich terminalach
>\\	- Ukośnik wsteczny
>\'	- Pojedynczy cudzysłów
>\"	- Podwójny cudzysłów
>\?	- Znak zapytania
>\0	- Znak zerowy
>```
>4. Sekwencje ucieczki `\n`
>5. Łańcuch znaków 
>```C++
>"good"	- stała łańcuchowa
>""		- stała łańcuchowa zerowa
>" "		- stała łańcuchowa sześciu białych znaków
>"x"		- stała łańcuchowa o pojedynczym znaku
>"Earth is round\n"	- wypisuje łańcuch z nową linią
>```


#### Stałe

>W C ++ możemy tworzyć zmienne, których wartości nie można zmienić. W tym celu używamy `const` słowa kluczowego, np.:
>```c++
>const int LIGHT_SPEED = 299792458;
LIGHT_SPEED = 2500 // Error! LIGHT_SPEED is a constant.
>```
>Stałą można również utworzyć za pomocą `#define`dyrektywy preprocesora - `C++ Macros.`




### Typy zmiennych / danych
>Wielkość typu może różnić się zależnie od systemu operacyjnego?!   
>** Modyfikatory typu** - zmieniają przedział liczbowy określonego typu:   
>- `signed` - zmienia przedział typu na liczby dodatnie i ujemne: -1, 0, 1 - domyślnie
>- `unsigned` - zmienia przedział typu tylko na liczby dodatnie: 0, 1
>- `short` - typ ma mniejszy rozmiar
>- `long` - typ ma większy rozmiar

>**Typy całkowite** - przechowuje liczby całkowite np.: -1 , 0, 1

|Typ danych / zmiennych|Rozmiar <br> w bajtach|Zakres|Przykład zastosowania|
|-|-|-|-|
|`short`|2|[-32768, 32767]|`short` x = -1;|
|`int`|4|[-2147483648, 2147483647]|`int` x = -11;|
|`long`|4|[-2147483648, 2147483647]|`long` x = -111;|
|`long long`|8|[-9223372036854775808, 9223372036854775807]|`long long` x = -1111;|
|`unsigned short`|2|[0, 65535]|`unsigned short` x = 1;|
|`unsigned int`|4|[0, 4294967295]|`unsigned int` x = 11;|
|`unsigned long`|4|[0, 4294967295]|`unsigned long` x = 111;|
|`unsigned long long`|8|[0, 18446744073709551615]|`unsigned long long` x = 1111;|

>**Typy rzeczywiste / zmiennoprzecinkowe** -  przechowuje liczby rzeczywiste np.: -64.74, 0, 134.64534  

|Typ danych / zmiennych|Rozmiar <br> w bajtach|Zakres|Przykład zastosowania|
|-|-|-|-|
|`float`|2|pojedyncza precyzja - dokładność 6 - 7 cyfr po przecinku|`float` x = 1.11;|
|`double`|8|podwójna precyzja - dokładność 15 - 16 cyfr po przecinku|`double` x = 1.1111;|
|`long double`|12|liczby z ogromną dokładnością - 19 - 20 cyfr po przecinku|`long double` x = 1.111111;|

>**Typy znakowe** - przechowuje znaki z klawiatury - oprócz poniższy istnieją jeszcze: `har8_t`, `char16_t`, `char32_t` -> cholera wie po co

|Typ danych / zmiennych|Rozmiar <br> w bajtach|Zakres|Przykład zastosowania|
|-|-|-|-|
|`char`|1|[-128, 127]|`char` x = 'h';|
|`unsigned char`|1|[0, 255]|`unsigned char` x = 'h';|
|`wchar_t`|2|szeroki char|`wchar_t` x = L'ם';|

>**Typy łańcuchowe** - łańcuch znaków - napisy - wielkość skalowalna

|Typ danych / zmiennych|Rozmiar <br> w bajtach|Zakres|Przykład zastosowania|
|-|-|-|-|
|`string`|*|*|`string` x = "Ciąg znaków?!"|


>**Typy logiczne** - używane w instrukcjach warunkowych i pętlach - wartości TAK lub NIE

|Typ danych / zmiennych|Rozmiar <br> w bajtach|Zakres|Przykład zastosowania|
|-|-|-|-|
|`bool`|1|[true (1) lub false (0)|`bool` x = false;|

>**Typy puste** - wskazuje na brak danych - oznacza „nic” lub „brak wartości”

|Typ danych / zmiennych|Rozmiar <br> w bajtach|Zakres|Przykład zastosowania|
|-|-|-|-|
|`void`|0|-|Używany w funkcjach i wskaźnikach|


> **Pochodne typy danych** - typy danych, które pochodzą z podstawowych typów danych, są typami pochodnymi. Na przykład: tablice, wskaźniki, typy funkcji, struktury itp.


### Podstawowe operecje I/O

```C++
#include <iostream>
using namespace std;

int main()
{
    int liczba1, liczba2;
    cout << "Podaj liczbe: \n";
    cin >> liczba1;
    cin >> liczba2; // Wprowadzenie zmiennych
    cout << "Liczba1 wynosi: " << liczba1 << endl;

    /*lub*/ cin >> liczba1 >> liczba2; // Wprowadzenie wielu zmiennych
    cout << liczba1 << " i " << liczba2 << " to liczby \n";
	return 0;
}
```

### Konwersja typu
####  Niejawna
> Konwersja typu, która jest wykonywana automatycznie przez kompilator, jest nazywana **niejawną konwersją typu**. Ten typ konwersji jest również nazywany** konwersją automatyczną.**
```C++
    // Przypisanie liczby całkowitej na zmiennoprzecinkową
    int num_int = 9;
    double num_double;
    num_double = num_int;

    cout << "num_int = " << num_int << endl;
    cout << "num_double = " << num_double << endl;

		Wynik:
			num_int = 9
			num_double = 9
    /* lub */

    // Przypisanie liczby zmiennoprzecinkowej na całkowitą
    int num_int;
    double num_double = 9.99;
    num_int = num_double;

    cout << "num_int = " << num_int << endl;
    cout << "num_double = " << num_double << endl;
	
Wynik:
num_int = 9
num_double = 9.99

```
##### Utrata danych
>Konwersja z jednego typu danych na inny jest podatna na **utratę danych**. Dzieje się tak, gdy dane większego typu są konwertowane na dane mniejszego typu.
![Alt|400x700](https://cdn.programiz.com/sites/tutorial2program/files/cpp-type-conversion.png)



####  Jawna
>**Odlewanie typu - notacja odlewana**  
(typ_danych)wyrażenie;
```C++
	int num_int;
	double num_double = 3.56;

	num_int = (int)num_double; // konwersja z int na double
    cout << "num_int = " << num_int << endl;
```
>**Odlewanie stylu funkcji - Rzutowanie typów**  
>data_type(wyrażenie);
```C++
	int num_int;
	double num_double = 3.56;

	num_int = int(num_double); // konwersja z int na double
    cout << "num_int = " << num_int << endl;
```
> **Przypisanie**
```C++
    double num_double = 3.56;
    cout << "num_double = " << num_double << endl;

    int num_int1 = (int)num_double; // przypisanie odlewania typu
    cout << "num_int1 = " << num_int1 << endl;

    int num_int2 = int(num_double); // przypisanie odlewania stylu funkcji 
    cout << "num_int2 = " << num_int2 << endl;
```
> Operatory konwersji typów - później:  
> `static_cast`, `dynamic_cast`,  `const_cast`,  `reinterpret_cast`
### Operatory
```C++
DZIAŁANIA i OPERATORY:
Operatory arytmetyczne:
    +	Dodanie	        2 + 2 = 4
    -	Odejmowanie	    5 - 2 = 3
    *	Mnożenie	    3 * 3 = 9
    /	Dzielenie	    22 / 8 = 2.75 // int 2, float 2.75
    %	Moduł / Reszta z dzielenie  22 % 8 = 6

Operatory przypisania wartości:
    =   Przypisanie wartości z lewej do prawej; znaczenie:  i=1;
    +=  Dodawanie; znaczenie:   x = x + y;
    -=  Odejmowanie; znaczenie: x = x - y;
    *=  Mnożenie; znaczenie:    x = x * y;
    /=  Dzielenie; znaczenie:   x = x / y;
    %=  Moduł / Reszta z dzielenie  x = x % y;

Operatory inkrementacji i dekrementacji:
    ++  Inkrementacja; znaczenie: i=i+1; // i++ lub ++i
    --  Dekrementacja; znaczenie: i=i+1; // i-- lub --i

Operatory porównania / relacji:
    !   Zaprzeczenie; znaczenie:    x ! y;
    ==  Równy; znaczenie:           x == y;
    !=  Różny; znaczenie:           x != y;
    <   Mniejszy; znaczenie:        x < y;
    >   Większy; znaczenie:         x > y;
    <=  Mniejszy równy; znaczenie:  x <= y;
    >=  Większy równy; znaczenie:   x >= y;

Operatory logiczne - działają po kolei do lewej - zwracają bool -> T/F:
    !   Zaprzeczenie / Negacja  NOT ("nie"); znaczenie: x ! y;
    &&  Koniunkcja  AND ("i"); znaczenie:       x && y;
    ||  Alternatywa OR  ("lub"); znaczenie:     x || y;
    
	bool result;
	result = (3 != 5) && (3 < 5);     // true

Operatory bitowe - !!!!!!!!!!! Przykłady http://webmaster.helion.pl/index.php/kjs-cechy-jezyka/kjs-operatory/kjs-operatory-bitowe
	&	Binarne AND
	|	Binarny OR
	^	Binarny XOR
	~	Uzupełnienie binarnego One
	<<	Binarne Shift w lewo
	>>	Binary Shift w prawo
	
Inne operatory
	sizeof	zwraca rozmiar typu danych	sizeof(int); // 4

	?: 		zwraca wartość na podstawie warunku	string result = (5 > 0) ? "even" : "odd"; // "even"

	&		reprezentuje adres pamięci operandu	# // address of num

	.		uzyskuje dostęp do elementów składowych zmiennych struktur lub obiektów klas	s1.marks = 92;

	->		używane ze wskaźnikami w celu uzyskania dostępu do zmiennych klasy lub struktury	ptr->marks = 92;

	<<		wypisuje wartość wyjściową	cout << 5;
	>>		pobiera wartość wejściową	cin >> num;
```
## Kontrola przepływu C ++
###  If ... else

>**Funkcja warunkowa** `if`,` if ... else`, `if ... else if ... else` i oraz zwgnieżdżony if
>- Od spełnienia warunków zależy który blok kodu zastanie wykonany
>- Do warunków logicznych używa się operatorów
>- Instrukcje można **zagnieżdżać** (umieszczać jedna w drugiej)
>- W wypadku przedziałów zaczynamy do** jednego z ekstremów**   
>i przesuwa się spełniając kolejne warunki np.: przedział wiekowe

>`if`  - funkcja prosta - gdy spełniony jest warunek, wykona się blok kodu
```C++
    if ( warunek_logiczny )
    {
        /* code */
    }
```
>`if ... else` - w zależności czy warunek jest spełniony wykonają się różne bloki kodu
```C++
    if ( warunek_logiczny )
    {
        /* code_1 */
    }
    else
    {
        /* code_2 */
    }
```
>`if ... else if ( ... else)` - gdy else nie wystarczy i potrzebujemy sprawdzić kolejny warunek
```C++
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
```
>**Zagnieżdżenie** + PRZYKŁAD
```C++
    if (wiek > 0)
    {   // Gdy blok kodu ma więcej niż 1 linijkę kodu { kod w nawiasach }
        // Funkcja zagnieżdżona
        if (wiek < 20) // Operatory logiczne i matematyczne
            cout << "młody"; // Gdy blok kodu ma 1 linijke - bez nawiasów {}
        else if (wiek < 60)
            cout << "dorosły";
        else if (wiek < 120)
            cout << "stary";
        else
            cout << "Ludzie tyle nie żyją";
    }
    else
        cout << "Ludzie tyle nie żyją";

```
### Pętla for

>**Pętle**
>- Stosowane przy powtarzaniu bloku kodu określoną liczbe razy
>   - Inicjalizacja - inicjalizuje zmienną - wykonywane tylko raz
>   - Warunek - spełniony = wykonanie, niespełniony = zakończenie
>   - Aktualizacja - aktualizuje wartość zainicjalizowanych zmiennych i ponownie sprawdza ich stan

```C++
    for( inicjalizacja; warunek; aktualizacj ) // warunek for (;;) - pętla nieskończona
    {
        /* code */
    }

PRZYKŁAD_1:
    for (int i = 0; i <= 5; i++) // lub ++i <- XD
    {
        cout << i;
    }

PRZYKŁAD_2 - pętla zagnieżdżona:
    int x;
    cin>>x;

    for (int i = 1; i <= x; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            if (i==x || j == 1 || j == i)
            {
                cout<<"*";
            }
            else
            {
                cout<<" ";
            }
        }
        cout<<endl;
    }
Wynik:
4
*
**
* *
****
```

### Pętla while
```C++
    while( warunek ) // warunek = while( true ) - pętla nieskończona
    {
        instrukcja;
        aktualizacja;
    }

PRZYKŁAD:
    int i = 0;
    while (i <= 5)
    {
        cout << i;
        i++;
    }
```
### Pętla  do ... while
```C++
    do
    {
        /* code */
        aktualizacja;
    } while ( warunek );

PRZYKŁAD:
    int i = 0;
    do
    {
        cout << i;
        i++;
    } while(i <= 5); // int = 0; i warunek = while( i = 0 ) - pętla nieskończona
```

### Break
> Instrukcja `break`  kończy pętlę, gdy zostanie napotkana, występuje   
> w funkcji wielokrotnego wyboru `switch`
```C++
	break;
```
```C++
PRZYKŁAD_1:
    for (int i = 1; i <= 5; i++)
    {
        if (i == 3)
        {
            break;
        }
        cout << i << endl;
    }

Wynik:
1 
2
```
```C++
PRZYKŁAD_2:
    while (true)
    {
        cout << "Wczytaj liczbe: ";
        cin >> number;

        if (number < 0)
        {
            break;
        }

        sum += number;
    }
    cout << "Suma wynosi " << sum << endl;

Wynik:
Wpisz liczbe: 1
Wpisz liczbe: 2
Wpisz liczbe: 3
Wpisz liczbe: -5
Suma wynosi 6
```
```C++
PRZYKŁAD_3:
    int number;
    int sum = 0;

    for (int i = 1; i <= 3; i++)
    {
        for (int j = 1; j <= 3; j++)
        {
            if (i == 2)
            {
                break;
            }
            cout << "i = " << i << ", j = " << j << endl;
        }
    }

Wynik:
i = 1, j = 1
i = 1, j = 2
i = 1, j = 3
i = 3, j = 1
i = 3, j = 2
i = 3, j = 3
```
### Continue

> Instrukcja `continue`  służy do pominięcia bieżącej iteracji pętli, a sterowanie programem przechodzi do następnej iteracji.
```C++
	continue;
```
```C++
PRZYKŁAD_1:
    for (int i = 1; i <= 5; i++)
    {
        if (i == 3)
        {
            continue;
        }

        cout << i << endl;
    }

Wynik:
1
2
4
5 
```
```C++
PRZYKŁAD_2:
    int sum = 0;
    int number = 0;

    while (number >= 0)
    {
        sum += number;

        cout << "Wpisz liczbe: ";
        cin >> number;

        if (number > 50)
        {
            cout << "Liczba jest większa niż 50 i nie zostanie obliczona." << endl;
            number = 0;
            continue;
        }
    }
    cout << "Suma wynosi " << sum << endl;

Wynik:
Wpisz liczbe: 12
Wpisz liczbe: 0
Wpisz liczbe: 2
Wpisz liczbe: 30
Wpisz liczbe: 50
Wpisz liczbe: 56
Liczba jest większa niż 50 i nie zostanie obliczona.
Wpisz liczbe: 5
Wpisz liczbe: -3
Suma wynosi 99 

```
```C++
PRZYKŁAD_3:
    int number;
    int sum = 0;

    for (int i = 1; i <= 3; i++)
    {
        for (int j = 1; j <= 3; j++)
        {
            if (j == 2)
            {
                continue;
            }
            cout << "i = " << i << ", j = " << j << endl;
        }
    }

Wynik:
i = 1, j = 1
i = 1, j = 3
i = 2, j = 1
i = 2, j = 3
i = 3, j = 1
i = 3, j = 3
```
### Switch ... case i enum
>`switch` - funkcja wielokrotnego wyboru
>- Pozwala dokonać jednego wyboru, co do wykonania pewnego bloku kodu (wielokrotnie w nieskończonej pętli)
>- Warto zamieniać go z if ... else if, gdy warunki wyglądają tak: `x == 1, x == 2, x == 3`, itd.
```C++
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
        cout << "To jest 2 \n"; // Gdy blok kodu ma 1 linijkę - bez nawiasów {}
        break;

    default:
        cout << "Nie ma takiej opcji do wyboru \n";
        break;
    }
```

>`enum` - typ wyliczeniowy
>- pozwala na zadeklarowanie stałych liczbowych
>- współgra z switch
>- przed funkcją main
>- numeracja zaczyna się od 0 - można przypisać inną
> - patrz więcej **Wyliczenie**

```C++
    enum nazwa_wyliczenia
    {
        element_0,     // 0 // Inna nazwa - element_0 dla elementu o nr 0
        element_1,     // 1
        element_2 = 3, // 3 -> Przypisanie innej wartości elementowi
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

WYJAŚNIENIE: Teraz do wyboru switch można użyć zarówno int jaki i nazwy stałej liczbowej ktorej można nadać dowolną nazwę i która jest odzwierciedleniem liczby int np.: nazwy kolorów

Przykładowy wynik:
element_0
LOL
	// lub
0
LOL
```
### Goto
>Instrukcja `goto` służy do zmiany normalnej kolejności wykonywania programu poprzez przekazanie kontroli do innej części programu
> - Należy unikać instrukcji przejścia `goto`, ponieważ sprawia, że logika programu jest złożona i zagmatwana
```C++
goto nazwa_etykiety; // Przejście do etykiety, pominięcie bloków kodu po goto nazwa_etykiety;
	kod ...
nazwa_etukiety: // Po przejściu do etykiety wykonywany są bloki kodu poniżej
	inny blok kodu ...

PRZYKŁAD:
    float num, srednia, sum = 0.0;
    int i, n;

    cout << "Maksymalna liczba wejsc: ";
    cin >> n;

    for (i = 1; i <= n; ++i)
    {
        cout << "Wpisz n" << i << ": ";
        cin >> num;

        if (num < 0.0)
        {
            goto jump; // Sterowanie programem przejdź do jump:
        }
        sum += num;
    }

jump:
    srednia = sum / (i - 1);
    cout << "\nSrednia = " << srednia;

Wynik:
Maksymalna liczba wejsc: 10
Wpisz n1: 2.3
Wpisz n2: 5.6
Wpisz n3: -5,6
Średnia = 3,95
```

## Funkcje C++
### Funkcje

> **Funkcja** to blok kodu o nadanej nazwie, który wykonuje określone zadanie
> - Polega na **rozłożeniu problemu** na mniejsze części
> - Powoduje, że cały program jest **łatwy** do zrozumienia
> - Napisany blok kodu **można ponownie używać**

>** Własności funkcji:**
> - Posiada własną nazwę
>   -** Nazwa** powinna określać **zadanie funkcji, czasownik, bez spacji**
> - Może posiadać** listę argumentów** potrzebną do działania funkcji
> - Może **zwracać wartość**

>Istnieją **dwa rodzaje funkcji**:
>- **Standardowe funkcje biblioteczne**: wstępnie zdefiniowane w C ++
>- **Funkcja zdefiniowana** / utworzona przez użytkownika

#### Deklaracja funkcji
>**Deklaracja funkcji** - ciało funkcji wykonujące operacje
```C++
typ_zwracanej_zmiennej nazwa_funkcji( typ_arg1 arg1, typ_arg2 arg2, ... )
	{
		// code
	}
	
PRZYKŁAD:
void witaj_swiecie()
{
    cout << "Hello World";
}
```

#### Wywołanie funkcji
>** Wywołanie funkcji** - po nazwie do pracy (jak koleżankę na studiach - po imieniu)
```C++
int main()
{
    nazwa_funkcji(arg1, arg2);
}

PRZYKŁAD - Wywołanie napisu :
// Deklaracja funkcji
void witaj_swiecie()
{
    cout << "Hello World";
}
// Wywoływanie funkcji
int main()
{
    witaj_swiecie();
    return 0;
}
```

#### Parametry / argumenty funkcji
> **Parametry / argumenty funkcji** - deklaracja typu skopiowanych danych i nadanie im nowej nazwy używanej w danej funkcji - więcej o tym później
```C++
PRZYKŁAD_1:

void printNum(int num) // Kopia wartości, nadanie jej innej nazwy i operacja na niej
{
    cout << num;
}

int main()
{
    int n = 7;
    printNum(n); // Wysłanie do funkcji wartości do pracy
    return 0;
}

PRZYKŁAD_2:
void displayNum(int n1, float n2) // Deklaracja kilku parametrów
{
    cout << "Liczba int to " << n1;
    cout << "Liczba double to " << n2;
}

int main()
{
    int num1 = 5;
    double num2 = 5.5;

    displayNum(num1, num2); // Wysłanie kilku wartości - odczytywane są one pokolei

    return 0;
}
```
#### Return - instrukcja zwrotu 
>`return x;` - zwraca wartość obliczoną przez funkcje, typ wartości równa się typ_zwracanej_zmiennej na początku deklarowania funkcji
```C++
PRZYKŁAD:
int add(int a, int b)
{
    return (a + b); Instrukcja zwrotu - zwraca sume argumentów
}

int main()
{
    int sum;
    sum = add(100, 78); // Zwraca sume 100 + 78, czyli int 178, który zostaje przypisany do zmiennej sum

    cout << "100 + 78 = " << sum << endl;

    return 0;
}
```
#### Prototyp funkcji
>**Prototyp funkcji** - deklarowanie istnienia ciała funkcji w dalszej części programu
>- Zwiększa czytelność - gdy deklarowana funkcja jest długa
>- Niezbędny przy deklaracji funkcji - po funkcji głównej (main)
```C++
void add(int, int); // Prototyp funkcji

int main()
{
    add(5, 3); // Wywoływanie funkcji
    return 0;
}

void add(int a, int b) // Deklaracja funkcji
{
    cout << (a + b);
}
```
#### Funkcje biblioteki
>Funkcje biblioteczne to wbudowane funkcje w językach programowania
>- Programiści mogą używać funkcji bibliotecznych, wywołując je bezpośrednio,  nie muszą samodzielnie pisać funkcji.
>- Aby korzystać z funkcji bibliotecznych, zwykle musimy dołączyć plik nagłówkowy, w którym te funkcje biblioteczne są zdefiniowane
>- Na przykład, aby używać funkcji matematycznych, takich jak `sqrt()`i `abs()`, musimy dołączyć plik nagłówkowy `cmath` - więcej w Biblioteki w C++

```C++
#include <iostream>
#include <cmath> // Dodanie biblioteki matematycznej
using namespace std;

int main()
{
    double num, pierwiastek;

    num = 25.0;
    pierwiastek = sqrt(num); // Wywołanie funkcji

    cout << "Pierwiastek kwadratowy z " << num << " = " << pierwiastek;

    return 0;
}
```
### Typy funkcji
>Wszystkie poniższe programy są poprawne i dają ten sam wynik
>- Nie ma zasad, którą należy wybrać - wszystko zależy od sytuacji i sposobu rozwiązania problemu :D
#### Funkcja bez argumentu i bez wartości zwracanej
> Cały program zawiera się w funkcji, main tylko wywołuje
```C++
void prime()
{
    int num, i, flag = 0;

    cout << "Wpisz dodatnia liczbe calkowita, ktora chcesz sprawdzic: ";
    cin >> num;

    for (i = 2; i <= num / 2; ++i)
    {
        if (num % i == 0)
        {
            flag = 1;
            break;
        }
    }

    if (flag == 1)
    {
        cout << num << " nie jest liczba pierwsza.";
    }
    else
    {
        cout << num << " jest liczba pierwsza.";
    }
}

int main()
{
    prime();
    return 0;
}
```

#### Funkcja bez argumentu, ale zwracająca wartość
> Funkcja main wywołuje funkcje w celu pobrania wartości
```C++
int prime();

int main()
{
    int num, i, flag = 0;


    num = prime(); // Żaden argument nie jest przekazywany do prime ()
    for (i = 2; i <= num / 2; ++i)
    {
        if (num % i == 0)
        {
            flag = 1;
            break;
        }
    }

    if (flag == 1)
    {
        cout << num << " nie jest liczba pierwsza.";
    }
    else
    {
        cout << num << " jest liczba pierwsza.";
    }
    return 0;
}

int prime() // Zwracany typ funkcji to int
{
    int n;

    printf("Wpisz dodatnia liczbe calkowita, ktora chcesz sprawdzic: ");
    cin >> n;

    return n;
}
```

#### Funkcja z argumentem, ale bez wartości zwracanej
> Funkcja jest funkcjią obliczeniową dającą pełną odpowiedź dla zapytania funkcji main
```C++
void prime(int n);

int main()
{
    int num;
    cout << "Wpisz dodatnia liczbe calkowita, ktora chcesz sprawdzic: ";
    cin >> num;

    prime(num); // Argument num jest przekazywany do funkcji prime ()
    return 0;
}

// Nie ma wartości zwracanej do wywołania funkcji. W związku z tym zwracany typ funkcji jest nieważny
void prime(int n)
{
    int i, flag = 0;
    for (i = 2; i <= n / 2; ++i)
    {
        if (n % i == 0)
        {
            flag = 1;
            break;
        }
    }
    if (flag == 1)
    {
        cout << n << " nie jest liczba pierwsza.";
    }
    else
    {
        cout << n << " jest liczba pierwsza.";
    }
}
```

#### Funkcja z argumentem i wartością zwracaną
> Funkcja jest funkcją obliczeniową zwracającą wartość dla funkcji main
```C++
int prime(int n);

int main()
{
    int num, flag = 0;
    cout << "Wpisz dodatnia liczbe calkowita, ktora chcesz sprawdzic: ";
    cin >> num;

    flag = prime(num); // Numer argumentu jest przekazywany do funkcji check ()

    if (flag == 1)
        cout << num << " nie jest liczba pierwsza.";
    else
        cout << num << " jest liczba pierwsza.";
    return 0;
}

int prime(int n) // Ta funkcja zwraca wartość całkowitą
{
    int i;
    for (i = 2; i <= n / 2; ++i)
    {
        if (n % i == 0)
            return 1;
    }

    return 0;
}
```

### Przeciążenie funkcji
> **Przeciążenie funkcji** - funkcje mogą mieć **tę samą nazwę**, jeśli **liczba i / lub typ** przekazywanych argumentów **jest różny**

```C++
Poprawne:
int test() {}
int test(int a) {}
float test(double a) {}
int test(int a, double b) {}

Błędne:
int test(int a) {}
double test(int b){}

PRZYKŁAD:
void display(int var1, double var2) // Funkcja z 2 parametrami
{
    cout << "Liczba int: " << var1;
    cout << " i liczba double: " << var2 << endl;
}

void display(double var) // Funkcja z pojedynczym parametrem typu double
{
    cout << "Liczba double: " << var << endl;
}

void display(int var) // Funkcja z pojedynczym parametrem typu int
{
    cout << "Liczba int: " << var << endl;
}

int main()
{
    int a = 5;
    double b = 5.5;

    display(a); // Wywołanie funkcji z parametrem typu int
    display(b); // wywołanie funkcji z parametrem typu double
    display(a, b); // Wywołanie funkcji z 2 parametrami

    return 0;
}
```
> ![Alt|500](https://cdn.programiz.com/sites/tutorial2program/files/cpp-function-overloading-parameters-number.png)
### Argument domyślny
>- Jeśli wywoływana jest funkcja **z domyślnymi argumentami bez przekazywania argumentów**, używane są **domyślne parametry**  
>- Jeśli jednak **argumenty są przekazywane** podczas wywoływania funkcji, **domyślne argumenty są ignorowane**

> ![Alt|600](https://cdn.programiz.com/sites/tutorial2program/files/cpp-default-parameters.png)

>-  Gdy podamy domyślną wartość parametru, wszystkie kolejne parametry również muszą mieć wartości domyślne
```C++
    // Niepoprawny
    void add(int a, int b = 3, int c, int d);

    // Niepoprawny
    void add(int a, int b = 3, int c, int d = 4);

    // Poprawny
    void add(int a, int c, int b = 3, int d = 4);
```
>- Definiowanie w prototypie
```C++
void display(char = '*', int = 3); // Lub (char c = '*', int count = 3)

int main()
{
    int count = 5;

    cout << "Nie przekazano argumentu: "; // 3 razy *
    display();

    cout << "Przekazano pierwszy argument: "; // 3 razy #
    display('#');

    cout << "Oba argumenty zostaly przekazane: "; // 5 razy $
    display('$', count);

    return 0;
}

void display(char c, int count)
{
    for (int i = 1; i <= count; ++i)
    {
        cout << c;
    }
    cout << endl;
}
```
>- Jeśli definiujemy argumenty w deklaracji to owa deklaracja funkcji musi znajdować się przed wywołaniem tej funkcji np.: przed main
```C++
void display(char c = '*', int count = 3)
{
    for (int i = 1; i <= count; ++i)
    {
        cout << c;
    }
    cout << endl;
}

int main()
{
    int count = 5;

    cout << "Nie przekazano argumentu: "; // 3 razy *
    display();

    cout << "Przekazano pierwszy argument: "; // 3 razy #
    display('#');

    cout << "Oba argumenty zostaly przekazane: "; // 5 razy $
    display('$', count);

    return 0;
}
```

### Klasa pamięci
>Zmienne w C++ mają 2 cech: **typ i klasę pamięci**
>- **Typ** przechowywanych danych
>- **Klasa pamięci** kontroluje dwie różne właściwości zmiennej:
>   - Okres istnienia -  jak długo zmienna może istnieć
>   - Zasięg - która część programu ma do niej dostęp  
>
>Wyróżniamy 4 rodzaje klas:

#### Zmienna lokalna
>**Zmienna lokalna / automatyczna** - istnieje tylko wewnątrz danej funkcji, życie zmiennej kończy się, gdy funkcja kończy działanie

```C++
int main()
{
    int var = 5; // Zmienna lokalna
    cout << var;

    return 0;
}
```
#### Zmienna globalna
**Zmienna globalna** - zdefiniowana poza wszystkimi funkcjami, jej zakras obejmuje cały program, życie zmiennej kończy się, gdy program kończy działanie

```C++
int var = 5; // Zmienna globalna

void test();

int main()
{
    cout << var << endl;
    test();
	
    return 0;
}

void test()
{
    cout << var;
}
```
#### Statyczna zmienna lokalna
> **Statyczna zmienna lokalna** - istnieje tylko wewnątrz danej funkcji, ale jej życie kończy się, gdy program kończy działanie

```C++
void test()
{
    static int var = 0; // Statyczna zmienna lokalna, podczas drugiego wywołania zmienna var już istnieje z wartością 1 i to do niej zostanie dodana 1
    ++var;

    cout << var << endl;
}

int main()
{
    test();
    test();
    return 0;
}

Wynik:
1
2
```
#### Pamięć lokalna wątku
>** Pamięć lokalna wątku** - magazyn lokalny wątku to mechanizm, za pomocą którego zmienne są przydzielane w taki sposób, że na każdy istniejący wątek przypada jedno wystąpienie zmiennej. W tym celu używane jest słowo kluczowe `thread_local` - dużo mi to mówi

### Rekurencja
> Funkcja rekurencyjna - funkcja która wywołuje samą siebie - tworzy swoje klony do obliczenia wyniku - wskutek czego jest bardziej zasobożerny niż iteracja
> - Trzeba zadbać by za każdym wywołaniem funkcji problem się redukuje
> - Przydatna wiedza z ciągów - matematyka  
> **Zalety**: kod jest krótki i przejrzysty, wymagana w przypadku problemów dotyczących struktur danych i zaawansowanych algorytmów  
>** Wady:** duże zużycie zasobów komputera, trudniejsze debugowanie
```C++
void rekurencja() // Deklaracja funkcji
{
    ... .. ...
    rekurencja(); // Funkcja wywołuje samą siebie do obliczenia
    ... .. ...
}

int main()
{
    ... .. ...
    rekurencja(); // Wywołanie funkcji
    ... .. ...
}
```
```C++
Przykład - Silnia liczby przy użyciu rekursji:

int oblicz_silnie(int);

int main()
{
    int n, silnia;

    cout << "Wpisz liczbe nieujemna: ";
    cin >> n;

    silnia = oblicz_silnie(n); // Przypisanie wartości zwracanej przez funkcję
    cout << "Silnia z " << n << " = " << silnia;
    return 0;
}

int oblicz_silnie(int n) // Deklaracja funkcji
{
    if (n > 1) // Warunek podstawowy - silnia - !0 = 1
		return n * oblicz_silnie(n - 1); // Jeśli n jest większe od 1, funkcja wywołuje samą siebie tyle że z n - 1, proces się powtarza aż do chwli, gdy n = 1 i funkcja zwraca 1 - co powoduje wykonanie się wcześniejszych klonów funkcji i zwrócenie wyniku
    else
		return 1;  // Warunek podstawowy - silnia - !0 = 1
}

/* lub zamienione miejscami */ 

int oblicz_silnie(int n) // Deklaracja funkcji
{
    if (n < 1) // Warunek podstawowy - silnia - !0 = 1
        return 1;
    else
		return n * oblicz_silnie(n - 1); // W przeciwnym wypadku silnia = licznba * Wywołanie funkcji przez samą siebie i redukcja -1 wartość liczby - proces się powtarza, n = 0
}
```
![Alt|500](https://cdn.programiz.com/sites/tutorial2program/files/cpp-function-recursion-example.png)
```C++

PRZYKŁAD: Rozwiązanie iteracyjne:
int oblicz_silnie(int);

int main()
{
    int n, silnia;

    cout << "Wpisz liczbe nieujemna: ";
    cin >> n;

    silnia = oblicz_silnie(n); // Przypisanie wartości zwracanej przez funkcje
    cout << "Silnia z " << n << " = " << silnia;
    return 0;
}

int oblicz_silnie(int n) // Deklaracja funkcji
{
    int silnia = 1;
    for (int i = 1; i <= n; i++) // Iteracje
    {
        silnia *= i;
    }
    return silnia;
}
```
### Powrót przez odniesienie
>Powrót przez odniesienie
```C++
int num; // Globalna zmienna

int &test(); // Prototyp funkcji

int main()
{
    test() = 5; // Zwraca adres num więc można przypisać jej wartość

    cout << num;
    test();
    return 0;
}

int &test() // Deklaracja funkcji
{
    return num; // Zwraca adres zmiennej globalnej i przypisuje 5 zadeklarowane w funkcji main, tak więc num = 5
}
```

## Tablice i łańcuchy C++
### Tablice
>  **Tablica** - zmienna, która może rzechowywać wiele wartości tego samego typu
>- Ilość elementów tablicy musi mieć wartość stałą - brak możliwości zmiany po deklaracji tablicy - pozbycie się wady - patrz tablice dynamiczne
>- Uwaga na rozmiar tablicy
>   - Numeracja indeksów zaczyna sie od 0 - np.: `tab[5]`  -> |0|1|2|3|4|
>   - Nieprzekraczać wartości tablicy - inaczej błąd krytyczny
>   - Jeśli `tab[n]` to ostatni element jest przechowywany pod indeksem `(n-1)`
>- Elementy tablicy mają **kolejne adresy**. Na przykład załóżmy, że adres początkowy `x[0]`to `2120d`. Wówczas adres następnego elementu `x[1`]będzie miał wartość `2124d`, adres `x[2]` to `2128d` itd.
```C++
typ_danych nazwa_tabliczy[rozmiartablicy];
PRZTKŁAD:
int tab[6]; // Deklaracja tablicy

/* lub */

int x = 6;
int tab[x]; // Deklaracja tablicy ze zmienną np.: lokalną
```

>  **Inicjalizacja tablicy** - wypełnienie tablicy przy deklaracjii
```C++
int tab[6] = {1, 3, 5, 7, 9, 11}; // Inicjalizacja tablicy

/* lub */

int x[] = {1, 3, 5, 7, 9, 11}; // Przypisanie automatyczne wielkości tablicy, wynikającej z liczby przypisanych elementów

/* lub */

int tab[6] = {1, 3, 5}; // Inicjalizacja tablicy z pustymi członkami
```

> **Dostęp do elementów w tablicy** - każdy element tablicy jest powiązany z liczbą. Liczba jest nazywana **indeksem tablicy**. Możemy uzyskać dostęp do elementów tablicy za pomocą tych indeksów

```C++
// Indeksy = |0 |1 |2 |3 |4 |5 |
int tab[6] = {1, 3, 5, 7, 9, 11}; // Inicjalizacja

cout << tab[0]; // Wywołanie danej komórki tablicy
cout << tab[5];

Wynik:
1
11
```
> Pobieranie i wyprowadzanie danych
```C++
PRZYKŁAD_1 - zwykłe pętle:
    int tab[5];

    for (int i = 0; i < 5; i++) // Zwykła pętla pobierająca elementy tablicy
    {
        cout << "Podaj liczbe: ";
        cin >> tab[i];
    }

    for (int i = 0; i < 5; ++i) // Zwykła pętla wypisująca elementy tablicy
    {
        cout << tab[i] << " ";
    }
	
PRZYKŁAD_2 - pętle odwołujące się do adresu elemetu tabeli - oszczędza zasoby

    int tab[5];

    for (int i = 0; i < 5; i++) // Zwykła pętla pobierająca elementy tablicy
    {
        cout << "Podaj liczbe: ";
        cin >> tab[i];
    }

    for (int &n : tab) // Pętla pobierająca adres elementów i wypisująca wartości z możliwoścą ich zmiany
    {
        cout << n << " ";
        n += 1; // Zmiana zawartości elementów tablicy
    }

    cout << endl;

    for (const int &n : tab) // Pętla pobierająca adres elementów i wypisująca wartości bez możliwości ich zmiany - const
    {
        cout << n << " ";
        // n += 1; -> Error
    }
```

### Tablice wielowymiarowe
> Całkowita liczba elementów tabilcy wielowymiarowej obliczomu mnożąc jej wymiary np.:` 3 x 4 = 12`, `2 x 4 x 3 =24`
```C++
int tab[3][4]; // Deklaracja tablicy dwuwymiarowej
float tab[2][4][3]; // Deklaracja tablicy trzywymiarowej itd.
```
![Alt|450](https://cdn.programiz.com/sites/tutorial2program/files/cpp-two-dimensional-array.png)

> Inicjalizacja tablicy wielowymiarowej
```C++
    int tab[2][3] = {{1, 2, 3},
                     {4, 5, 6}};

	int tab[3][2] = {{1, 2},
					 {3, 4},
					 {5, 6}};

	int tab[2][3][4] = {{{3, 4, 2, 3}, {0, -3, 9, 11}, {23, 12, 23, 2}},
						{{13, 4, 56, 3}, {5, 9, 3, 5}, {5, 1, 4, 9}}};
```
>Pobieranie i wyprowadzanie danych
```C++
    int tab[2][3][2];

    for (int i = 0; i < 2; i++) // Pętla pobierająca
    {
        for (int j = 0; j < 3; j++)
        {
            for (int k = 0; k < 2; k++)
            {
                cin >> tab[i][j][k];
            }
        }
    }

    for (int i = 0; i < 2; i++) // Pętla wypisująca
    {
        for (int j = 0; j < 3; j++)
        {
            for (int k = 0; k < 2; k++)
            {
                cout << "tab[" << i << "][" << j << "][" << k << "] = " << tab[i][j][k] << endl;
            }
        }
    }
```

### Funkcje i tablice
```C++
typ_zmiennej nazwa_funkcji(typ_argumentu nazwa_tablicy[rozmiar tablicy]) {
	// code
}

PRZYKŁAD:
int funkcja(int tab[5]) {
    // code
}
```

```C++
PRZYKŁAD_1:
// Określenie liczby wierszy w tablicy nie jest obowiązkowe. Jednak zawsze należy określić liczbę kolumn - dlatego int n[][2]
void display(int n[][2]) // Definicja funkcji + przekazanie tablicy 2d
{
    cout << "Wyswietl wartosc: " << endl;
    for (int i = 0; i < 3; ++i)
    {
        for (int j = 0; j < 2; ++j)
        {
            cout << "num[" << i << "][" << j << "]: " << n[i][j] << endl;
        }
    }
}

int main()
{
    int num[3][2] = {
        {3, 4},
        {9, 5},
        {7, 1}};

    display(num);

    return 0;
}
```

```C++
PRZYKŁAD_2 - przekierowanie orginalnej tablicy do funkcji
- PS.: Patrz Dynamiczne alokowanie pamięci new i delete:

// Wywałanie tablic alokowanych
void nazwa_funkcji(typ_zmiennej *nazwa_tablicy, int wymiar_tablicy);
void nazwa_funkcji(typ_zmiennej **nazwa_tablicy, int wymiar_tablicy_1, int wymiar_tablicy_2);


void wyscwietl_tablice(int *tab, int num_1);
void wyscwietl_tablice(int **tab, int num_1, int num_2);

```

```C++
PRZYKŁAD_3 - zwracanie tablic alokowanych:

typ_tablicy* nazwa_funkcji(typ_1 arg_1, ... typ_n arg_n);
typ_tablicy** nazwa_funkcji(typ_1 arg_1, ... typ_n arg_n);

PRZYKŁAD_3:
int *rezerwauj_zasoby(int wybor);
int **rezerwauj_zasoby(int wybor);
```

```C++
PRZYKŁAD_4 - działania funkcujne na alokowanych tablicach:
int *zarezerwuj_tablice(int num_1); // 2D ** + num_2
void wprowadz_dane(int *tab, int num_1); // 2D ** + num_2
void wyswietlanie_tab(int *tab, int num_1); // 2D ** + num_2
void zwolnienie_zasobow(int *tab); // 2D ** + num_1

int main()
{
    int num_1;
    cout << "Podaj wielkosc tablicy: ";
    cin >> num_1;

    int *tab = zarezerwuj_tablice(num_1);
    wprowadz_dane(tab, num_1);
    wyswietlanie_tab(tab, num_1);

    zwolnienie_zasobow(tab);

    return 0;
}

int *zarezerwuj_tablice(int num_1)
{
    return new int[num_1];
}

void wprowadz_dane(int *tab, int num_1)
{
    for (int i = 0; i < num_1; i++)
    {
        cout << "Podaj element " << i << ": ";
        cin >> tab[i];
    }
}

void wyswietlanie_tab(int *tab, int num_1)
{
    for (int i = 0; i < num_1; i++)
    {
        cout << tab[i] << "\t";
    }
}

void zwolnienie_zasobow(int *tab)
{
    delete[] tab;
}

PS.: To samo w tablicach wielowymiarowych patrz Dynamiczne alokowanie pamięci new i delete
```

### Łańcuchy String i Char
> Łańcych -  zbiór znaków  
> `Stringi` - tablice typu `char` zakończone znakiem` null`, to znaczy `\0` (wartość znaku null w kodzie ASCII wynosi 0)

```C++
PRZYKŁADY:
char str [] = "C ++";
char str [4] = "C ++"; 
char str [] = {'C', '+', '+', '\ 0'}; 
char str [4] = {'C', '+', '+', '\ 0'};
char str [100] = "C ++";
string str;
string str = "C ++";

PRZYKŁAD_1 - łą:
    char str[100];

    cout << "Wprowadz lancych: ";
    cin >> str; // Łańcych kończy się po wprowadzeniu spacji
    cout << "Wprowadziles: " << str << endl;

    cout << "\nWprowadz lancych: ";
    cin >> str;
    cout << "Wprowadziles: " << str << endl;

PRZYKŁAD_2:
    char str[100];
    cout << "Wprowadz lancych: ";
    cin.set(str, 100); // Łańcych pobiera całą linie

    cout << "Wprowadziles: " << str << endl;

PRZYKŁAD_3:
    string str;

    cout << "Wprowadz lancych: ";
    cin >> str; // Łańcych kończy się po wprowadzeniu spacji
    cout << "Wprowadziles: " << str << endl;

    cout << "\nWprowadz lancych: ";
    cin >> str;
    cout << "Wprowadziles: " << str << endl;

PRZYKŁAD_4:
    string str;
    cout << "Wprowadz lancych: ";
    setline(cin, str); // Łańcych pobiera całą linie

    cout << "Wprowadziles: " << str << endl;
PS.: Przykład 1 i 3 - rozwiązanie problemu spacji w Zabezpieczenie przed wprowadzaniem błędnych danych
```
> Funkcje i łańcychy

```C++
void display(char *); // * nietrzeba tej gwiazdki
void display(string);

int main()
{
    string str1;
    char str[100];

    cout << "Wprowadz lancuch string: ";
    setline(cin, str1);

    cout << "Wprowadz lancuch char: ";
    cin.set(str, 100, '\n');

    display(str1);
    display(str);
    return 0;
}

void display(char s[])
{
    cout << "Wprowadzony lancuch char: " << s << endl;
}

void display(string s)
{
    cout << "Wprowadzony lancuch string: " << s << endl;
}
```

## Struktury C++
### Struktury
>**Struktura** - zbiór zmiennych o różnych typach danych pod jedną nazwą. Jest podobny do **klasy** w tym, że obie zawierają zbiór danych różnych typów danych


```C++
struct Osoba // Definiowanie struktury
{
    char imie[50];
    int wiek;
    float wyplata;
};

int main()
{
    Osoba p1; // Zdefiniowanie struktury - utworzenie pojemnika (osoby) p1 przechowującego zmienne

    cout << "Wprowadz imie i nazwisko: ";
    cin.set(p1.imie, 50); // Wprowadzanie poszczegulnych zmiennch - tablica
    cout << "Wprowadz wiek: ";
    cin >> p1.wiek; // Wprowadzanie poszczegulnych zmiennch - int
    cout << "Wprowadz wyplate: ";
    cin >> p1.wyplata;

    cout << "\nWyswietlenie informacji:" << endl;
    cout << "Imie: " << p1.imie << endl;
    cout << "Wiek: " << p1.wiek << endl;
    cout << "wyplata: " << p1.wyplata;

    return 0;
}
```
### Struktury i funkcjie
> Wartość wszystkich członków zmiennej strukturalnej można **przypisać** do innej struktury za pomocą operatora przypisania =, jeśli obie zmienne strukturalne są tego samego typu. Nie musisz ręcznie przypisywać każdego członka


```C++
struct nazwa_struktury
{
    typ_denych_1 nazwa_1;
    typ_denych_2 nazwa_2;
	...
    typ_denych_n nazwa_n;
};

PRZYKŁAD:
struct Osoba // Definiowanie struktury
{
    char imie[50];
    int wiek;
    float wyplata;
};

Osoba getData(Osoba);    // Prototyp funkcji pobierania
void displayData(Osoba); // Prototyp funkcji wyświetlania

int main()
{
    Osoba p1; // Zdefiniowanie struktury Osoba o nazwie p1

    p1 = getData(p1); // Przypisanie wartości strukturze p1 poprzez wywołanie funkcji zwracającej wypełnioną strukturę
    displayData(p1);  // Wywołanie funkcji ze zmienną strukturalną jako argumentem

    Osoba p2 = p1; // Przepisanie danych z jednej struktury do innej
    displayData(p2);
    return 0;
}

Osoba getData(Osoba p) // Deklaracja funckji zwracającej strykture = funkcja klonuje pustą strukturę p1 i zwraca już wypełnionego kolona p1
{
    cout << "Wprowadz imie i nazwisko: ";
    cin.get(p.imie, 50); // Wprowadzanie poszczegulnych zmiennch - tablica
    cout << "Wprowadz wiek: ";
    cin >> p.wiek; // Wprowadzanie poszczegulnych zmiennch - int
    cout << "Wprowadz wyplate: ";
    cin >> p.wyplata;

    return p;
}

void displayData(Osoba p) // Deklaracja funkcji ze zmienną strukturalną jako argumentem = przekazanie struktury
{
    cout << "\nWyswietlenie informacji:" << endl;
    cout << "Imie: " << p.imie << endl;
    cout << "Wiek: " << p.wiek << endl;
    cout << "Wyplata: " << p.wyplata;
}
```
###  Struktury zagnieżdżone
```C++
struct adres // Struktyra zagnieżdżana musi być pierwsza
{
    string miejscowosc;
    string nr_domu;
};

struct student
{
    string imie;
    int wiek;
    adres adres_zamieszkania; // Zagnieżdżenie wcześniej zadeklarowanej struktury
};

int main()
{
    student student_1; // Standardowe stworzenie objektu;

    student_1.imie = "Jan Kowalski";
    student_1.wiek = 20;
    // Wywołanie objrkt.nazwa_zagnieżdżonej_struktury.typ_struktury; itd. gdy jest więcej zagnieżdżeń
    student_1.adres_zamieszkania.miejscowosc = "Warszawa";
    student_1.adres_zamieszkania.nr_domu = "35A";

    cout << "Dane student_1: " << student_1.imie << " "
         << student_1.wiek << " lat, adres: "
         << student_1.adres_zamieszkania.miejscowosc << " "
         << student_1.adres_zamieszkania.nr_domu;
    // Reszta zalerzności funkcjie, tablice, alokowanie itp. tak samo jak zawsze
    return 0;
}
```



### Wskaźniki do struktury
> **Wskaźniki zmiennych** mogą być tworzone nie tylko przez rodzime typy podoba ( int, float, doubleitd.), ale  również mogą być tworzone dla określonych typów zdejiniowanych przez użytkowników, takich jak **struktury** - patrz Wskaźniki C++

```C++
PRZYKŁAD_1:
struct Dlugosc
{
    int i;
    float f;
};

int main()
{
    Dlugosc *wsk; // Tworzy wskaźnik wsk struktury typu Dlugosc
    return 0;
}
```

```C++
PRZYKŁAD_2:
struct Dystans
{
    int metr;
    float centymetr;
};

int main()
{
    Dystans dlugosc;
    Dystans *wsk = &dlugosc;

    cout << "Wprowadz metry: ";
    cin >> (*wsk).metr;
    cout << "Wprowadz centymetry: ";
    cin >> (*wsk).centymetr;

    cout << "Wyswietlenie informacji" << endl;
    cout << "Odleglosc = " << (*wsk).metr << "m i " << (*wsk).centymetr << "cm"; // . ma wyższy prioryten niż * dlatedo są ()

    return 0;
}
```

```C++
PRZYKŁAD_3 - wskaźnki + funckje - Dystans getData(Dystans *wsk) = zbędny kod:
struct Dystans
{
    int metr;
    float centymetr;
};

Dystans getData(Dystans *wsk); // Funckcja ze wskaźnikiem niejawnym z typem zwrotowym, po co zwracać wskaźnik do struktury ??? lub
void getData_2(Dystans *wsk);  // Funckcja ze wskaźnikiem niejawnym z funkcją niezwracającą
void displayData(Dystans wsk); // Funckcja z referencjią

int main()
{
    Dystans dlugosc;
    Dystans *wsk = &dlugosc;

    getData(&dlugosc);
    displayData(dlugosc);

    getData_2(&dlugosc);
    displayData(dlugosc);

    return 0;
}

Dystans getData(Dystans *wsk)
{
    cout << "Wprowadz metry: ";
    cin >> (*wsk).metr;
    cout << "Wprowadz centymetry: ";
    cin >> (*wsk).centymetr;
    return *wsk;
}
void getData_2(Dystans *wsk)
{
    cout << "Wprowadz metry: ";
    cin >> (*wsk).metr;
    cout << "Wprowadz centymetry: ";
    cin >> (*wsk).centymetr;
}

void displayData(Dystans wsk)
{
    cout << "Wyswietlenie informacji:" << endl;
    cout << "Odleglosc = " << wsk.metr << "m i " << wsk.centymetr << "cm" << endl; // . ma wyższy prioryten niż * dlatedo są ()
}
```

```C++
PRZTKŁAD_4 - struktury dynamiczne - alokacja Ale po co lol???
struct Dystans
{
    string nazwa;
    int metr;
    float centymetr;
};

Dystans *createDystans(); // Tworzenie alokowanej struktury za pomocą funkcji
void getDystans(Dystans *dystans_1); // Wczytywanie danych
void displayDystans(Dystans *dystans_1); // Wypisywanie danych

int main()
{
    Dystans *dystans_1 = new Dystans; // Tworzenie alokowanej struktury; Dystans [ilosc] - dla tablic
    /* lub */
    // Dystans *dystans_1 = createDystans();

    getDystans(dystans_1);
    displayDystans(dystans_1);
    delete dystans_1;
    return 0;
}

Dystans *createDystans()
{
    return new Dystans;
}

void getDystans(Dystans *dystans_1)
{
    dystans_1->nazwa = "Moj dystans"; // Wczytywanie danych do elementów struktury operator "->" - natychmiastowe zapisanie w strukturze
    cout << "Podaj ilosc metrow:\n";
    cin >> dystans_1->metr;
    cout << "Podaj ilosc centymetrow:\n";
    cin >> dystans_1->centymetr;
}

void displayDystans(Dystans *dystans_1)
{
    cout << "Wyswietlenie danych:\n";
    cout << "Nazwa: " << dystans_1->nazwa << endl;
    cout << "Dystans: " << dystans_1->metr << "m " << dystans_1->centymetr << "cm" << endl;
}
```

### Tablice struktur

```C++
struct student
{
    string imie;
    int wiek;
};

int main()
{
    student student[3]; // Standardowe stworzenie objektu;

    student[0].imie = "Jan Kowalski";
    student[0].wiek = 20;

    student[1].imie = "Gustaf Janoski";
    student[1].wiek = 21;

    student[2].imie = "Grarzyna Dumala";
    student[2].wiek = 22;

    for (int i = 0; i < 3; i++)
    {
        cout << "Student " << i << " : "
             << student[i].imie << " "
             << student[i].wiek << " lat" << endl;
    }

    return 0;
}
```
### Wyliczenie enum
> **Wyliczenie** - typ danych zdefiniowany przez użytkownika, który składa się ze stałych całkowitych,  aby zdefiniować wyliczenie, używane jest słowo kluczowe `enum` - patrz też Switch ... case i enum
> - W C ++ można osiągnąć prawie wszystko bez korzystania z wyliczeń, jednak w niektórych sytuacjach mogą być bardzo przydatne
```C++
enum pora_roku {wiosna, lato, jesień, zima}; // Definiowanie wyliczenia, wiosna, lato, jesien, zima = wartości typu pora_roku, moją one wartości domyślne: |wiosna = 0|lato = 1| jesien = 2|zima = 3|

enum pora_roku // Deklaracja wyliczenia ze zmianą wartości domyślnych
{
    wiosna = 0,
    lato = 4,
    jesien = 8,
    zima = 12
};

PRZYKAD_1:
enum week
{
    Sunday = 1,
    Monday = 2,
    Tuesday = 3,
    Wednesday = 4,
    Thursday = 5,
    Friday = 6,
    Saturday = 7
} check; // Flaga przypisania PRZYKŁAD_2

int main()
{
    week today;
    today = Wednesday;
    cout << "Dzis " << today + 1 << endl; // Możliwość operacji matematycznych

    int day;
    day = Saturday; // Możliwość przypisania
    cout << "Sobota jest " << day << " dniem tydodnia - chyba, ze masz inny kalendarz XD\n";
    check = Friday;

    cout << "Rozmiar zmiennej wyliczeniowej to " << sizeof(check) << " bajy"; // Wielkośc int :D
    return 0;
}

PRZYKŁAD_2 - wyliczneia do flag
enum designFlags // Zdefiniowanie możliwości wyglądu flagi - potęgi liczby 2, aby istniała możliwość sumowania efektów
{
    BOLD = 1,     // Pogrubienie 00000001
    ITALICS = 2,  // Kursywa 00000010
    UNDERLINE = 4 // Podkreślenie 00000100
};

int main()
{
    int myDesign = BOLD | UNDERLINE; // Operator sumy bitowej or = |

    //    00000001
    //  | 00000100
    //  ___________
    //    00000101

    cout << myDesign; // Wynik 5 -> kod(jeśli 5 to tekst bedzie pogrubiony i podkreślony)

    return 0;
}
```

## Wskaźniki C++
### Wskaźniki
> **Wskaźnik** - typ zmiennej odpowiedzialny za wskazanie adresu do innej zmiennej
> - Można nim wsakzywać na zmienną, tablicę, funkcję, strukturę i klasę
> - Operatory wskąźników:
>   - `*` -  **operator wyłuskanie wartości  zmiennej,  na którą wskazuje wskaźnik**
>   - `&` - **operator pobrania adresu zminnej**
> - Pozwalają:
>   - Przekazać do funkcji dowolną ilosć zmiennych
>   - Modyfukować orginelne zmienne / parametry w obrębie funkcji (funkcje działają na klonach przekazanych zmienneych)
>   - Dunamicznie alokować pamięć
> - Ważne:
>   - Można zmienić adres, na jaki wskazuje wskaźnik (nowy adres zmiennej)  
>   `int *wsk; *wsk = &adr_1; -> *wsk = &adr_2`
>   - Wksaźnik może przyjmować wartość NULL `int *wsk = NULL`
```C++
typ_zmiennej * nazwa_wskaźnika = &nazwa_wskazywanej_zmiennej(jej adres)

    int num = 1;
    int *wskaznik = &num; // Deklaracja wskaźnika i przypisanie do niego adresu zmiennej - niepreferowana składnia
    // int * wskaznik = &num; // * może być wszedzie
    // int* wskaznik = &num; // * może być wszedzie - ponoć preferowana składnia

    /* lub */

    // int* wskaznik; // Deklaracja wskażnika
    // wskaznik = &num; // Przypisanie adresu zmiennej

    // Uzyskanie adresu zmiennej
    cout << "Adres liczby: " << &num << endl;
    cout << "Adres liczby ze wskaznikiem: " << wskaznik << endl;

    // Uzyskanie wartości zmiennej
    cout << "Wartosc liczny: " << num << endl;
    cout << "Wartosc liczny ze wskaznika: " << *wskaznik << endl;

    // Zmiana wartosci poprzez wskażnik
    *wskaznik = 7;
    cout << "Wartosc liczny: " << num << endl;
    cout << "Wartosc liczny ze wskaznika: " << *wskaznik << endl;
	
Wynik:
Adres liczby: 0x61fe14
Adres liczby ze wskaznikiem: 0x61fe14
Wartosc liczny: 1
Wartosc liczny ze wskaznika: 1
Wartosc liczny: 7
Wartosc liczny ze wskaznika: 7
```

### Wskaźniki, referencje i funkcjie
```C++
PRZYKŁAD_1 - klonowanie zmiennych do funkcji:
void zerowanie(int num);

int main()
{
    int num = 1;

    // Funkcje działają na klonach wartości zmiennch (które można nazwać inaczej wewnątrz tej funkcji)
    cout << "Liczba: " << num << endl; // Wypisanie wartości liczby
    zerowanie(num); // Funkcja operuje na klonie / kopii wartości zmiennej
    cout << "Liczba: " << num << endl; // Wypisanie wartości liczby
    return 0;
}

void zerowanie(int licz) // Inna nazwa dla klonów num = licz
{
    licz = 0;
    cout << "Liczba funkcujna: " << licz << endl;
}

Wynik:
Liczba: 1
Liczba funkcyjna: 0
Liczba: 1
```

> **Referencja** - bezpośredni, niezmienny adres danej zmiennej, uproszczony wskaźnink, musi się odnosić do poprawnych adresów

> **Porównanie wskaźnika i referencji:**
> - **wsk:** typ zmiennej
> - **ref:** adres zmiennej <br> <br>
> - **wsk:** można do niego przypisać dowolny adres zmiennej w tym NULL
> - **ref:** można do niej przypisać tylko poprawny adres zmiennej, bez NULL <br> <br>
> - **wsk:**  można przypisać mu nowy adres
> - **ref:** nie można przypisać mu nowy adres <br> <br>
> - **wsk:** wyświetlenie wskaźnika pokarze adres zmiennej, z `*` jej zawartość
> - **ref:** wyświetla wartość zmiennej <br> <br>
> - **wsk:** przekazanie orginalnych danych do funkcji
> - **ref:** przekazanie orginalnych danych do funkcji
```C++
typ_zmiennej &nazwa_referencji = nazwa_zmiennej_wskazanego_typu
Wywołanie: funkcja(nazwa_referencji);

PRZYKŁAD_2 - przekazywanie funkcji orginału zmiennej poprzez adres zmiennej - referencja:

void zerowanie(int &num); // Lub (int &)

int main()
{
    int num = 1;
	/*lub*/
	// int &ref_num = num; // Deklaracja referencji

	cout << "Liczba: " << num << endl;
    zerowanie(num); // Funkcja operuje na orginalnej zmiennej - przekazanie nazwy zmiennej, lub zamiast num -> ref_num itd...
    cout << "Liczba: " << num << endl;
    return 0;
}

void zerowanie(int &num) // Adres orginalnej zmiennej
{
    num = 0;
    cout << "Liczba funkcyjna: " << num << endl;
}

Wynik:
Liczba: 1
Liczba funkcyjna: 0
Liczba: 0
```

```C++
PRZYKŁAD_3 - przekazywanie funkcji orginału zmiennej poprzez niejawny wskaźnik:

void zerowanie(int *wskaznik); // Lub (int *)

int main()
{
    int num = 1;
    cout << "Liczba: " << num << endl;
    zerowanie(&num); // Funkcja operuje na orginalnej zmiennej - przekazanie adresu
    cout << "Liczba: " << num << endl;

    /* lub dłużej, lepiej to pierwsze :D*/

    num = 1;
    int *wskaznik = &num; // Deklaracja wskażnika zwykłego
    cout << "Liczba: " << num << endl;
    zerowanie(wskaznik); // Funkcja operuje na orginalnej zmiennej - przekazanie adresu
    cout << "Liczba: " << num << endl;
    return 0;
}

void zerowanie(int *wskaznik) // Utworzenie niejawnego wskaźnika
{
    *wskaznik = 0;
    cout << "Liczba funkcyjna: " << *wskaznik << endl;
}

Wynik:
Liczba: 1
Liczba funkcyjna: 0
Liczba: 0
Liczba: 1
Liczba funkcyjna: 0
Liczba: 0
```
```C++
PRZYKŁAD_4 - referencja, wskaźnik i funkcja:
int sumowanie(int &ref, int *wsk); // Prototyp alt: int sumowanie(int &, int *)

int main()
{
    int num_1, num_2;
    cout << "Podaj dwie liczby:" << endl;
    cin >> num_1 >> num_2;
    // Przekazanie zmiennej num_1 od referencji i adresu num_2 do wskaźnika
    cout << "Suma tych liczb wynosi: " << sumowanie(num_1, &num_2);
    return 0;
}
// Deklaracja referencji i niejawnego wskaźnika - działanie na orginalnych zmiennych
int sumowanie(int &ref, int *wsk)
{
    return ref + *wsk;
}
```

### Wskaźiki i tablice
> Nazwa tablicy jest wskaźnikiem dla elementu tablicy o indeksie 0
```C++
    int tab[5] = {0, 1, 2, 3, 4};
    cout << "tab[0] = " << tab[0] << "\t"
         << "*tab -> tab[0] = " << *tab << endl; // Wskaźnik do tablicy

    cout << "tab[1] = " << tab[1] << "\t"
         << "*(tab + 1) -> tab[1] = " << *(tab + 1) << endl; // Wskaźnik do tablicy

    // Poruszanie się po tablicy za pomocą wskaźnika
    // Przypisanie wartości
    for (int i = 0; i < 5; i++)
    {
        cin >> *(tab + i); // *(tab[0] + 0) -> tab[0]; *(tab[0] + 1) -> tab[1]; itd.
        // cin >> tab[i];
    }

    // Za pomocą wskaźnika
    for (int i = 0; i < 5; i++)
    {
        cout << *(tab + i) << "\t"; // *(tab[0] + 0) -> tab[0]; *(tab[0] + 1) -> tab[1]; itd.
        // = cout << tab[i] << "\t";
    }

Wynik:
tab[0] = 0      *tab -> tab[0] = 0
tab[1] = 1      *(tab + 1) -> tab[1] = 1
1 2 3 4 5
1       2       3       4       5
```
### Dynamiczne alokowanie pamięci new i delete
> **Alokacja pamięci** - przydzielenie obiektowi pewnego obszaru pamięci oraz nadanie mu wartości początkowej
> - **statyczna** - alokacja pamięci następuje przed rozpoczęciem wykonywania programu
> - **dynamiczny** - alokacja następuje w fazie wykonywania programu - pozwala na na manipulowanie danymi o zmiennej wielkości, co znacząco zwiększa elastyczność programu, więc:  
> `new` - słóży do dynamicznego alokowania pamięci  
> `delete` - słóży do zwalniania zarezerwownej pamięci
> - Należy zawsze zwalniać pamięć inaczej może zdarzyć się sytuacja gdzie zabraknie zasobów do obliczeń
```C++
// Alokowanie zmiennej
	typ_danych *nazwa_wskaźnika = new typ_danych;
	// code
	delete nazwa_wskaźnika;

// Alokowanie tablicy
	typ_danych *nazwa_wskaźnika = new typ_danych[ilość_danych];
	// code
	delete[] nazwa_wskaźnika;
```

```C++
PRZYKŁAD_1 - alokownie zmiennej i tablicy:
    // Alokowanie zmiennej
    int *wsk = new int; // Alokowanie zmiennej
    *wsk = 1;
    cout << "wsk = " << *wsk << endl;
    delete wsk; // Zwalnianie pamięći

    // Alokowanie tablicy
    int num;
    cout << "Podaj wielkosc tablicy: ";
    cin >> num;

    int *tab = new int[num]; // Alokowanie tablicy

	// Tablicy można używać w normalny sposób - tu jest za pomocą wskoźnika
    for (int i = 0; i < num; i++)
    {
        cin >> *(tab + i);
    }

    for (int i = 0; i < num; i++)
    {
        cout << *(tab + i) << "\t";
    }

    delete[] tab; // Zwalnianie pamięći
	
Wynik:
wsk = 1
Podaj wielkosc tablicy: 3
1 3 5
1       3       5
```

> Alokownie tablicy wielowymiarowej - tu jest trudniej  
> Trzeba stworzyć wskoźnik na tablicę wskaźników na wymiary tablicy
> Trzeba stworzyć wskoźnik `**` na tablicę - podanie ilości wierszy:  
>```C++
>	int num_1, num_2;
>	
>	int **tab = new int *[num_1];
>```  
> Wypełnioną wskaźnikami do tablic alokowanych o podanej liczbie kolumn:
>```C++
>	for (int i = 0; i < num_1; i++)
>    {
>        tab[i] = new int[num_2];
>    }
>    // Np.: tab[0] = new int[10];
>    //      tab[1] = new int[10];
>    //      tab[2] = new int[10]; itd.
>```  
> Działania na takiej tablicy wykonuje się normalnie  
> Po zakończeniu obliczeń nalerzy zwolnić pamięć - **w odwrotnej kolejności niż deklarowanie:**
>```C++
>    for (int i = 0; i < num_1; i++)
>    {
>        delete[] tab[i];
>    }
>    delete[] tab;
>```

```C++
PRZYKŁAD_2 - alokownie tablicy wielowymiarowej
    int num_1, num_2; // Liczba wierszy, liczba kolumn
    cout << "Podaj wymiaty tablicy\n";
    cin >> num_1 >> num_2;

    // Alokowanie dynamicznej tablicy dwuwymiarowej
    int **tab = new int *[num_1];   // Alokowanie dynamicznej tablicy tablic / wskaźników
    for (int i = 0; i < num_1; i++) // Alokacja dynamicznych tablic
    {
        tab[i] = new int[num_2];
    }

    // Wypełnianie - normalnie
    for (int i = 0; i < num_1; i++)
    {
        for (int j = 0; j < num_2; j++)
        {
            tab[i][j] = i + j;
        }
    }

    // Wypisywnie - normalnie
    for (int i = 0; i < num_1; i++)
    {
        for (int j = 0; j < num_2; j++)
        {
            cout << tab[i][j] << "\t";
        }
        cout << endl;
    }

    // Zwalnianie pamięći
    for (int i = 0; i < num_1; i++)
    {
        delete[] tab[i];
    }
    delete[] tab;

Wynik:
Podaj wymiaty tablicy
3 4
0       1       2       3
1       2       3       4
2       3       4       5

Bonus:

    // Wpisywanie do tablicy wielowymiarowej
    for (int i = 0; i < num_1; i++)
    {
        for (int j = 0; j < num_2; j++)
        {
            cout << "Podaj [" << i << "][" << j << "]: ";
            cin >> tab[i][j];
        }
    }
```

```C++
PRZYKŁAD_3 - alokownie objektu:
class Student
{
    int age;

public:
    // Konstruktor inicjalizuje wiek na 12
    Student() : age(12) {}

    void getAge()
    {
        cout << "Wiek = " << age << endl;
    }
};

int main()
{

    // Dynamicznie inicjalizacja obiektu Student
    Student *wsk = new Student();

    // Wywołanie funkcji getAge ()
    wsk->getAge();

    // Pamięć ptr zostaje zwolniona
    delete wsk;

    return 0;
}

Wynik:
Wiek = 12
```

## Projekt - dzielenie kodu
> - Z czasem, z powiększeniem wiedzy i umiejętności **programy zaczynaja się rozrastać**  
> - Grupowanie elementów jakie znamy okazuje się niewystarczające, przez co **poruszanie się po kodzie staje się utrudnione**  
> - **Dlatego należy taki kod pogrópować, wydzielić i przenieść do oddzielnych tematycznych plików = czytelność i łatwość w utrzymaniu**  
> - Taki sposób pozwala na **używanie kodu w innych oddzielnych programach**, np. można **stworzyć zbiór własnych przydatnych narzędzi wywoływanych przez funkcje**  
> - W ten sposób tworzy się **projekty**
>>** Projekt - ** zbiór aktywności charakteryzujący się następującymi cechami:
>> -   są ze sobą powiązane w złożony sposób,
>> -   zmierzają do osiągnięcia celu, często poprzez wytworzenie unikatowego produktu, bądź rezultatu,
>> -   posiadają zaplanowany z góry początek i koniec
### Pliki główne, nagłówkowe i źródłowe
#### Plik Główny
> ** np.: `main.cpp` - program główny**
> - zawiera **główny program wywołujący funkcje** zawarte w pliku źródłowym `projekt.cpp`
> - może być tylko **jeden na projekt**
> - **wywołuje / jest połączony z ** `projekt.h` **lub** `projekt.hpp` - który przekazuje nazwy dostępnuch funkcji

#### Plik Nagłówkowy
>**`projekt.h` (C) / `projekt.hpp` (C++) -  header - program nagłówkowy, łączący - interfejs tego co dostarcza biblioteka**
> - **deklaruje: typy, funkcje, struktury, klasy, stałe, zmienne globalne**;
> - może **przypisywać wartości początkowe / startowe**
> - **wywoływany przez** `main.cpp` i `projekt.cpp`
> - w konstruktorze lub w metodzie można zawrzeć kod sprawdzający poprawność wprowadzanych zmienych - patrzy Klasy
>> Wstawianie / Przyłączanie pliku nagłówkowego `projekt.hpp` do pliku głównego `main.cpp` i źródłowego `projekt.cpp` :
>> 
>>``` C++
>> #include <nazwa_biblioteki> // < ... > = domyślne ścierzki do plików nagłówkowych bibliotek
>> 
>>#include "ścierzka_do_pliku" // " ... " = plik znajduje się względem bierzącego katalogu = mini biblioteka
>>// W zalerzności do umiejscowienia pliku np. w innym katalogu; w innym kompilatorze owy katalog trzeba utworzyć jako "source folder" by uiknąć błędów
>>
>> // Np.: Wstawić w main.cpp i projekt.cpp
>>#include "projekt.hpp"
>>
>>```

#### Plik Źródłowy
> **`projekt.cpp` - program źródłowy - zawiera kod odwalający czarną robote**
> - zawiera **funkcje wykorzystywane przez** `main.cpp` i **nazwane w** `projekt.hpp`
> - konkretne funkcje są **wywoływane przez program** `main.cpp`
>  - **wywołuje / jest połączony z ** `projekt.h` **lub** `projekt.hpp`
>   - mogą nim być: **inne pliki (np. *txt), bazy danych itd. ...**

```C++
PRZYKŁAD:

========================================
main.cpp - główny:

#include <iostream>
#include "projekt.hpp"
using namespace std;

int main()
{
    add(5, 3); // Wywoływanie funkcji
    return 0;
}

========================================
projekt.hpp - nagłówkowy:

// https://pl.wikipedia.org/wiki/Preprocesor
// Instrukcja procesora, sprawdza, czy zmienna procesorowa o podanej nazwie istnieje, jeśli nieistnieje to wszystkie instrukcje #if !defined(__) zostaną wykonane - działą jak if
#if !defined(_PROJEKT_HPP_)
// Tworzy zminną procesorową 
#define _PROJEKT_HPP_

void add(int, int); // Prototyp funkcji

// Koniec bloku warynkowego procesora
#endif // _PROJEKT_HPP_

========================================
projekt.cpp = źródłowy:

#include <iostream>
#include "projekt.hpp"
using namespace std;

void add(int a, int b) // Deklaracja funkcji
{
    cout << (a + b);
}

========================================
Wynik:
8
```

## Klasy i obiekty C ++
### Klasy i obiekty
> **OOP - Podejście Obiektowe - Object Oriented Programing** - kolejny sposób na to by kod był bardziej przejrzysty i łatwiejszy w utrzymaniu oraz rozwijaniu
>
> **Program komputerowy** - zbiór obiektów komunikujących się pomiędzy sobą w celu wykonywania zadań, każdy obiekt stworzony jest według przepisu podanego w klasie  


> **Klasa** - zbiór abstrakcyjnych sformułowań / cech / informacji definiujących i opisujących obiekt
> - w programowaniu obiektowym **własny typ danych**
> - na podstawie klasy - przepisu, mogą być wytwarzane konkretne egzemplarze obiektów
> 
> **Obiekt** - dający się wyodrębnić element rzeczywistości, mający swój zestaw cech zdefiniowanych w klasie - jego konspekcje / koncepcji / wyobrarzeniu
> 
> - w programowaniu obiektowym - przedstawiciel, czyli reprezentant klasy
>>```C++
>>Klasy = atrybuty (właściwości, cechy) + metoda (funkcja w klasie) 
>>Metoda - funkcja wewnątrz klasy
>>```
>
> Czyli elementy tworzące całość (zmienne, funkcje) zamykamy w klasie i decydujemy co z mimi zrobić, np.: ukryć je przed uźytkownikiem (hermetyzacja, enkapsulacja), lub zapisać i udostępnić w swego rodzaju ** interfejsie**

```C++
// Definjowanie klasy
class Nazwa_klasy
{
    // Code - definicje typów i funkcji
};

int main()
{
    // Stworzenie objektu
    Nazwa_klasy nazwa_klasy;
    return 0;
}

PRZYKŁAD_1 - błędny kod - zadziałało by w strukturach:
class Nazwa_klasy
{
// protected: // Domyślnie
    int num;
};

int main()
{
    // Stworzenie objektu
    Nazwa_klasy nazwa_klasy;
    nazwa_klasy.num = 0;
	cout << nazwa_klasy.num;
    return 0;
}

Wynik spowodowany hermetyzacją:
ERROR
```
#### Hermetyzacja - dostępność
> **Hermetyzancja** - hronienie przed światem, ukrywanie danych, dostępność
> Wewnątrz klasy różne pola mogą mieć rórzny typ dostępu:
> - `private:` - **dostęp prywatny, (domyślny)** - nie można wykożystać zmiennych i metod zdefiniowanych w klasie "na zewnątrz klasy"<br><br>
> - `protected:` - **dostęp chroniony** - d. prywatny + **klasy dzidziczące** mają dostęp do zmiennych chronionych <br><br>
> - `public:` - **dostęp publiczny (domyślny w strukturach)** - stłay dostęp do zmiennych i funkcji w całym kodzie

> **Metody** - funkcja wewnątrz klasy
> - moją dostęp do wszystkich pól klasy
> - Metoda prywatna - funkcja dostępna tylko w danej klasie, wykorzystywana jako fuckcja pomocnicza
> - Metoda pubLiczba - interfejs wykożystywany w funkcji głównej
> - Metoda chroniona - to samo co prywatna + dostępność w innych klasach

```C++
PRZYKŁĄD_1 - klasy, pola dostępnści, zmienne i metody:
#include <iostream>
using namespace std;

class Pokoj // Deklaracja klasy
{
private: // Zmienne i metody (funkcjie) mogą byś używane tylko w klasie
    float dlugosc;
    float szerokosc;
    float wysokosc;

    float oblicz_pole_prywatnie() // Metoda prywatna
    {
        return dlugosc * szerokosc;
    }

public: // Zmienne i metody (funkcjie) są dostępne wszędzie
    void setData(float dl, float szer, float wys) // Pobranie zmiennych i przypisanie objektowi
    {
        dlugosc = dl; // Przypisanie wortości zmiennym prywatnym
        szerokosc = szer;
        wysokosc = wys;
    }

    void printData() // Wyświetlanie obliczen
    {
        cout << "Pole pokoju = " << oblicz_pole() << endl;
        cout << "Objetosc pokoju = " << oblicz_objetosc() << endl;
    }

    float oblicz_pole() // Metoda pubLiczba
    {
        return oblicz_pole_prywatnie(); // Wykorzystanie metody prywatnej do obliczeń
    }

    float oblicz_objetosc() // Metoda pubLiczba
    {
        return dlugosc * szerokosc * wysokosc;
    }

protected:
    float oblicz_sume_bokow() // Funkcje chroniona - dziedziczenie później
    {
        return dlugosc * 4 + szerokosc * 4 + wysokosc * 4;
    }
};

int main()
{
    Pokoj pokoj_1, pokoj_2;      // Stworzenie objektów
	// Przypisanie zmiennych (tu długości) do objektów
    pokoj_1.setData(10, 10, 10);
    pokoj_2.setData(10, 20, 30);

    // Obliczanie wyniku poprzez wywołanie metod z klasy, poprzez stworzony objektobjekt
    cout << "Pole pokoju 1 = " << pokoj_1.oblicz_pole() << endl;
    cout << "Objetosc pokoju 1 = " << pokoj_1.oblicz_objetosc() << endl;

    cout << endl
         << "Rozmiary pokoju 2:" << endl;
    pokoj_2.printData(); // Wywołanie metody wyświtlajżcej wyniki metod obliczeniowych

    return 0;
}

Wynik:

Pole pokoju 1 = 100
Objetosc pokoju 1 = 1000

Rozmiary pokoju 2:
Pole pokoju = 200
Objetosc pokoju = 6000
```

#### :: - Operator zasięgu
> **Deklaracja ciała metody publicznej poprzez operator zasięgu ** `::`   
`typ_zwrotny_funckcji Nazwa_klasy::nzawa_metody(){Code}`
```C++
PRZYKŁAD_2 - operator zasięgu:
#include <iostream>
using namespace std;

class Pokoj // Deklaracja klasy
{
private: // Zmienne i funkcjie mogą byś używane tylko w klasie
    float dlugosc;
    float szerokosc;
    float wysokosc;

    float oblicz_pole_prywatnie(); // Metoda prywatna

public: // Zmienne i funkcjie (metody) są dostępne publicznie
    // Prototypy metod
    void setData(float dl, float szer, float wys); // Pobieranie danych - setter
    void getData();                                // Wyświetlanie danych i obliczen - getter
    float oblicz_pole();                           // ObLiczbaie pola
    float oblicz_objetosc();                       // ObLiczbaie objentoscu

protected:                     // Zmienne i funkcje chroniona - dziedziczenie później
    float oblicz_sume_bokow(); // Obliczanie sumy bokow
};

int main()
{
    Pokoj pokoj_1, pokoj_2;      // Stworzenie objektów
    pokoj_1.setData(10, 10, 10); // Przypisanie zmiennych tu długości do objektu
    pokoj_2.setData(10, 20, 30);

    // Obliczanie wyniku poprzez wywołanie metod z klasy, poprzez stworzony objektobjekt
    cout << "Pole pokoju 1 = " << pokoj_1.oblicz_pole() << endl;
    cout << "Objetosc pokoju 1 = " << pokoj_1.oblicz_objetosc() << endl;

    cout << endl
         << "Rozmiary pokoju 2:" << endl;
    pokoj_2.getData(); // Wywołanie metody wyświtlajżcej wyniki metod obliczeniowych

    return 0;
}

// Deklaracja ciała metody poprzez operator zasięgu ::
// typ_zwrotny_funckcji Nazwa_klasy::nzawa_metody(){Code}

void Pokoj::setData(float dl, float szer, float wys)
{
    dlugosc = dl;
    szerokosc = szer;
    wysokosc = wys;
}

void Pokoj::getData()
{
    cout << "Pole pokoju = " << oblicz_pole() << endl;
    cout << "Objetosc pokoju = " << oblicz_objetosc() << endl;
}

float Pokoj::oblicz_pole()
{
    return oblicz_pole_prywatnie();
}

float Pokoj::oblicz_pole_prywatnie() // Metoda prywatna
{
    return dlugosc * szerokosc;
}

float Pokoj::oblicz_objetosc()
{
    return dlugosc * szerokosc * wysokosc;
}

float Pokoj::oblicz_sume_bokow() // Metoda chroniona
{
    return dlugosc * 4 + szerokosc * 4 + wysokosc * 4;
}

Wynik:

Pole pokoju 1 = 100
Objetosc pokoju 1 = 1000

Rozmiary pokoju 2:
Pole pokoju = 200
Objetosc pokoju = 6000
```

#### Klasy + pliki projektowe
```C++
PRZYKŁAD_3 - klasy w projekcje

========================================
main.cpp - główny:

#include <iostream>
#include "projekt.hpp"
using namespace std;

int main()
{
    Pokoj pokoj_1, pokoj_2;      // Stworzenie objektów
    pokoj_1.setData(10, 10, 10); // Przypisanie zmiennych tu długości do objektu
    pokoj_2.setData(10, 20, 30);

    // Obliczanie wyniku poprzez wywołanie metod z klasy, poprzez stworzony objektobjekt
    cout << "Pole pokoju 1 = " << pokoj_1.oblicz_pole() << endl;
    cout << "Objetosc pokoju 1 = " << pokoj_1.oblicz_objetosc() << endl;

    cout << endl
         << "Rozmiary pokoju 2:" << endl;
    pokoj_2.getData(); // Wywołanie metody wyświtlajżcej wyniki metod obliczeniowych

    return 0;
}

========================================
projekt.hpp - nagłówkowy:

#if !defined(_PROJEKT_HPP_)
#define _PROJEKT_HPP_

class Pokoj // Deklaracja klasy
{
private: // Zmienne i funkcjie mogą byś używane tylko w klasie
    float dlugosc;
    float szerokosc;
    float wysokosc;

    float oblicz_pole_prywatnie(); // Metoda prywatna

public: // Zmienne i funkcjie (metody) są dostępne publicznie
    // Prototypy metod
    void setData(float dl, float szer, float wys); // Pobieranie danych - setter
    void getData();                                // Wyświetlanie danych i obliczen - getter
    float oblicz_pole();                           // ObLiczbaie pola
    float oblicz_objetosc();                       // ObLiczbaie objentoscu

protected:                     // Zmienne i funkcje chroniona - dziedziczenie później
    float oblicz_sume_bokow(); // Obliczanie sumy bokow
};

#endif // _PROJEKT_HPP_

========================================
projekt.cpp = źródłowy:

#include <iostream>
#include "projekt.hpp"
using namespace std;

// Deklaracja ciała metody poprzez operator zasięgu ::
// typ_zwrotny_funckcji Nazwa_klasy::nzawa_metody(){Code}

void Pokoj::setData(float dl, float szer, float wys)
{
    dlugosc = dl;
    szerokosc = szer;
    wysokosc = wys;
}

void Pokoj::getData()
{
    cout << "Pole pokoju = " << oblicz_pole() << endl;
    cout << "Objetosc pokoju = " << oblicz_objetosc() << endl;
}

float Pokoj::oblicz_pole()
{
    return oblicz_pole_prywatnie();
}

float Pokoj::oblicz_pole_prywatnie() // Metoda prywatna
{
    return dlugosc * szerokosc;
}

float Pokoj::oblicz_objetosc()
{
    return dlugosc * szerokosc * wysokosc;
}

float Pokoj::oblicz_sume_bokow() // Metoda chroniona
{
    return dlugosc * 4 + szerokosc * 4 + wysokosc * 4;
}

========================================
Wynik:
Pole pokoju 1 = 100
Objetosc pokoju 1 = 1000

Rozmiary pokoju 2:
Pole pokoju = 200
Objetosc pokoju = 6000
```
#### Uwagi
> - **Nazwa** klasy zaczyna sie **od dużej litery**
> - Całą klase możemy **oddzielić od głównego pliku**
>   - ** .hpp** - deklaracja klasy w pliku nagłówkowym
>   - **.cpp** - implementacje w pliku źródłowym
>   - **nazwa_klasy.hpp i nazwa_klasy.cpp**
> -** Jedna klasa = jeden zestaw plików (.hpp i .cpp)** niedotyczy klas pomocniczych
> - **Zmienne** kalsy powinny być **prywatne**
>   - Nadanie wartości poprzez **setter** - funkcji pobierająca
>     - **ang.** funkcja zaczyna się na** set... ; pl na ustaw...**
>   - Wyświetlanie wartości poprzez getter - funkcja wyświetlająca
>     - **ang.** funkcja zaczyna się na **get... ; pl na pobierz...**
> -** Interfej** klasy powinien być **prosty - prototypy metod**
> - **Nazwa klasy** niepowinna byś częścią **nazwy metody**
> - **Metody** powinny mieścić się **na jednym ekranie - łatwa analiza**
>   - Jeśli tak nie jest to rozbić ję na **minejsze metody prywatne**
> - **Metody publiczne tylko absolutne minimum** - zmiany w publicznej są **kłopotliwe**
> - Upieszczanie kolejno:** pola klasy, konstruktory, metody**

### Konstruktory
> **Konstruktor** - specjalna metoda danej klasy, wywoływana automatycznie podczas tworzenie nowego objektu (jeśli nie stworzymy konstruktora kompilator sam utworzy nowy, tyle że taki konstruktor niebędzie nic robił)
> - **zainicjowywuje on objekt (wypełnia go wartościami początkowymi)**, a w niektórych językach programowania także **tworzy obiekt**
> -  Informacje:
>    - nie ma typu zwracanej wrtości 
>    - nazwa taka sama jak nazwa kalsy
>    - może przyjmować argumenty
>    - można mieć kilka konstruktorów w jednej klasie

> **Konstruktor domyślny** - bez argumentów, nie przekazujemy wartości 
>```C++
>Prostokat();
>
>Prostokat::Prostokat()
>{
>    bok_1 = 0.0;
>    bok_2 = 0.0;
>}
>
>Prostokat prostokat_1;
>prostokat_1.wyswietl_boki();
>```

> **Konstruktor z argumentami** - przekazuje wartości  
>```C++
>Prostokat(float bok1, float bok2);
>
>Prostokat::Prostokat(float bok1, float bok2)
>{
>    bok_1 = bok1;
>    bok_2 = bok2;
>}
>
>Prostokat prostokat_1(1.1, 2.2);
>prostokat_1.wyswietl_boki();
>```

>** Konstruktor domyślny z argumentami** - połączenie poprzednich, przypisanie wartości startowych w pliku .hpp  
>```C++
>Prostokat(float bok1 = 1.1, float bok2 = 2.2);
>
>Prostokat::Prostokat(float bok1, float bok2)
>{
>    bok_1 = bok1;
>    bok_2 = bok2;
>}
>
>Prostokat prostokat_1;
>prostokat_1.wyswietl_boki();
>```

```C++
PRZYKŁAD_1: Konstruktor domyślny i z argumentami

========================================
main.cpp - główny:

#include <iostream>
#include "projekt.hpp"
using namespace std;

int main()
{
    Prostokat prostokat_1; // Wywołanie konstruktora domyślnego
    prostokat_1.wyswietl_boki();

    int bok1;
    cout << "Podaj pierwszy bok: "; cin >> bok1; // Podanie wartości początkowej
    Prostokat prostokat_2(bok1, 2.2); // Wywołanie konstruktora domyślnego z argumentami
    prostokat_2.wyswietl_boki();
    return 0;
}

========================================
projekt.hpp - nagłówkowy:

#if !defined(_PROJEKT_HPP_)
#define _PROJEKT_HPP_

class Prostokat
{
private:
    float bok_1, bok_2;

public:
    Prostokat();                       // Konstruktor domyślny
    Prostokat(float bok1, float bok2); // Konstruktor z argumentami

    void wyswietl_boki();
};

#endif // _PROJEKT_HPP_

========================================
projekt.cpp = źródłowy:

#include <iostream>
#include "projekt.hpp"
using namespace std;

Prostokat::Prostokat() // Konstruktor domyślny + przypisanie wartości
{
    bok_1 = 0.0;
    bok_2 = 0.0;
}

Prostokat::Prostokat(float bok1, float bok2) // Konstruktor z argumentami
{
    bok_1 = bok1;
    bok_2 = bok2;
}

void Prostokat::wyswietl_boki()
{
    cout << "Prostokat ma boki: " << bok_1 << ", " << bok_2 << endl;
};

========================================
Wynik:
Prostokat ma boki: 0, 0
Podaj pierwszy bok: 2
Prostokat ma boki: 2, 2.2
```

```C++
PRZYKŁAD_2: Konstruktor domyślny z argumentami
========================================
main.cpp - główny:

#include <iostream>
#include "projekt.hpp"
using namespace std;

int main()
{
    Prostokat prostokat_1; // Wywołanie konstruktora domyślnego z argumentami
    prostokat_1.wyswietl_boki();

    return 0;
}

========================================
projekt.hpp - nagłówkowy:

#if !defined(_PROJEKT_HPP_)
#define _PROJEKT_HPP_

class Prostokat
{
private:
    float bok_1, bok_2;

public:
    Prostokat(float bok1 = 1.1, float bok2 = 2.2); // Konstruktor z argumentami

    void wyswietl_boki();
};

#endif // _PROJEKT_HPP_

========================================
projekt.cpp = źródłowy:

#include <iostream>
#include "projekt.hpp"
using namespace std;

Prostokat::Prostokat(float bok1, float bok2) // Konstruktor z domyślny z argumentami
{
    bok_1 = bok1;
    bok_2 = bok2;
}

void Prostokat::wyswietl_boki()
{
    cout << "Prostokat ma boki: " << bok_1 << ", " << bok_2 << endl;
};

========================================
Wynik:
Prostokat ma boki: 1.1, 2.2
```

### Lista inicjalizacyjna
> - **Konstruktor nadaje wartości po utworzeniu objektu**
> - Inicjowanie w ten sposub zmiennych** typu const** oraz **refarencji** jest zawolne i **powoduje błędy**
> - **Inicjalizowanie wartości objektów ze zmiennymi typu const i referencji musi sie odbyć w trakcie ich tworzenia **
> - Do tego służą **listy inicjalizacyjne**

> **Lista iniscjalizacyjna:**
> - **szybsza** od konstruktorów
> - **czytelna**
> - umocliwia **inicjalizowanie zmiennych typu const**
> - umożliwia** inicjalizowanie zmiennej zdefiniowaniej jako referencja**
> - stosowana w **dziedziczeniu klas**
```C++
BŁĘDNY KOD:
========================================
main.cpp - główny:

    float pr = 5.0;
    Kolo kolo_1(pr);
    kolo_1.wyswietl_wartosci();

========================================
projekt.hpp - nagłówkowy:

class Kolo
{
private:
    float &promien;
    const float pi;

public:
    Kolo(float &pr);
    void wyswietl_wartosci();
};

========================================
projekt.cpp = źródłowy:

Kolo::Kolo(float &pr)
{
    promien = pr;
    pi = 3.14;
}

void Kolo::wyswietl_wartosci()
{
    cout << "PI = " << pi << ", promien = " << promien << endl;
}
```

```C++
PRZUKŁĄD - lista inicjalizacyjna:
========================================
main.cpp - główny:

#include <iostream>
#include "projekt.hpp"
using namespace std;

int main()
{
    float pr = 5.0;
    Kolo kolo_1(pr);
    kolo_1.wyswietl_wartosci();

    return 0;
}

========================================
projekt.hpp - nagłówkowy:

#if !defined(_PROJEKT_HPP_)
#define _PROJEKT_HPP_

class Kolo
{
private:
    float &promien;
    const float pi;

public:
    Kolo(float &pr);
    void wyswietl_wartosci();
};

#endif // _PROJEKT_HPP_

========================================
projekt.cpp = źródłowy:

#include <iostream>
#include "projekt.hpp"
using namespace std;

// Lista inicjalizacyjna
// Klasa::Konstruktor(typ referencja) : przypisanie_referncji(zmienna_pobierana), przypisanie_const(wartość), itd {}

Kolo::Kolo(float &pr) : promien(pr), pi(3.14) // Lista inicjalizacyjna
{
}

void Kolo::wyswietl_wartosci()
{
    cout << "PI = " << pi << ", promien = " << promien << endl;
}

========================================
Wynik:
PI = 3.14, promien = 5

```

### Destruktory
>** Destruktor** - metoda, która jast wywoływana zawsze tuż **przed usunięciem objektu klasy**  
> - Jest to  zaplanowanie zwolnienia pamieci po zadeklarowaniu pamięci metodą **new**
> Informacje:
> - nie ma typu zwrotnego
> - wygląd nazwa klasy  poprzedzona ~ (np.: ~nazwaKlasy)
> - jest bez parametrowy
> - klasa może mieć tylko jeden destruktor
> - destruktor uruchamaia się kiedy skończy się funkcja w której objekt istnieje np.: if ... else
```C++
PRZYKŁĄD_1:	
========================================
main.cpp - główny:

int main()
{

    float liczba_float = 3.14; // else -3.14
    if (liczba_float > 0)
    {
        Liczba liczba_1(liczba_float);
        liczba_1.wyswietl();
    } // Wywołanie destruktora dla objektu liczba_1 w if
    else
    {
        Liczba liczba_1;
        liczba_1.wyswietl();
    } // Wywołanie destruktora dla objektu liczba_1 w else

    Liczba liczba(2.25);
    liczba.wyswietl();

    return 0;
} // Wywołanie destruktora dla objektu liczba

========================================
projekt.hpp - nagłówkowy:

class Liczba
{
private:
    float liczba;

public:
    Liczba();               // Konstruktor domyślny
    Liczba(float liczba_1); // Konstruktor z argumentem
    ~Liczba();              // Destruktor
    void wyswietl();
};

========================================
projekt.cpp = źródłowy:

Liczba::Liczba() : liczba(0.0)
{
}

Liczba::Liczba(float liczba_1) : liczba(liczba_1)
{
}

Liczba::~Liczba() // Destruktor - TU NIC NIE ROBI
{
    cout << "No i destruktor pozamiatal!" << endl;
}

void Liczba::wyswietl()
{
    cout << "Liczba = " << liczba << endl;
}
```

```C++
PRZYKŁĄD_2:	
========================================
main.cpp - główny:

    Liczba *liczba = new Liczba(2.25);
    liczba->wyswietl();

    delete liczba; // Skasowanie objektu -> wywołanie destruktora

========================================
projekt.hpp - nagłówkowy:

class Liczba
{
private:
    float liczba;

public:
    Liczba();               // Konstruktor domyślny
    Liczba(float liczba_1); // Konstruktor z argumentem
    ~Liczba();              // Destruktor
    void wyswietl();
};

========================================
projekt.cpp = źródłowy:

Liczba::Liczba() : liczba(new float(0.0)) // Konstruktor dla wskaźnika
{
}

Liczba::Liczba(float liczba_1) : liczba(new float(liczba_1)) // Z argumentami
{
    // LUB - po utworzeniu objektu, zamiast listy inicjalizacyjnej
	// Lepiej to wyżej
    // liczba = new float(liczba_1);
}

Liczba::~Liczba()
{
    cout << "No i destruktor pozamiatal!" << endl;
    delete liczba; // Sens destruktora - zwalnianie pamięci
}

void Liczba::wyswietl()
{
    cout << "Liczba = " << *liczba << endl;
}
```

### Operator =
```C++
PRZYKŁĄD_1 - prosty operator przypisania:

    int num_1 = 2, num_2 = 0;
	
    cout << "Liczba 1 = " << num_1 << " , liczba 2 = " << num_2 << endl;
	
    num_2 = num_1; // Przypisanie
    cout << "Liczba 1 = " << num_1 << " , liczba 2 = " << num_2 << endl;
	
    num_1 = 5; // num_2 nie zmienia wartości
    cout << "Liczba 1 = " << num_1 << " , liczba 2 = " << num_2 << endl;
```
```C++
PRZYKŁĄD_2 - niewidoczny / automatyczny operator przypisania w klasach i objektach - tu działa:

#include <iostream>
using namespace std;

class Prostokat
{
private:
    int bok_1, bok_2;

public:
    Prostokat();
    Prostokat(int a, int b);
    ~Prostokat();
    void wyswietlBoki();
    void aktualizacjaBoki(int a, int b);
};

Prostokat::Prostokat() : bok_1(0), bok_2(0) // Lista inicjalizacyjna bez argumentów
{
}

Prostokat::Prostokat(int a, int b) : bok_1(a), bok_2(b) // Lista inicjalizacyjna z argumentami
{
}

Prostokat::~Prostokat() // Pusty destruktor
{
}

void Prostokat::wyswietlBoki()
{
    cout << "Bok a = " << bok_1 << " , bok b = " << bok_2 << endl;
}

void Prostokat::aktualizacjaBoki(int a, int b)
{
    bok_1 = a;
    bok_2 = b;
}

int main()
{
    Prostokat prostokat_1(2, 4), prostokat_2; // Wywołano 2 konstruktory

    cout << "Prostokat 1: ";
    prostokat_1.wyswietlBoki();
    cout << "Prostokat 2: ";
    prostokat_2.wyswietlBoki();

    prostokat_2 = prostokat_1; // Stworzenie niewidzialnego operatora przypisania
    // np.  prostokat_2.bok_1 = prostokat_1.bok_1
    //      prostokat_2.bok_2 = prostokat_1.bok_2 itd.

    cout << "Prostokat 1: ";
    prostokat_1.wyswietlBoki();
    cout << "Prostokat 2: ";
    prostokat_2.wyswietlBoki();

    prostokat_1.aktualizacjaBoki(3, 3);

    cout << "Prostokat 1: ";
    prostokat_1.wyswietlBoki();
    cout << "Prostokat 2: ";
    prostokat_2.wyswietlBoki();

    return 0;
}
```
```C++
PRZYKŁĄD_3 - operator przypisania w wskaźnikach:

    int *num_1 = new int(2);
    int *num_2 = new int(0);

    cout << "Liczba 1 = " << *num_1 << " , liczba 2 = " << *num_2 << endl;

    *num_2 = *num_1; // Przypisanie wskaźników
    // num_2 = num_1; // Stworzenie dwóch wskaźników na jeden adres
    // Wtedy wynik: Liczba 1 = 5 , liczba 2 = 5
    cout << "Liczba 1 = " << *num_1 << " , liczba 2 = " << *num_2 << endl;

    *num_1 = 5; // num_2 nie zmienia wartości
    cout << "Liczba 1 = " << *num_1 << " , liczba 2 = " << *num_2 << endl;

    delete num_1;
    delete num_2;
```


```C++
PRZYKŁĄD_4 - operator przypisania w wskaźnikach klasy BŁĄD = przypisanie adresu wskaźnika zapiast wartości na którą wskazuje:

#include <iostream>
using namespace std;

class Prostokat
{
private:
    int *bok_1, *bok_2;

public:
    Prostokat();
    Prostokat(int a, int b);
    ~Prostokat();
    void wyswietlBoki();
    void aktualizacjaBoki(int a, int b);
};

Prostokat::Prostokat() : bok_1(new int(0)), bok_2(new int(0)) // Lista inicjalizacyjna bez argumentów ze wskaźnikami
{
}

Prostokat::Prostokat(int a, int b) : bok_1(new int(a)), bok_2(new int(b)) // Lista inicjalizacyjna z argumentami ze wskaźnikami
{
}

Prostokat::~Prostokat()
{
    delete bok_1;
    delete bok_2;
}

void Prostokat::wyswietlBoki()
{
    cout << "Bok a = " << *bok_1 << " , bok b = " << *bok_2 << endl;
}

void Prostokat::aktualizacjaBoki(int a, int b)
{
    *bok_1 = a;
    *bok_2 = b;
}

int main()
{
    Prostokat prostokat_1(2, 4), prostokat_2; // Wywołano 2 konstruktory

    cout << "Prostokat 1: ";
    prostokat_1.wyswietlBoki();
    cout << "Prostokat 2: ";
    prostokat_2.wyswietlBoki();

    prostokat_2 = prostokat_1; // Stworzenie niewidzialnego operatora przypisania przez kompilator - przepisanie adresu wskaćnika zamiast wartości na którą wskazuje = potęcjalny błąd
    // np.  prostokat_2.bok_1 = prostokat_1.bok_1
    //      prostokat_2.bok_2 = prostokat_1.bok_2 itd.

    cout << "Prostokat 1: ";
    prostokat_1.wyswietlBoki();
    cout << "Prostokat 2: ";
    prostokat_2.wyswietlBoki();

    prostokat_1.aktualizacjaBoki(3, 3);

    cout << "Prostokat 1: ";
    prostokat_1.wyswietlBoki();
    cout << "Prostokat 2: ";
    prostokat_2.wyswietlBoki();

    return 0;
}

Wynik:
Prostokat 1: Bok a = 2 , bok b = 4
Prostokat 2: Bok a = 0 , bok b = 0
Prostokat 1: Bok a = 2 , bok b = 4
Prostokat 2: Bok a = 2 , bok b = 4
Prostokat 1: Bok a = 3 , bok b = 3
Prostokat 2: Bok a = 3 , bok b = 3
```
### This
> `this` - **odwołanie do bieżącego objektu klasy**, na rzecz którego została wywołana dana metoda, **wskaźnik na bieżący objekt klasy**
```C++
Zastosowanie this w funkcji przypisania:
public:
    Prostokat &operator=(const Prostokat &prostokatPrawy);
	// UWAGA! - jeśli umieścimy ten prototyw w sekcji private: - przypisywanie prostokat_2 = prostokat_1; będzie niemożliwe - uniemożliwienie błędnego przypisywania adresów patrz PRZYKŁAD_4:
	
	Prostokat &Prostokat::operator=(const Prostokat &prostokatPrawy)
{
    // cout << "Jestem operatorem = !" << endl;
    if (this == &prostokatPrawy)
        return *this;

    *this->bok_1 = *prostokatPrawy.bok_1;
    *this->bok_2 = *prostokatPrawy.bok_2;

    return *this;
}	
	prostokat_2 = prostokat_1; -> Przypisanie wartości, bez powyższej metody przypisanie adresu
```
	
```C++
Zastosowanie this w zbierzności nazw argumentu i zmiennej metody
	
	int *bok_1, *bok_2; // #1
	...
	void aktualizacjaBoki(int bok_1, int bok_2); // #2
	
	void Prostokat::aktualizacjaBoki(int bok_1, int bok_2)
{
	// *bok_1 = bok_1 // WTF zbieźnosc nazw
    *this->bok_1 = bok_1; // #1 == #2
    *this->bok_2 = bok_2;
}

```

```C++
PRZYKŁĄD_5 - operator przypisania w wskaźnikach klasy - przypisanie wartości na jakie wskazuje wskaźnik - stworzenie funkcji przypisania ze złowem this lub nazwą zmiennej metody kalsy:

#include <iostream>
using namespace std;

class Prostokat
{
private:
    int *bok_1, *bok_2;

public:
    Prostokat();
    Prostokat(int a, int b);
    ~Prostokat();
    // Referencja_do_klasy& operator=(stały_objekt_klasy_Prostokat &prawa_str_znaku_=);
    Prostokat &operator=(const Prostokat &prostokatPrawy);
    void wyswietlBoki();
    void aktualizacjaBoki(int bok_1, int bok_2);
};

Prostokat::Prostokat() : bok_1(new int(0)), bok_2(new int(0)) // Lista inicjalizacyjna bez argumentów ze wskaźnikami
{
}

Prostokat::Prostokat(int a, int b) : bok_1(new int(a)), bok_2(new int(b)) // Lista inicjalizacyjna z argumentami ze wskaźnikami
{
}

Prostokat::~Prostokat()
{
    delete bok_1;
    delete bok_2;
}

Prostokat &Prostokat::operator=(const Prostokat &prostokatPrawy)
{
    cout << "Jestem operatorem = !" << endl;
    // Sprawdzanie, czy podane wartości są równe jeśli tak to nic się nie robi
    if (this == &prostokatPrawy)
        return *this;

    // Jeśli nie to:
    // wartość_pola_bok_1/2 =  wartość_pola_bok_1/2_objektu_po_prawej_stronie
    *this->bok_1 = *prostokatPrawy.bok_1;
    *this->bok_2 = *prostokatPrawy.bok_2;
    // *this->bok_1/2 to samo co: *bok1/2 - przydatne, gdy przekazujemy argumenty o tej samej nazwie

    return *this;
}

/*
    this - odwołanie do bieżącego objektu klasy, na rzecz którego została wywołana dana metoda, wskaźnik na bieżący objekt klasy
*/

void Prostokat::wyswietlBoki()
{
    cout << "Bok a = " << *bok_1 << " , bok b = " << *bok_2 << endl;
}

void Prostokat::aktualizacjaBoki(int bok_1, int bok_2)
{
    *this->bok_1 = bok_1; // Zbieźnosc nazw - przydatny this
    *this->bok_2 = bok_2;
}

int main()
{
    Prostokat prostokat_1(2, 4), prostokat_2; // Wywołano 2 konstruktory

    cout << "Prostokat 1: ";
    prostokat_1.wyswietlBoki();
    cout << "Prostokat 2: ";
    prostokat_2.wyswietlBoki();

    prostokat_2 = prostokat_1; // Stworzenie niewidzialnego operatora przypisania przez kompilator - przepisanie adresu wskaćnika zamiast wartości na którą wskazuje = potęcjalny błąd
    // np.  prostokat_2.bok_1 = prostokat_1.bok_1
    //      prostokat_2.bok_2 = prostokat_1.bok_2 itd.

    cout << "Prostokat 1: ";
    prostokat_1.wyswietlBoki();
    cout << "Prostokat 2: ";
    prostokat_2.wyswietlBoki();

    prostokat_1.aktualizacjaBoki(3, 3);

    cout << "Prostokat 1: ";
    prostokat_1.wyswietlBoki();
    cout << "Prostokat 2: ";
    prostokat_2.wyswietlBoki();

    return 0;
}

// C++11 ma lepsze rozwiązanie

Wynik:

Prostokat 1: Bok a = 2 , bok b = 4
Prostokat 2: Bok a = 0 , bok b = 0
Jestem operatorem = !
Prostokat 1: Bok a = 2 , bok b = 4
Prostokat 2: Bok a = 2 , bok b = 4
Prostokat 1: Bok a = 3 , bok b = 3
Prostokat 2: Bok a = 2 , bok b = 4
```

```C++
PRZYKŁAD_6 - operator przypisania w alokowanej tablicy dwywymiarowej zadeklarowanej w klasie

#include <iostream>
using namespace std;

class Macierz
{
private:
    const int wymiar_1, wymiar_2; // Stałe wymiary macierzy
    float **macierz;              // Wskaźnik/i do macierzy

public:
    Macierz(int aWymiar1, int aWymiar2);             // Kreator, wielkość i wypełnienie
    ~Macierz();                                      // Destruktor macierzy
    Macierz &operator=(const Macierz &macierzPrawa); // Poprawny operator przypisania
    void wyswietl();                                 // Wyświetlenie macierzy
    void aktualizuj();                               // Aktualizacja macierzy
};

Macierz::Macierz(int aWymiar1, int aWymiar2) : wymiar_1(aWymiar1),
                                               wymiar_2(aWymiar2) // Wielkość macierzy
{
    // Stworzenie alokowaniej macirzy
    macierz = new float *[wymiar_1]; // Ilość wierszy
    for (int i = 0; i < wymiar_1; i++)
    {
        macierz[i] = new float[wymiar_2]; // Ilość kolumn
    }

    // Wypełnienie macierzy
    cout << "Podaj nowe dane macierzy: \n";
    for (int i = 0; i < wymiar_1; i++)
    {
        for (int j = 0; j < wymiar_2; j++)
        {
            cout << "Podaj element: " << i << ", " << j << ": ";
            cin >> macierz[i][j];
        }
    }
}

Macierz::~Macierz() // Usunięcie alokowanej macierzy
{
    for (int i = 0; i < wymiar_1; i++)
    {
        delete[] macierz[i]; // Zwalnianie kolumn
    }
    delete[] macierz; // Zwalnianie macierzy (wierszy)
}

Macierz &Macierz::operator=(const Macierz &macierzPrawa)
{
    if (this == &macierzPrawa) // Sprawdzanie równości objektów
        return *this;          // Można uleprzyć o znajdowanie równości wielkości macierzy
    // Tj. niewykonywuj jeśli liczba wierszy i kolumn jest różna

    for (int i = 0; i < wymiar_1; i++)
    {
        for (int j = 0; j < wymiar_2; j++)
        {
            // Przypisanie wartości z prawej od obecnego objektu macierzy
            this->macierz[i][j] = macierzPrawa.macierz[i][j];
        }
    }
    return *this; // Zwracanie bierząceej macierzy po przypisaniu nowych wartości
}

void Macierz::wyswietl()
{
    for (int i = 0; i < wymiar_1; i++)
    {
        for (int j = 0; j < wymiar_2; j++)
        {
            cout << macierz[i][j] << "\t";
        }
        cout << "\n";
    }
}

void Macierz::aktualizuj()
{
    cout << "Podaj nowe dane do macierzy: \n";
    for (int i = 0; i < wymiar_1; i++)
    {
        for (int j = 0; j < wymiar_2; j++)
        {
            cout << "Podaj element: " << i << ", " << j << ": ";
            cin >> macierz[i][j];
        }
    }
}

int main()
{
    cout << "\nmacierz_1: \n";
    Macierz macierz_1(2, 3);
    macierz_1.wyswietl();

    cout << "\nmacierz_2: \n";
    Macierz macierz_2(2, 3);
    macierz_2.wyswietl();

    cout << "\nmacierz_1 = macierz_1: \n";
    macierz_1 = macierz_1; // Operator przypisania

    cout << "\nmacierz_1 - zmiana danych: \n";
    macierz_1.aktualizuj();
    macierz_1.wyswietl();

    cout << "\nmacierz_2 - sprawdzenie czy cos sie zmienilo \n";
    macierz_2.wyswietl();

    return 0;
}
```

### Konstruktor kopiujący
> - **Podczas tworzenia klasy kompilator tworzy dla nas pewne funkcje których niezadeklarowaliśmy** 
> - Są to między innymi **poerator =**, jaki i **konstruktor kopiujący**
> - Są to przydatne konstrukcjie, **przydatne** w wielu sytuacjach  
> - Jednakże są **bardzo proste** (przypisywanie adresu zmiennej, zamiast jej zawartości), co zatym idzie, **mogą powadować odmienne rezultatu od zamierzonych**  
> - **Operator kopiujęcy** - wywoływany  gdy tworzymy objekt klasy w oparciu o inny objekt klasy

```C++
PRZYKŁAD_1 - prosty konstruktor kopiujący:

#include <iostream>
using namespace std;

class Prostokat
{
private:
    float bok1, bok2;

public:
    Prostokat();
    Prostokat(int aBok1, int aBok2);
    ~Prostokat();
    void wyswietlBoki();
    void aktualizujBoki(int aBok1, int aBok2);
};

Prostokat::Prostokat() : bok1(0), bok2(0) {}

Prostokat::Prostokat(int aBok1, int aBok2) : bok1(aBok1), bok2(aBok2) {}

Prostokat::~Prostokat()
{ /*Pustka*/
}

void Prostokat::wyswietlBoki()
{
    cout << "Bok1 = " << bok1 << ", Bok2 = " << bok2 << endl;
}

void Prostokat::aktualizujBoki(int aBok1, int aBok2)
{
    bok1 = aBok1;
    bok2 = aBok2;
}

int main()
{

    Prostokat prostokat_1(2, 4);

    cout << "Prostakat_1 = ";
    prostokat_1.wyswietlBoki();

    cout << "Tworzenie prostokat_2 uzywajac konstruktora kopiujacego!!!" << endl;
    Prostokat prostokat_2(prostokat_1); // Konstruktor kopiujący
    cout << "Prostakat_2 = ";
    prostokat_2.wyswietlBoki();

    cout << "Aktualizacja bokow Prostakat_1!!!" << endl;
    prostokat_1.aktualizujBoki(3, 3);

    cout << "Prostakat_1 = ";
    prostokat_1.wyswietlBoki();
    cout << "Prostakat_2 = ";
    prostokat_2.wyswietlBoki();
    return 0;
}

Wynik:
Prostakat_1 = Bok1 = 2, Bok2 = 4
Tworzenie prostokat_2 uzywajac konstruktora kopiujacego!!!
Prostakat_2 = Bok1 = 2, Bok2 = 4
Aktualizacja bokow Prostakat_1!!!
Prostakat_1 = Bok1 = 3, Bok2 = 3
Prostakat_2 = Bok1 = 2, Bok2 = 4
```

```C++
PRZYKŁAD_2 - konstruktor kopiujący pracując ze wskaźnikami :

#include <iostream>
using namespace std;

class Prostokat
{
private:
    float *bok1, *bok2;

public:
    Prostokat();
    Prostokat(int aBok1, int aBok2);
    Prostokat(Prostokat &pr); // Konstruktor kopiujący dla wskaźników
    // Gdy Prostokat(Prostokat &pr); będzie w sekcji private: zablokujemy dostęp do konstruktor kopiującego
    ~Prostokat();
    void wyswietlBoki();
    void aktualizujBoki(int aBok1, int aBok2);
};

Prostokat::Prostokat() : bok1(new float(0)), bok2(new float(0)) {}

Prostokat::Prostokat(int aBok1, int aBok2) : bok1(new float(aBok1)),
                                             bok2(new float(aBok2)) {}

Prostokat::Prostokat(Prostokat &pr) // &pr = objekt prostokat1 jego zmienne bok1/2
{
    cout << "Jestem konstruktorem kopiujacym!\n";
    // Rezerwacja pemięci + Przypisanie wartości do mowego objektu poprzez referencje i wskaźnik
    bok1 = new float(*pr.bok1); // Skopiowanie wartości, a nie adresu
    bok2 = new float(*pr.bok2);
}

Prostokat::~Prostokat()
{
    delete bok1;
    delete bok2;
}

void Prostokat::wyswietlBoki()
{
    cout << "Bok1 = " << *bok1 << ", Bok2 = " << *bok2 << endl;
}

void Prostokat::aktualizujBoki(int aBok1, int aBok2)
{
    *bok1 = aBok1;
    *bok2 = aBok2;
}

int main()
{

    Prostokat prostokat_1(2, 4);

    cout << "Prostakat_1 = ";
    prostokat_1.wyswietlBoki();

    cout << "Tworzenie prostokat_2 uzywajac konstruktora kopiujacego!!!" << endl;
    Prostokat prostokat_2(prostokat_1); // Konstruktor kopiujący
    cout << "Prostakat_2 = ";
    prostokat_2.wyswietlBoki();

    cout << "Aktualizacja bokow Prostakat_1!!!" << endl;
    prostokat_1.aktualizujBoki(3, 3);

    cout << "Prostakat_1 = ";
    prostokat_1.wyswietlBoki();
    cout << "Prostakat_2 = ";
    prostokat_2.wyswietlBoki();
    return 0;
}

Wynik:
Prostakat_1 = Bok1 = 2, Bok2 = 4
Tworzenie prostokat_2 uzywajac konstruktora kopiujacego!!!
Jestem konstruktorem kopiujacym!
Prostakat_2 = Bok1 = 2, Bok2 = 4
Aktualizacja bokow Prostakat_1!!!
Prostakat_1 = Bok1 = 3, Bok2 = 3
Prostakat_2 = Bok1 = 2, Bok2 = 4
```


```C++
PRZYKŁAD_3 - wykorzystanie w tablicach:

#include <iostream>
using namespace std;

class Tablica
{
private:
    const int wymiar;
    float *tablica;

public:
    Tablica(int aWymiar);
    Tablica(Tablica &tab); // Konstruktor kopiujący
    ~Tablica();
    void wyswietlDane();
    void aktualizujDane();
    float obliczSredia();
};

Tablica::Tablica(int aWymiar) : wymiar(aWymiar)
{
    tablica = new float[wymiar];
    for (int i = 0; i < wymiar; i++)
    {
        cout << "Podaj element tablicy nr " << i << ": ";
        cin >> tablica[i];
    }
}

Tablica::Tablica(Tablica &tab) : wymiar(tab.wymiar) // Referaencja na kopiowaną tablice + przekazanie wymiaru tablicy
{
    tablica = new float[wymiar]; // Inicjalizacja nowej tablicy
    for (int i = 0; i < wymiar; i++)
    {
        tablica[i] = tab.tablica[i]; // Przupisanie wartości
    }
}
Tablica::~Tablica()
{
    delete tablica;
}

void Tablica::wyswietlDane()
{
    for (int i = 0; i < wymiar; i++)
    {
        cout << tablica[i] << "\t";
    }
    cout << endl;
}

void Tablica::aktualizujDane()
{
    for (int i = 0; i < wymiar; i++)
    {
        cout << "Podaj nowy element tablicy nr " << i << ": ";
        cin >> tablica[i];
    }
}

float Tablica::obliczSredia()
{
    float suma = 0;
    for (int i = 0; i < wymiar; i++)
    {
        suma += tablica[i];
    }
    return suma / wymiar;
}

int main()
{
    int x;
    cout << "Podaj wymiar tablicy: ";
    cin >> x;
    Tablica tablica_1(x);
    cout << "tablica_1:\t";
    tablica_1.wyswietlDane();

    cout << "Kopiowanie do tabilca_2!!!\n";
    Tablica tablica_2(tablica_1);
    cout << "tablica_2:\t";
    tablica_2.wyswietlDane();

    cout << "Aktualizacja tablica_1!!!\n";
    tablica_1.aktualizujDane();
    cout << "tablica_1:\t";
    tablica_1.wyswietlDane();
    cout << "tablica_2:\t";
    tablica_2.wyswietlDane();

    cout << "Srednia tablica_1: " << tablica_1.obliczSredia() << endl;
    cout << "Srednia tablica_2: " << tablica_2.obliczSredia() << endl;
    return 0;
}
```
### Przeciążanie operatorów i operatory
https://www.programiz.com/cpp-programming/operator-overloading
```C++

```


## Dziedziczenie C ++
### Dziedziczenie
> **Dziedziczenie** (ang. inheritance) - mechanizm współdzielenia funkcjonalności (zmienne i metody) między klasami.  
> Klasa może dziedziczyć po innej klasie, co oznacza, że oprócz swoich własnych atrybutów oraz zachowań, uzyskuje także te pochodzące z klasy, z której dziedziczy, co zapobiega redundancji (powtarzania) tych samych linii kodu
> 
> **Słowniczek:**
> - **klasa pochodna** - potomek
> - **klasa podstawowa** - od której się dziedziczy
> - **dziedzicznie wielopokoleniowe** - klasa pochodna może stać się klasą podstawową
> - **dziedzicznie jednokrotne** - na podstawie 1 klasy podstawowej
> - dziedziczenie wielokrotne - na podstawie więcej niż jednej klasy podstawowej (drzewo dziedziczenia)
> - nowe klasy powstają już z istniejących klas zgromadzonych w bibliotekach - umożliwia to budowanie programów z komponentów wielokrotnego użytku
> - **dziedziczymy wszystkie pola klasy podstawowej i jej metody**
> - **nie dziedziczymy: konstruktorów, destruktorów, operatorów przypisania**

> **Osoba** - klasa podstawowa:
> - publiczne metody:  
>   - konstruktor  
>   - `wyswietlDane`  - wyświetli poniższe zmienne, a klasy pochodne odziedziczą tą funkcjie<br> <br>
> - prywatne składowe:
>   - `string imię`
>   - `string nazwisko`
>   - `string telefon`
>
>> **Student** - klasa pochodna:
>> - publiczne metody:  
>>    - konstruktor  
>>    - `wyswietlDane` - odziedziczona funkcjia, możliwość dodania orginalnych zmienneych wywoływancy tą samą metodą<br> <br>
>> - prywatne składowe:
>>   - long numerIndeksu
>>   - float sredniaOcen
>
>> **Wykładowca** - klasa pochodna:
>> - publiczne metody:  
>>    - konstruktor  
>>    - `wyswietlDane` <br> <br>
>> - prywatne składowe:
>>   - string tytulNaukowy
>>   - float numerPokoju
>
>> **Pracownik** - klasa pochodna:
>> - publiczne metody:  
>>    - konstruktor  
>>    - `wyswietlDane` <br> <br>
>> - prywatne składowe:
>>   - string stanowisko

#### Składnia
```C++
class Klasa_podstawowa
{
    // Zawartość klasy podstawowej
};

class Klasa_pochodna: typ_dziedziczenia Klasa_podstawowa
{
    // Zawartość klasy pochodniej
};
```

### Typy dziedziczenia - kontrola dostępu Public, Protected i Private
> Wewnątrz klasy różne pola mogą mieć rórzny typ dostępu:
> - `private:` - **dostęp prywatny, (domyślny)** - nie można wykożystać zmiennych i metod zdefiniowanych w klasie "na zewnątrz klasy"<br><br>
> - `protected:` - **dostęp chroniony** - d. prywatny + **klasy dzidziczące** mają dostęp do zmiennych chronionych <br><br>
> - `public:` - **dostęp publiczny (domyślny w strukturach)** - stłay dostęp do zmiennych i funkcji w całym kodzie
> 
![[Dostęp do klas w C++.png]]
### Zastępowanie funkcji
```C++

```
### Typy dziedziczenia
```C++

```
### Funkcja znajomego i klasy znajomego
```C++

```
### Funkcja wirtualna
```C++

```
### Szablony


## Biblioteki w C++
> **Biblioteki** - 


## Fstream - Pliki w C++
> **Program po zakończenieniu działania traci dane**, które obliczał  
> Aby utrwalić informaje zapisuje się je w **plikach**  
> **Później** przy ponownym uruchomieniu jesteśmy wstanie je **odczytać i pobrać**, a co zatym idzie wykonywać na nich operacje  
> **Biblioteka działania na plikach** `#include <fstream>`

### Klasy w fstream
|Klasa|Znaczenie|
|-|-|
|`ofstream`|Tworzenie i zapisywanie do pliku|
|`ifstream`|Odczyt danych z pliku|
|`fstream` |Kombinacja ofstream i ifstream: tworzy, odczytuje i zapisuje do pliku|ów

### Ifstream - Odczyt danych z pliku
```C++
ifstream nazwa_zmiennej_plikowej("Ścierzka_do_pliku");

Zawartość pliku:
jeden dwa trzy
cztery piec szesc 

#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream plik("plik.txt"); // Strumień wejścia pliku - tylko pobieranie

    if (!plik) // Sprawdzanie istnienia pliku lub bez ! i kody odwrotnie
    {
        cout << "Plik nie istnieje!" << endl;
    }
    else
    {
        // code poniżej 3 przykłądy pobierania
		plik.close(); // Zamknięcie pliku
    }

    return 0;
}
```
> `>>` - wczytywanie danych  - przekierowanie do zmiennej, pomijanie znaków białych  
> - Zastosowanie np.: wczytywanie liczb do tablicy, w pliku ułorzenie liczb dowolne  
> - Zapis: `zmienna_plikowa >> zmienna`
```C++
while (!plik.eof()) // Wykonuje pętle aż do końca pliku - end of file
{
    string wyraz;
    plik >> wyraz;
    cout << wyraz;
}
plik.close(); // Zamknięcie pliku

Wynik:
jedendwatrzyczterypiecszesc
    lub
jedendwatrzyczterypiecszescszesc - zalerzy od kompilatora -> spacja na końcu pliku
Niwelacja:
wyraz = "";
```
> `getline` -  wczytywanie danych, pobierz całą linie - wraz ze znakami białymi, pomija Enter  
> - Zastosowanie np.: wczytywanie autora lub tytułów  
> - Zapis: `getline(zmienna_plikowa, zmienna_string)`
```C++
while (!plik.eof())
{
    string linia;
    getline(plik, linia);
    cout << linia;
}
plik.close();

Wynik:
jeden dwa trzycztery piec szesc
```
>`get` - wczytywanie danych, pobierz znak z pliku - pobiera znak jeden po drugim  
> - Zastosowanie, gdy ważne jest ułorzenie danych w pliku
> - Zapis: `zmienna_plikowa.get(zmienna_char)`
```C++
while (!plik.eof())
{
    char znak;
    plik.get(znak);
    cout << znak;
}
plik.close();

Wynik:
jeden dwa trzy
cztery piec szesc
```

### Ofstream - Zapis danych do pliku
```C++
ofstream nazwa_zmiennej_plikowej("Ścierzka_do_pliku");

#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ofstream plik("plik.txt"); // Strumień wejścia pliku - tylko zapisywanie, gdy plik nie istnieje to zostanie utworzony, gdy istnieje - kasowanie zawartości pliku przy otwarciu i zapis nowych danych

    if (!plik)
    {
        cout << "Plik nie istnieje!" << endl;
    }
    else
    {
        // code
        int cala = 1;
        string tekst = "To jest tekst\n";
        plik << tekst;
        plik << "To jest w cudzysłowie + znak \\n\n";
        plik << cala << "\t" << cala;

        plik.close();
    }

    return 0;
}

Wynik w pliku:
To jest tekst
To jest w cudzysłowie + znak \n
1	1
```

### Fstream - Pliki w różnych trybach
> - [Dokumentacja fstream](https://www.cplusplus.com/reference/fstream/fstream/)
#### Tryby otwarcia pliku
|Tryb otwarcia|Znaczenie|
|-|-|
|`ios::in`|Input - Otwiera plik do odczytu|
|`ios::out`|Output - Otwiera plik do zapisu|
|`ios::binary`|Otwiera plik w trybie binarnym|
|`ios::ate`|At end - Rozpoczyna przeglądanie pliku od ostatniego znaku|
|`ios::app`|Append - Wszystkie operacje zapisu są przeprowadzane na końcu pliku. Nie zmienia dotychczasowej zawartości pliku|
|`ios::trunc`|Trancate - Jeśli plik istniał to jego zawartość zostaje zastąpiona nową|
> 

#### Funkcje fstream
|Funkcja|Znaczenie|
|-|-|
|`open(name, mode)`|Otwiera plik o podanej nazwie i w podanym trybie|
|`is_open()`|Sprawdza czy strumień jest aktywny|
|`good()`|Sprawdza czy nie ma błędów w odczycie|
|`eof()`|Sprawdza czy odczyt się zakończył tj. osiągnął koniec pliku|
|`bad()`|Sprawdza czy nie wystąpił błąd przy zapisie|
|`close()`|Zamyka strumień odczytu / zapisu|



```C++
zmienna_plikowa.open("Ścierzka_do_pliku, tryb_otwarcia | drugi | itd.")

#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    fstream plik; // Utworzenie zmiennej plikowej XD

    plik.open("plik.txt", ios::in | ios::out | ios::app);

    if (!plik.good()) // lub (!plik.is_open())
    {
        cout << "Plik nie istnieje!" << endl;
		// exit(0); // Wyjście z programu
    }
    else
    {
        // code
        plik.close();
    }
    return 0;
}
```

#### Pliki binarne
> **Pliki binarne** - używane, gdy pliki tekstowe są niewystarczające  
> - **Wady i zalery:**
>   - **pliki tekstowe:**
>     - mogą być otwierane i edytowane
>     - dane do odczytu muszą być odczielone białymi znakami
>   - **pliki binarne:**
>     - są obsługiwane szybciej
>     - nadają się do przechowywania dużej ilości danych
>     - są minejsze:  
>  `4.8MB - plik.bin`  
>  `7,7MB - plik.txt`
>     - dane w nich są ułorzone jednda za drugą (brak problemów z odczytaniem)  <br> <br>
> `xxd -b plik.bin` - wyświetlanie zawartości pliku binarnego w terminalu Linux




```C++
plik.write(const char * bufor, rozmiar_bufora ilość_danych_do_zapisania); // Funkcja zapisująca do pliku binarnego
plik.read(char * bufor, rozmiar_bufora ilość_danych_do_zapisania); // Funkcja odczytująca plik binarny

strcpy(zmienna, "Nowy tekst"); // Teskt o stałej długości - biblioteka cstring; strcpy = string copy; zamiana ciągu na ciąg

POD - Plain Old Data (stare zwykłe dane) np.: int, char, bool, float, double, long, short itp.
// Wyszykać POD w kontekście klas w C++


PRZYKŁAD:
#include <iostream>
#include <fstream>
#include <cstring> // Biblioteka manipulowania napisami C i tablicami
using namespace std;

struct struktura // Można zapisać strukturę binarną, gdy posiada zmienne POD, czyli bez np.: string
{
    int num_1;
    float num_2;
    char znak;
    char znaki[40];
};

int main()
{
	// Zmienne i ich wartości do zapisania w pliku binarnym
    int num_1 = 100;
    float num_2 = 100.001;
    char znak = 'a';
    char znaki[40] = "To jest tekst o stalej dlugosci!"; // Tak naprawde 39 znaków + znak \0 (NULL)
    string tekst = "To jest tekst o dynamicznie alokowaniej pamieci!";

    struktura struktura_1; // Stworzenie objektu struktury i przypisanie wartości
    struktura_1.num_1 = 100;
    struktura_1.num_2 = 100.001;
    struktura_1.znak = 'a';
    strcpy(struktura_1.znaki, "To jest tekst o stalej dlugosci!");

    fstream plik; // Utworzenie zmiennej plikowej

    // Praca z plikiem binarnym do zapisu
    plik.open("plik.bin", ios::out | ios::binary);
    if (!plik.good()) // lub !plik.is_open()
    {
        cout << "Plik nie istnieje!" << endl;
        exit(0);
    }
    else
    {
        // Zmienne typu liczbowego
        plik.write((const char *)&num_1, sizeof num_1); // Int
        // Lub sizeof(int) plik.write((const char *)&num_1, sizeof(int));
        plik.write((const char *)&num_2, sizeof num_2); // Float

        // Zmienne typu znak
        plik.write((const char *)&znak, sizeof znak); // Char
        // lub plik.write(&znak, sizeof znak);

        // Teskt o stałej długości
        plik.write((const char *)&znaki, sizeof znaki); // Tablica char

        // Tekst string
        plik.write(tekst.c_str(), tekst.size() + 1); // String
        // c_str() - zwraca łańcych znaków w językach C
        // size() - pobiera długość łańcucha znaków, + 1 aby uwzględnić znak NULL - potrzebny do prawidłowego odczytania

        // Objekt struktury ze zmiennymi POD
        plik.write((const char *)&struktura_1, sizeof struktura_1); // Struktura POD
        plik.close();
    }

    // Przypisanie nowych wartości = sprawdzenie dla odczytywania
    num_1 = 0;
    num_2 = 0;
    znak = '0';
    strcpy(znaki, "Nowy tekst"); // Podmiana tekstu o stałej długości
    tekst = "Nowy tekst";

    struktura_1.num_1 = 0;
    struktura_1.num_2 = 0;
    struktura_1.znak = '0';
    strcpy(struktura_1.znaki, "Nowy tekst");

    // Praca z plikiem binarnym do odczytu
    plik.open("plik.bin", ios::in | ios::binary);
    if (!plik.good()) // lub !plik.is_open()
    {
        cout << "Plik nie istnieje!" << endl;
        exit(0);
    }
    else
    {
        // Zmienne typu liczbowego
        plik.read((char *)&num_1, sizeof num_1); // Int
        cout << "Zmienna int = " << num_1 << endl;

        plik.read((char *)&num_2, sizeof num_2); // Float
        cout << "Zmienna float = " << num_2 << endl;

        // Zmienne typu znak
        plik.read((char *)&znak, sizeof znak); // Char
        cout << "Zmienna char = " << znak << endl;

        // Teskt o stałej długości
        plik.read((char *)&znaki, sizeof znaki); // Tablica char
        cout << "Tablica char = " << znaki << endl;

        // Tekst string
        getline(plik, tekst, '\0'); // String
		// Nazwa pliku dla programu, typ zmiennej do zapisania, + aż napotkasz znak NULL - \0
        cout << "Tekst string = " << tekst << endl;

        // Objekt struktury ze zmiennymi POD
        plik.read((char *)&struktura_1, sizeof struktura_1); // Struktura POD
        cout << "Struktura POD:"
             << "\n"
             << "Int = " << struktura_1.num_1 << "\n"
             << "Float = " << struktura_1.num_2 << "\n"
             << "Char = " << struktura_1.znak << "\n"
             << "Tablica char = " << struktura_1.znaki << endl;

        plik.close();
    }
    return 0;
}

Wynik - zapis w pliku binarnym plik.bin wartości zmiennych; odczytany z pliku binarnego:
Zmienna int = 100
Zmienna float = 100.001
Zmienna char = a
Tablica char = To jest tekst o stalej dlugosci!
Tekst string = To jest tekst o dynamicznie alokowaniej pamieci!
Struktura POD:
Int = 100
Float = 100.001
Char = a
Tablica char = To jest tekst o stalej dlugosci!
```


https://www.programiz.com/cpp-programming/constructors
https://www.youtube.com/watch?v=jhKxPe_p2dA&list=PL_1QM_dtCJDcV4qcY4Y2k8vk0thByI2vJ&index=36&ab_channel=AitraAitra











```C++

```

```C++

```

```C++

```

```C++

```




