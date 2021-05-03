---
	METADANA niewidoczna część notatki w Obsidian
---

# Markdown składnia
___
## Nagłówki
# h1 Nagłówek
## h2 Nagłówek
### h3 Nagłówek
#### h4 Nagłówek
##### h5 Nagłówek
###### h6 Nagłówek

h1 Nagłówek
===============
h2 Nagłówek
---------------


## Podział - kreska
___
---
***


## Podział wierszy i akapitów
Wiersz 1 -> Trzy spacje + Enter ->   
Wiersz 2

Wiersz 1 -> znacznik HTML "br" -> <br>
Wiersz 2

Akapit 1 -> Enter + Enter ->

Akapit 2


## Formatowanie

**Pogrubiony tekst** -> w środku zdania

__Pogrubiony tekst__

*Kursywa*  -> w środku zdania

_Kursywa_

***Pogrubiona kursywa*** -> w środku zdania

~~Przekreślenie~~

==Zaznaczony tekst==

Niwelacja działania znaków specjalnych poprzez znak \\ - działa na: \\ \` * _ {} [] <> () # + - . ! |   
\- Ze znakiem \\
- Bez znaku \\

-> Do formatowania można również używać znaczników **HTML**


## Cytaty blokowe

> Cytaty blokowe można zagnieżdżać ...
>> ... używając dodatkowych znaków większości bezpośrednio obok siebie ...
> > > ... lub ze spacjami między strzałkami, ... <br>   
>>> a także łamać wiersza trzema spacjami lub znacznikiem "br", ...
>>
>> żeby opuścić zagnieżdżenie należy użyć tej samej ilości znaków większości + Enter ... 
> 
> dziwne co nie.


## Listy

Utwórz listę nieuporządkowaną, zaczynając linię od `+`, `-` lub` * `
+ plus
- minus
* gwiazdka

Utwórz listę uporządkowaną, zaczynając linię od 1. 2. 3. 

1.  Pierwsza pozycja
2.  Druga pozycja
3.  Trzecia pozycja

Utwórz listę uporządkowaną, zaczynając linię od 1. 1. 1.
1.  Pierwsza pozycja
1.  Druga pozycja
1.  Trzecia pozycja

Utwórz listę uporządkowaną, zaczynając linię - licząc od 100. 1. 1. 2. 3 itp.

100. foo
1.  Pierwsza pozycja
1.  Druga pozycja
2.  Trzecia pozycja

Utwórz listę zagnieżdżoną -> Enter + Tab
1.  Pierwsza pozycja
	-  Podpunkt jeden
	-  Podpunkt dwa
2.  Druga pozycja
	1.  Podpunkt jeden
	2.  Podpunkt dwa

Rozpoczynanie nieuporządkowanych elementów listy z numerami -> \\
- 2020\.
- 2021


## Bloki kodu

Kod nieoznaczony -> `kod`

Kod z wcięciem -> Enter + Tab

	Kilka komentarzy
    linia 1 kodu
    linia 2 kodu
    linia 3 kodu


Nieoznaczony kod z ogrodzeniem ->  \```kod```

```
Przykładowy tekst tutaj...
```

Podświetlanie składni języka programowania -> \``` nazwa języka -> Enter -> kod -> Enter```

``` js
var foo = function (bar) {
  pasek powrotu ++;
};

console.log (foo (5));
```


## Tabele

| Opcja | Opis |
| ------ | ----------- |
| dane | ścieżka do plików danych w celu dostarczenia danych, które zostaną przekazane do szablonów. |
| silnik | silnik do przetwarzania szablonów. Kierownica jest ustawieniem domyślnym. |
| ext | rozszerzenie, które ma być używane dla plików dest. |

Kolumny wyrównane do prawej

| Opcja | Opis |
| ------: | -----------: |
| dane | ścieżka do plików danych w celu dostarczenia danych, które zostaną przekazane do szablonów. |
| silnik | silnik do przetwarzania szablonów. Kierownica jest ustawieniem domyślnym. |
| ext | rozszerzenie, które ma być używane dla plików dest. |


## Linki

-> [Tekst linku](http://dev.nodeca.com)

-> [Link z tytułem](http://nodeca.github.io/pica/demo/ "Tekst tytułu!")

Link z automatyczną konwersią -> https://github.com/nodeca/pica


## Obrazy

| Obraz |Obraz z tytułem | Obraz z linkiem do obrazu i tytułem w przypisie  |Obraz z linkiem wysyłającym do źródła i tytułem|
| ----- | ----- | ----- | ----- |

![Obraz1](https://picsum.photos/seed/picsum/150)
![Obraz2](https://picsum.photos/seed/picsum/150 "Tekst tytułu!")
![Obraz3][id]
[![Obraz4](https://picsum.photos/seed/picsum/150)](https://www.youtube.com/  "Tekst tytułu!")

[id]: https://picsum.photos/seed/picsum/150  "Tekst tytułu!"


## Przypisy Obsidian

Przypis 1 link[^1].

Przypis 2 link[^2].

Powielone odniesienie do przypisu[^2].

Przypis wewnętrzny^[Tekst wbudowanego przypisu] definicja.

[^1]: Notka **może mieć znaczniki**

	i wiele akapitów.

[^2]: Tekst przypisu 2.
