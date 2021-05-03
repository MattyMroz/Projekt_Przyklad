# Projekt_Przyklad
Przykładowy projekt od nauki
---
__Reklama :)__

- __ [pica] (https://nodeca.github.io/pica/demo/) __ - wysoka jakość i szybki obraz
  zmienić rozmiar w przeglądarce.
- __ [babelfish] (https://github.com/nodeca/babelfish/) __ - przyjazny dla programistów
  i18n z obsługą liczby mnogiej i prostą składnią.

Spodoba ci się te projekty!

---

# h1 Nagłówek 8-)
## h2 Nagłówek
### h3 Nagłówek
#### h4 Nagłówek
##### h5 Nagłówek
###### h6 Nagłówek

## Zasady horyzontalne

___

---

***


## Zastępstwa typograficzne

Włącz opcję typograficzną, aby zobaczyć wynik.

(c) (C) (r) (R) (tm) (TM) (p) (P) + -

test.. test... test..... test?..... test!....

!!!!!! ???? ,, - ---

„Smartypants, podwójne cudzysłowy” i „pojedyncze cudzysłowy”


## Nacisk

**To jest pogrubiony tekst**

__To jest pogrubiony tekst__

*To jest kursywa*

_To jest kursywa_

~~Przekreślenie~~


## Cytaty blokowe


> Cytaty blokowe można również zagnieżdżać ...
>> ... używając dodatkowych znaków większości bezpośrednio obok siebie ...
>>> ... lub ze spacjami między strzałkami.


## Listy

Niezamówiony

+ Utwórz listę, zaczynając linię od `+`, `-` lub` * `
+ Podlisty są tworzone przez wcięcie 2 spacji:
  - Zmiana znaku markera wymusza początek nowej listy:
    * Ac tristique libero volutpat at
    + Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit
+ Bardzo proste!

Zamówione

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa


1. Możesz użyć kolejnych numerów ...
1. ... lub zachowaj wszystkie liczby jako `1`

Rozpocznij numerację z przesunięciem:

57. foo
1. bar


## Kod

Wbudowany `kod`

Kod z wcięciem

    // Kilka komentarzy
    linia 1 kodu
    linia 2 kodu
    linia 3 kodu


Kod blokowy „ogrodzenia”

```
Przykładowy tekst tutaj...
```

Podświetlanie składni

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

[tekst linku](http://dev.nodeca.com)

[link z tytułem](http://nodeca.github.io/pica/demo/ "tekst tytułu!")

Łącze z automatyczną konwersją https://github.com/nodeca/pica (włącz linkify, aby zobaczyć)


## Obrazy

![Minion](https://octodex.github.com/images/minion.png)
![Stormtroopocat](https://octodex.github.com/images/stormtroopocat.jpg "The Stormtroopocat")

Podobnie jak linki, obrazy mają również składnię w stylu przypisów

![Alt text][id]

Z odniesieniem w dalszej części dokumentu określającego lokalizację adresu URL:

[id]: https://octodex.github.com/images/dojocat.jpg  "The Dojocat"



## Wtyczki

Zabójczą cechą programy `markdown-it` jest bardzo skutecznym obsługa
[wtyczk składniowych](https://www.npmjs.org/browse/keyword/markdown-it-plugin).


### [Emoji](https://github.com/markdown-it/markdown-it-emoji)

> Klasyczne znaczniki:: mrugnięcie:: zgniatanie:: płacz:: łza:: śmiech:: mniam:
>
> Skróty (emotikony): :-) :-( 8-) ;)

zobacz [jak zmienić wyjście](https://github.com/markdown-it/markdown-it-emoji#change-output) z twemoji.


### [Indeks](https://github.com/markdown-it/markdown-it-sub) / [Indeks górny](https://github.com/markdown-it/markdown-it-sup)

- 19^th^
- H~2~O


### [\<ins>](https://github.com/markdown-it/markdown-it-ins)

++Wstawiony tekst++


### [\<mark>](https://github.com/markdown-it/markdown-it-mark)

==Zaznaczony tekst==


### [Przypisy](https://github.com/markdown-it/markdown-it-footnote)

Przypis 1 link[^first].

Przypis 2 link[^second].

Przypis wewnętrzny^[Tekst wbudowanego przypisu] definicja.

Powielone odniesienie do przypisu[^second].

[^first]: Footnote **może mieć znaczniki**

    i wiele akapitów.

[^second]: Tekst przypisu.


### [Listy definicji](https://github.com/markdown-it/markdown-it-deflist)

:	Termin 1

	Definicja 1 z leniwą kontynuacją.

Termin 2 ze _znacznikami wbudowanymi_

:	Definicja 2

		{ jakiś kod, część definicji 2 }
	
	Trzeci akapit definicji 2

_Kompaktowy styl:_

Termin 1

	~ Definicja 1

Termin 2

	~ Definicja 2a
	~ Definicja 2b


### [Skróty](https://github.com/markdown-it/markdown-it-abbr)

To jest przykład skrótu HTML .

Konwertuje „ HTML ”, ale zachowuje nienaruszone częściowe wpisy, takie jak „xxxHTMLyyy” i tak dalej.

### [Kontenery niestandardowe](https://github.com/markdown-it/markdown-it-container)

::: warning
*tu będą smoki*
:::
