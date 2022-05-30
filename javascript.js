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



<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Document</title>
    <style>
        *,
        *::before,
        *::after {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Open Sans', sans-serif;
            background-color: #414141;
        }

        .content {
            width: 1300px;
            height: 2000px;
            margin: 0 auto;
            padding: 30px;
            background-color: #282e2f;
            position: relative;
            display: flex;
            justify-content: center;
            /* align-items: center; */

        }

        .nav {
            margin-top: 140px;
            width: 300px;
            height: auto;
            display: flex;
            flex-direction: column;
        }

        .imgs img {
            width: 300px;
            height: 150px;
            padding-bottom: 20px;
            /* background-color: #414141; */
        }

        .czas {
            width: 200px;
            height: 100px;
            background-color: #6a6a6a;
            top: 20px;
            right: 20px;
            position: absolute;
            border-radius: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 10px 20px;
        }

        .czas p {
            color: #fff;
            font-size: 25px;
            font-weight: bold;
        }

        .slider {
            width: 900px;
            height: 500px;
            background-color: #fff;
            margin: 140px auto;
        }

        .slider img {
            width: 900px;
            height: 500px;
        }

        .tekst_reklamowy {
            width: 900px;
            height: 50px;
            background-color: #414141;
            margin: 10px auto;
            color: #fff;
            font-size: 30px;
            font-weight: bold;
            border-radius: 10px;
            display: flex;
            align-items: center;
        }

        input {
            width: 900px;
            height: 50px;
            background-color: #414141;
            margin: 10px auto;
            padding: 10px;
            color: #fff;
            font-size: 30px;
            font-weight: bold;
            border-radius: 10px;
            display: flex;
            align-items: center;
        }
    </style>
</head>

