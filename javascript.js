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

/////////////// przecinek w pętli
for(let i = 0, j = 5; i < 5; i++, j--){
    console.log("i:" + i + "j:" + j);
}
/*
i:0 j:5
1:1 j:4
i:2 j:3
i:3 j:2
i:4 j:1
*/

var c = +"27"; // operator+konwertuje operand na liczbę, c=27
var d = -"27"; // number: -27
var e = void 0; // void wywołuje wyrażenieizwraca undefined var


// Operatory relacyjne
let obj{num: 10 };
if( "num" in obj) console.log (" zmienna numwobj"); // zmienna num jestwobj
let arr ["one", "two", "three"];
if(1in arr)console.log("indeks1jestwtablicy");
if( "length" in arr)console.log("właściwość length jestwtablicy");

////////////// Błąd zmiennych globalnych i lokalnych
function check(){
    "use strict";
   AnewNum 200; // normalnie stanie się zmienną globalną, ale powyższa linia temu zapobiega i jest ok
}
// ale teraz jest słowo let i jest to deklaracja zmiennej lokalnej co za tym idzie niweluje ona będy które może powodować var - zmienna globalna
// tak samo w const
czyli używac let i const i będzie ok










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




////////////////////// Galeria
<!DOCTYPE html>
<html lang="pl-PL">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- =============== METADATA =============== -->
    <meta name="description" content="Opis zawartości strony dla wyszukiwarek">
    <meta name="keywords" content="słowa, kluczowe, opisujące, zawartość">
    <meta name="author" content="Mateusz Mróz">

    <!-- =============== TITLE =============== -->
    <title>MyWebside</title>

    <!-- =============== FAVICONS =============== -->
    <link rel="shortcut icon" href="assets/img/favicon.png" type="image/x-icon">

    <!-- =============== REMIXICON =============== -->
    <link href="https://cdn.jsdelivr.net/npm/remixicon@2.5.0/fonts/remixicon.css" rel="stylesheet">

    <!-- =============== SWIPER CSS =============== -->
    <link rel="stylesheet" href="">

    <!-- =============== CSS =============== -->
    <!-- <link rel="stylesheet" href="assets/css/styles.css"> -->
    <link rel="stylesheet" href="assets/css/styles.css">

    <style>
        *,
        *::before,
        *::after {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            transition: .2s linear;
        }

        /*
        body::-webkit-scrollbar {
            display: none;
        } */


        body {
            background-color: rgb(56, 56, 56);
        }

        .pictures {
            /* background-color: blueviolet; */
            width: 100%;
            height: 1000px;
        }

        .big__img__div {
            margin: auto;
            width: 1000px;
            height: 600px;
            padding: 50px 0;
        }

        #big__img {
            width: 100%;
            height: 100%;
            cursor: pointer;
            border: 2px solid black;
            border-radius: 10px;
        }

        .small__img__div {
            margin: auto;
            width: 100%;
            height: 400px;
            /* background-color: red; */
            display: flex;
            justify-content: space-evenly;
            align-items: center;
        }

        .small__img__div div {
            width: 600px;
            height: 300px;
        }

        .small__img {
            width: 100%;
            height: 100%;
            cursor: pointer;
            border: 2px solid black;
            border-radius: 10px;
        }
    </style>
</head>

<body>
    <!-- =============== GALERIA =============== -->
    <div class="pictures">
        <div class="big__img__div">
            <img id="big__img" src="https://picsum.photos/1000/500?grayscale" alt="obraz1">
        </div>
        <div class="small__img__div">
            <div>
                <img class="small__img" src="https://picsum.photos/1000/500" alt="obraz2">
            </div>
            <div>
                <img class="small__img" src="https://picsum.photos/seed/picsum/1000/500" alt="obraz3">
            </div>
            <div>
                <img class="small__img" src="https://picsum.photos/id/237/1000/500" alt="obraz4">
            </div>
        </div>
    </div>

    <!-- =============== JQUERY =============== -->
    <script src="https://code.jquery.com/jquery-3.6.0.js"
        integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.9.1/gsap.min.js"></script>

    <!-- =============== MAIN JS =============== -->
    <script src="assets/js/main.js"></script>

    <script>
        $(".small__img").click(function () {

            // podmiana małedo na duży i dużego na mały przy kliknięciu ze znikaniem i pojawianiem się 

            let big__img = $("#big__img");
            let small__img = $(this);
            let big__img__src = big__img.attr("src");

            big__img.fadeOut(400);
            small__img.fadeOut(400);

            setTimeout(function () {
                big__img.attr("src", small__img.attr("src"));
                small__img.attr("src", big__img__src);
            }, 500);

            big__img.fadeIn(500);
            small__img.fadeIn(500);
        });
    </script>

</body>

</html>
