typeof 23; // number
typeof "tekst"; // string
typeof "45"; // string
typeof true; // boolean
typeof{data:10 }; // object
typeof undefined; // undefined
typeof 1n; // bigint
typeof Symbol(); // symbol
typeof function (){}; // function
typeof []; // object
// objectwtypeof dla null to błądwJavaScript, który
// nigdy nie zostanie poprawiony
typeof null; // object

var b = 123;
let txt `tekst ${b}, 
${23 + 23 * 1} 
zachowanie Enterów`; // Operacje na stringu



///////////// krótki if
let age=18;
let data(age >= 18)?"dorosły":"nieletni";
// tosamo CO
if( age >= 18){
    data="dorosły";
}else{
    data="nieletni";
}


/////////////////////////////////
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




// zaokrąglanie liczb 2 metody
var x= 100.96756432;

Number.prototype.round = function(places) {
    return +(Math.round(this + "e+" + places) + "e-" + places);
}

Number.prototype.toFixedDown = function(digits) {
    var re = new RegExp("(\\d+\\.\\d{" + digits + "})(\\d)"),
        m = this.toString().match(re);
    return m ? parseFloat(m[1]) : this.valueOf();
}

document.write(x.round(3));
document.write(x.toFixedDown(3));








/////////////////// wysyłanie formularza 
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Document</title>
    <style>
        label,
        input.btn {
            display: block;
            margin-top: 10px;
        }
    </style>
</head>

<body>
    <form action="index.php" method="post">
        <label for="imie">Imie</label>
        <input type="text" name="imie" id="imie">
        <label for="nazwisko">Nazwisko</label>
        <input type="text" name="nazwisko" id="nazwisko">
        <label for="pesel">Pesel</label>
        <input type="text" name="pesel" id="pesel">
        <input type="submit" value="Wyslij" class="btn">
    </form>

    <script src="src/javascript.js"></script>
    <script>
        const imie = document.getElementById('imie');
        const nazwisko = document.getElementById('nazwisko');
        const pesel = document.getElementById('pesel');
        const btn = document.getElementsByClassName('btn')[0];

        btn.addEventListener('click', function (e) {
            e.preventDefault();
            if (imie.value.length < 1) {
                alert('Imie jest za krótkie');
                imie.focus();
                return;
            }
            if (nazwisko.value.length < 1) {
                alert('Nazwisko jest za krótkie');
                nazwisko.focus();
                return;
            }
            if (pesel.value.length != 11) {
                alert('Pesel musi miec 11 znakow');
                pesel.focus();
                return;
            }
            this.form.submit();

        });
    </script>
</body>
<!-- <script src="https://code.jquery.com/jquery-3.6.0.js"
    integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script> -->

</html>







///////////////// FABRYKA SAMOCHODÓW
    <script>
        var CarPlant = {
            numProducedCars: 0,
            carsArr: [],
            makeCar: function (brand, model, year) {
                var car = {
                    brand: brand,
                    model: model,

                    year: year
                };
                this.numProducedCars++;
                this.carsArr.push(car);
                return car;
            },
            printStats: function () {
                console.log("Ilość wyprodukowanych aut:" + this.numProducedCars);
            }
        };
    </script>


////////////////////////// sklep
    <script>
        let ShopingCart = {
            items: [],
            add: function (name, price) {
                this.items.push({
                    name: name,
                    price: price
                });
            },
            remove: function (name) {
                for (let i = 0; i < this.items.length; i++) {
                    if (this.items[i].name === name) {
                        this.items.splice(i, 1);
                    }
                }
            },

            removeByIndex: function (index) {
                this.items.splice(index, 1);
            },

            getTotal: function () {
                let total = 0;
                for (let i = 0; i < this.items.length; i++) {
                    total += this.items[i].price;
                }
                return total;
            },

            getItems: function () {
                return this.items;
            },

            printInfo: function () {
                let finalPrice = 0;
                for (let i = 0; i < this.items.length; i++) {
                    let element = this.items[i];
                    finalPrice += element.price;
                    console.log(element.name + ": " + element.price);
                }
                console.log("Total price: " + finalPrice);
            }
        }

        ShopingCart.add("Milk", 1.5);
        ShopingCart.add("Bread", 2);
        ShopingCart.add("Eggs", 3);

        ShopingCart.printInfo();

        ShopingCart.remove("Milk");
        ShopingCart.printInfo();

        ShopingCart.removeByIndex(1);
        ShopingCart.printInfo();


        console.log(ShopingCart.getItems());
        console.log(ShopingCart.getTotal());
    </script>




//////////////////////