<body>
    <!-- Utwórz stronę internetową, na której w prawym górnym rogu będą wyświetlane bieżąca data i czas. W nagłówku strony znajdzie się slider ze zdjęciami, które będą się zmieniały co 10 sekund. Poniżej slidera ma być umieszczony baner reklamowy z tekstem
    Witamy na naszej stronie, który będzie „płynął” od prawej do lewej krawędzi strony.
    Z lewej strony zostanie utworzone menu pionowe składające się z trzech gotowych ikon
    (wcześniej przygotowanych w postaci plików graficznych). Najechanie na każdą z ikon
    kursorem myszy ma spowodować zmianę jej wyglądu. Odsunięcie kursora ma skutkować przywróceniem poprzedniego wyglądu ikony. Kliknięcie pierwszej ikony spowoduje przeniesienie do strony www.men.gov.pl, drugiej — do strony www.cke.edu.pl, a trzeciej — do strony http://helion.pl. W swojej pracy wykorzystaj skrypty języka JavaScript. -->
    <div class="content">
        <div class="czas">
            <p class="data_i_godzina"></p>
        </div>
        <div class="nav">
            <div class="imgs">
                <a href="https://www.gov.pl/web/edukacja-i-nauka"><img
                        src="data:image/jpeg;base64,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FrNcXSoBwzW1U9WYe4ytK/JRtamTlpo3VdKq6++xgF+bUx+EoIWrvRRALnOV4eB4zl3enE0auLr1MOuWi1QmmoFtO5Rwudbd8lOH5Jdq1SMyU073qg28luZP9y+SWjg3WtiXFequqqFy0kI4Gx1cjtPugEv3GwL4bZ+EpOLOlFAw7DluRN9EQDCaCk3yrftsLzLafYgCIiAIiIAnxlvPsQDFSoqvoqF8AB8pqt9fV+L9hU+gzdTU7z4V6+DxFKmLu9J0UcLsykAXPfAOUsD/ANyn+NfqE6/KAixAI75zjheTDaquhOHFgyk/0icAQT1zpBeEA/KUwvAAeAtMkRAEREAREQBERAEREASqNrevl9rS+hJa8qja3r5fa0voSV1NDX2P8dX5JecS14iJYZAny0+xAMP2dD91fcI+zJ+qvuEzRANdjNj4euuWpRpsO9RfyPESM7H3BoUa1R6g5xM39EjG4Atclh1m9xr2SbxPHFPMvpYqtSg4Qk0nr74fQ8qYKkostNAOwKAPgJ+/stP9RfcJnielBjSko4ADwFp+7T7EAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREASqNrevl9rS+hJa8jGI3Sp1MYMWaj5sytlstugAAOF/uyE4trI0NnYmnQlNzesWl1bXoSeIiTM8REQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAP/9k="
                        alt=""></a>
            </div>
            <div class="imgs">
                <a href="https://cke.gov.pl/"><img src="https://zs-chojnice.pl/wp-content/uploads/2020/03/cke4.jpg"
                        alt=""></a>
            </div>
            <div class="imgs">
                <a href="https://helion.pl/"><img
                        src="https://jug-jawor.joomla.pl/images/sponsorzy/helion_logo_1024.jpg" alt=""></a>
            </div>

        </div>
        <div class="slider">
            <div class="imgs_slider">
                <img src="https://picsum.photos/id/1/900/550" alt="ok" id="baner">
            </div>
            <div class="tekst_reklamowy">
                <!-- <p></p> -->
                <form name="napis">
                    <input id="tekst" name="text" size=1000
                        value=" Witamy na naszej stronie!                                                                 ">
                </form>
            </div>
        </div>


    </div>



    <script src="src/javascript.js"></script>
    <script>
        setInterval(function () {
            let dni = ['Niedziela', 'Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota'];
            let miesiace = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień',
                'Wrzesień', 'Październik', 'Listopad', 'Grudzień'
            ];
            data = new Date();
            godzina = data.getHours();
            minuty = data.getMinutes();
            sekundy = data.getSeconds();
            dzien = data.getDay();
            miesiac = data.getMonth();
            rok = data.getFullYear();

            document.querySelector('.data_i_godzina').innerHTML =
                `${dni[dzien]} ${miesiace[miesiac]} ${rok} ${godzina}:${minuty}:${sekundy}`;
        }, 1000);


        // galeria zdjęć
        let nr = 0;

        window.onload = zmiana;

        function zmiana() {

            let obrazy = ["https://picsum.photos/id/1/900/500", "https://picsum.photos/id/2/900/500",
                "https://picsum.photos/id/3/900/500", "https://picsum.photos/id/4/900/500",
                "https://picsum.photos/id/5/900/500", "https://picsum.photos/id/6/900/500",
                "https://picsum.photos/id/7/900/500", "https://picsum.photos/id/8/900/500",
                "https://picsum.photos/id/9/900/500", "https://picsum.photos/id/10/900/500",
                "https://picsum.photos/id/11/900/500", "https://picsum.photos/id/12/900/500",
                "https://picsum.photos/id/13/900/500", "https://picsum.photos/id/14/900/500",
                "https://picsum.photos/id/15/900/500", "https://picsum.photos/id/16/900/500",
                "https://picsum.photos/id/17/900/500", "https://picsum.photos/id/18/900/500",
                "https://picsum.photos/id/19/900/500", "https://picsum.photos/id/20/900/500",
                "https://picsum.photos/id/21/900/500", "https://picsum.photos/id/22/900/500",
                "https://picsum.photos/id/23/900/500", "https://picsum.photos/id/24/900/500",
                "https://picsum.photos/id/25/900/500", "https://picsum.photos/id/26/900/500",
                "https://picsum.photos/id/27/900/500", "https://picsum.photos/id/28/900/500",
                "https://picsum.photos/id/29/900/500", "https://picsum.photos/id/30/900/500"
            ];

            nr++;
            if (nr == obrazy.length) {
                nr = 0;
            }

            let baner = document.getElementById("baner");

            baner.src = obrazy[nr];

            setTimeout(zmiana, 3000);

        }



        let imgs = document.querySelectorAll('.imgs');

        for (let i = 0; i < imgs.length; i++) {
            imgs[i].addEventListener('mouseover', function () {
                imgs[i].style.opacity = '0.5';
            });
            imgs[i].addEventListener('mouseout', function () {
                imgs[i].style.opacity = '1';
            });
        }



        czas = 200;
        znak_p = 1;

        function przewin() {
            window.setTimeout(przewin, czas);
            var nap = document.napis.text.value;
            document.napis.text.value = nap.substring(znak_p) +
                nap.substring(0, znak_p);
        }
        przewin()
    </script>
