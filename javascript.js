function Klient(nazwisko, imie) {
    this.nazwisko_k = nazwisko;
    this.imie_k = imie;
}
Klient.prototype.zawod = 'kierowca';
Klient.prototype.pisz_dane = function () {
    document.write(this.nazwisko_k + ' ' + this.imie_k);
}
var osoba1 = new Klient("Malinowski", "Oskar", "kierowca");
osoba1.pisz_dane();


function Uczen(nazwisko, imie, wiek, klasa, sport) {
    this.nazwisko_u = nazwisko;
    this.imie_u = imie;
    this.wiek_u = wiek;
    this.klasa_u = klasa;
    this.sport_u = sport;
    this.wypisz = function () {
        document.write(this.nazwisko_u + ' ' + this.imie_u + ' '
            + this.wiek_u + ' lat, sport: ' + this.sport_u + '.' + "<br>");
    }
}

var uczen1 = new Uczen("Nowak", "Paweł", 12, "5b", "tenis");
var uczen2 = new Uczen("Polak", "Anna", 13, "6a", "pływanie");
var uczen3 = new Uczen("Czaja", "Maciej", 13, "6a", "siatkówka");
var uczen4 = new Uczen("Malak", "Julia", 12, "5c", "gimnastyka");
var uczen5 = new Uczen("Wojak", "Michał", 13, "6b", "pływanie");

uczen1.wypisz();
uczen2.wypisz();
uczen3.wypisz();
uczen4.wypisz();
uczen5.wypisz();

function Klient(nazwisko_k, imie_k, zawod_k) {
    this.nazwisko = nazwisko_k;
    this.imie = imie_k;
    this.zawod = zawod_k;
    this.wypisz = function () {
        alert(this.nazwisko + ' ' + this.imie);
    }
}

var osoba = new Klient('Kowalski', 'Jan', 'programista');
osoba.wypisz();
document.write(osoba.nazwisko + ' ' + osoba.imie + ' ' + osoba.zawod);






var pojazd = {
    marka: "Ford",
    model: "Mustang",
    rok_produkcji: "2020",
    przebieg: 15000,
    wyswietlDane: function () {
        document.write(this.marka + ' ' + this.model + ', rok produkcji: '
            + this.rok_produkcji + "<br>");
    }
};
pojazd.wyswietlDane();
pojazd.numer_rej = "WA34789";
pojazd.wyswietlDetal = function () {
    document.write('Marka: ' + this.marka + ', numer rejestracyjny: '
        + this.numer_rej);
}
pojazd.wyswietlDetal();


var pojazd = {
    marka: "Fiat",
    model: "500",
    rok_produkcji: "2005",
    przebieg: "120000",
    numer_rej: "2000",
    wyswietlDane: function () {
        document.write("Marka pojazdu: " + this.marka + "<br>");
        document.write("Model pojazdu: " + this.model + "<br>");
        document.write("Rok produkcji: " + this.rok_produkcji + "<br>");
        document.write("Przebieg: " + this.przebieg + "<br>");
        document.write("Numer rejestracyjny: " + this.numer_rej + "<br>");
    }
};
pojazd.wyswietlDane();



var osoba = {
    imie: "Piotr",
    nazwisko: "Zalewski",
    wiek: 44,
    kolorOczu: "niebieski",
    podpis: function () { return this.imie + " " + this.nazwisko; }
};

osoba.imie = "Janusz";
osoba.nazwisko = "Nowak";
osoba.wiek = 33;
osoba.kolorOczu = "czerwony";
alert(osoba.podpis());

var osoba2 = new osoba();


// 1. funkcja 3 argumenty zwraca minimalną wartość tych argumentów
var a = parseInt(prompt("Podaj pierwszą liczbę:"));
var b = parseInt(prompt("Podaj drugą liczbę:"));
var c = parseInt(prompt("Podaj trzecią liczbę:"));
function minimalna(a, b, c) {
    if (a < b && a < c) {
        return a;
    } else if (b < a && b < c) {
        return b;
    } else {
        return c;
    }
}
alert("Minimalna wartść to: " + minimalna(a, b, c));

// 2. funkcja która sprawdza za pomocą pętli czy liczba jest pierwsza
var liczba = parseInt(prompt("Podaj liczbę:"));
function pierwsza(liczba) {
    for (var i = 2; i < liczba; i++) {
        if (liczba % i == 0) {
            return false;
        }
    }
    return true;
}
alert("Czy jest pierwsza, wynik to: " + pierwsza(liczba));

// Zadanie 1
var a = parseInt(prompt("Podaj pierwsza liczbe"));
var b = parseInt(prompt("Podaj druga liczbe"));
var c = parseInt(prompt("Podaj trzecia liczbe"));

function isTreangle(a, b, c) {
    if (a + b > c && a + c > b && b + c > a) {
        alert("To jest trójkąt");
    }
    else {
        alert("To nie jest trójkąt");
    }
}
isTreangle(a, b, c);


//Zadanie 2
var rok = prompt("Podaj rok:");

function czyPrzestepny(rok) {
    rok = parseInt(rok);
    if (rok % 4 == 0 && rok % 100 != 0 || rok % 400 == 0) {
        alert("Rok " + rok + " jest przestępny");
    } else {
        alert("Rok " + rok + " nie jest przestępny");
    }
}
czyPrzestepny(rok);

// Zadanie 3
function srednia() {
    var ile = parseInt(prompt("Podaj ile liczb chcesz wprowadzić:"));
    var suma = 0, liczba;
    for (var i = 0; i < ile; i++) {
        liczba = parseFloat(prompt("Podaj liczbe"));
        suma += liczba;
    }
    alert(suma / liczba);
}
srednia();