</body>
<!-- <script src="https://code.jquery.com/jquery-3.6.0.js"
    integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script> -->

</html>


//////////////////////////////// Slider 

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/remixicon@2.5.0/fonts/remixicon.css" rel="stylesheet">
    <title>Document</title>
    <style>
        *,
        *::before,
        *::after {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            transition: .2s linear;
        }

        body {
            background-color: black;
        }

        .slider__outer {
            position: relative;
            width: 900px;
            height: 600px;
            margin: 50px auto;
        }

        .slider__inner {
            position: relative;
            width: 900px;
            height: 600px;
        }

        .slider__inner>div {
            position: absolute;
            transition: none !important;
        }

        .slider__inner>div>img {
            width: 900px;
            height: 600px;
        }

        .slider__arrows {
            position: absolute;
            font-size: 50px;
            width: 70px;
            height: 100%;
            top: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 100;
            cursor: pointer;
            color: rgb(255, 255, 255);
            opacity: 0;
        }

        .slider__outer:hover .slider__arrows {
            opacity: 0.5;
        }

        .prev__slider {
            left: 0;
        }

        .next__slider {
            right: 0;
        }
    </style>
</head>

<body>

    <div class="slider__outer">
        <div class="slider__arrows prev__slider">
            <i class="ri-arrow-left-line "></i>
        </div>

        <div class="slider__inner">
            <div>
                <img src="https://picsum.photos/900/600" alt="1">
            </div>
            <div>
                <img src="https://picsum.photos/900/600?grayscale" alt="2">
            </div>
            <div>
                <img src="https://picsum.photos/900/600?grayscale=2" alt="3">
            </div>
            <div>
                <img src="https://picsum.photos/900/600/?blur" alt="4">
            </div>
        </div>

        <div class="slider__arrows next__slider">
            <i class="ri-arrow-right-line"></i>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.6.0.js"
        integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.9.1/gsap.min.js"></script>
    <script>
        $(document).ready(function () {
            $(function () {
                async function StartSlider() {
                    $('.slider__inner > div:gt(0)').hide();
                    interfal = setInterval(function () {
                        $('.slider__inner > div:first')
                            .fadeOut(1000)
                            .next()
                            .fadeIn(1000)
                            .end()
                            .appendTo('.slider__inner');

                    }, 2000);
                }

                function StopSlider() {
                    clearInterval(interfal);
                }

                $(".prev__slider").on("click", function () {
                    setTimeout(function () {
                        $('.slider__inner > div:gt(0)').hide();
                        $('.slider__inner > div:first')
                            .fadeOut(800);

                        $('.slider__inner > div:last')
                            .fadeIn(800)
                            .prependTo('.slider__inner');
                    }, 200);
                });

                $(".next__slider").on("click", function () {
                    setTimeout(function () {
                        $('.slider__inner > div:gt(0)').hide();
                        $('.slider__inner > div:first')
                            .fadeOut(800)
                            .next()
                            .fadeIn(800)
                            .end()
                            .appendTo('.slider__inner');
                    }, 200);
                });

                $('.slider__outer').hover(StopSlider, StartSlider);
                StartSlider();
            });
        });
    </script>
</body>

</html>




Fajny PARAGRAF
    $('p').css({
        'position': 'absolute',
        'top': '50%',
        'left': '50%',
        'transform': 'translate(-50%, -50%)'
    });

