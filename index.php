https://phpkurs.pl/
https://www.w3schools.com/php/
https://www.php.net/manual/en/book.array.php

phpinfo() - informacjei o php



<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8" />
    <title>Skrypt PHP</title>
</head>

<body>
    <?php

    // $first = "PHP";
    // $second = "Lekcja 2";
    // echo $first . " " . $second ;
    // echo "<h3> $first $second </h3>";
    // print $first . " " . $second ;

    define("KURS", 4.5);

    $USD = 100;
    $PLN = round($USD * KURS, 2);

    echo "<br>";

    $PLN = 100;
    $USD = round($PLN / KURS, 2);


    echo "<ul> <li> $PLN PLN </li> <li> $USD USD</li></ul>";

    echo var_dump($PLN);


    ?>
</body>

</html>



<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <!-- php -->
    <?php

    // Zad1

    // $droga = 522;
    // $czas = 2;
    // $predkosc = $droga / $czas;

    // if ($predkosc < 21) {
    //     echo "ślimaki Cię wyprzedzają";
    // } elseif ($predkosc < 51) {
    //     echo "ciągnik mojego dziadka jest szybszy";
    // } elseif ($predkosc > 50) {
    //     echo "prawie ferrari";
    // } else {
    //     echo "możesz się zatrzymać na zielonym";
    // }

    // Zad2

    // $num = 2;
    // switch ($num) {
    //     case 1:
    //         echo "Poniedziałek";
    //         break;
    //     case 2:
    //         echo "Wtorek";
    //         break;
    //     case 3:
    //         echo "Środa";
    //         break;
    //     case 4:
    //         echo "Czwartek";
    //         break;
    //     case 5:
    //         echo "Piątek";
    //         break;
    //     case 6:
    //         echo "Sobota";
    //         break;
    //     case 7:
    //         echo "Niedziela";
    //         break;
    //     default:
    //         echo "Nie ma takiego dnia";
    //         break;
    // }

    // Zad3

    echo "<form action='index.php' method='post'>
        <input type='number' name='num'>
        <input type='submit' value='Sprawdź'>
        </form>";

    $num = $_POST['num'];

    if ($num % 2 == 0 && $num % 3 == 0 && $num % 5 == 0) {
        echo "Podzielna przez 2, 3 i 5";
    } elseif ($num % 2 == 0 && $num % 3 == 0) {
        echo "Podzielna przez 2 i 3";
    } elseif ($num % 2 == 0 && $num % 5 == 0) {
        echo "Podzielna przez 2 i 5";
    } elseif ($num % 3 == 0 && $num % 5 == 0) {
        echo "Podzielna przez 3 i 5";
    } elseif ($num % 2 == 0) {
        echo "Podzielna przez 2";
    } elseif ($num % 3 == 0) {
        echo "Podzielna przez 3";
    } elseif ($num % 5 == 0) {
        echo "Podzielna przez 5";
    } else {
        echo "Nie podzielna przez 2, 3 i 5";
    }
    ?>
</body>

</html>


<?php

    // zad1
    $imie1 = "Janusz";
    $imie2 = "Anna";

    echo "Imię: $imie1<br> Imię: $imie2<br>";
    if ($imie1 == $imie2) {
        echo "Imiona są takie same";
    } else {
        echo "Imiona są różne";
    }

    // zad2
    $zdanie = "Ala ma kota";
    echo substr($zdanie, 4, 2);

    // zad3
    $zdanie = "Ala ma kota - kot ma Ale";
    echo substr($zdanie, 0, strpos($zdanie, "-"));

    // zad4
    $zdanie = "Ala ma kota";
    if (strpos($zdanie, "a")) {
        echo "W zdaniu występuje litera a";
    }

    // zad5
    $email = "mateuszmroz001@gmail.com";
    if (strpos($email, "@") && strpos($email, ".")) {
        echo "Email poprawny";
    } else {
        echo "Email niepoprawny";
    }

    echo "<br>Login: " . substr($email, 0, strpos($email, "@"));
    echo "<br>Domena: " . substr($email, strpos($email, "@") + 1, strpos($email, ".") - strpos($email, "@") - 1);

    // zad6
    echo "godz: " . strftime("%H:%M") . " dzień: " . strftime("%Y-%m-%d");

    // zad7
    $data = mktime(0, 0, 0, 4, 30, 2024);
    $data2 = time();
    $roznica = $data - $data2;
    $dni = floor($roznica / 60 / 60 / 24);
    $miesiace = floor($dni / 30);
    $dni = $dni - $miesiace * 30;
    echo "Do 30 kwietnia 2024 r. pozostało $miesiace miesięcy i $dni dni";


    $date1 = new DateTime("2021-01-01");
    $date2 = new DateTime("2021-01-02");

    $diff = date_diff($date1, $date2);

    echo $diff->format("%a");
    





?>



<?php

    //Deklaracja funkcji
    function tekst()
    {
        echo 'Funkcja wypisuje tekst<br/>';
    }
    //Wywołanie funkcji
    tekst();
    tekst();

    // Funkcja z jednym parametrem
    function test($wyraz)
    {
        echo $wyraz . '<br/>';
    }
    test('PHP jest proste');
    test('bardzo proste');
    test('jest to prawda');

    // Funkcja z kilkoma parametrami
    function opis($nazwa, $kategoria, $cena)
    {
        echo $nazwa . ' ';
        echo $kategoria . ' ';
        echo $cena . ' ';
        echo '<br/>';
    }
    opis('chleb', 'pieczywo', 2);


    function dodawanie($a, $b)
    {
        $suma = $a + $b;
        echo $suma;
    }
    dodawanie(15, 47);


    // Funkcja zwracająca wartość
    function dodawanie($a, $b)
    {
        $suma = $a + $b;
        return $suma;
    }
    $wynik = dodawanie(4, 5);
    echo $wynik;


    function dodawanie($a, $b)
    {
        $suma = $a + $b;
        if ($suma > 1000) {
            return true;
        } else {
            return false;
        }
    }
    var_export(dodawanie(678, 487));

    // Funkcja z domyślnymi parametrami
    function opis($nazwa = 'chleb', $kategoria = 'pieczywo', $cena = 2)
    {
        echo $nazwa . ' ';
        echo $kategoria . ' ';
        echo $cena . ' ';
        echo '<br/>';
    }
    opis();


?>





<?php
    // zad1
    function cennik($nazwa = "Produk", $kategoria = "Kategoria", $cena = 100)
    {
        echo <<<T
        <table>
        <tr>
        <th>Nazwa</th>
        <th>Kategoria</th>
        <th>Cena</th>
        </tr>
        <tr>
        <td>$nazwa</td>
        <td>$kategoria</td>
        <td>$cena</td>
        </tr>
        </table>
        T;
    }

    cennik("Produkt1", "Książki", 100);
    cennik("Produk2", "Książki", 32);
    cennik("Produk3", "LOL", 12);

    // zad2
    function suma100($a, $b)
    {
        if ($a + $b >= 100) {
            echo "Suma = " . ($a + $b);
        } else {
            echo "Do 100 brakuje " . (100 - ($a + $b));
        }
    }

    suma100(50, 5);


    // zad3
    function iloraz($a, $b)
    {
        if ($b == 0) {
            echo "Nie dziel przez 0";
        } else {
            echo "Iloraz = " . ($a / $b);
        }
    }

    iloraz(10, 0);
    echo "<br>";
    iloraz(10, 2);

    // zad4
    function rabat($kwota, $procent)
    {
        echo "Kwota = " . $kwota . "<br>";
        echo "Procent = " . $procent . "%<br>" ;
        echo "Rabat = " . ($kwota * $procent / 100) . "<br>";
        echo "Kwota po rabacie = " . ($kwota - ($kwota * $procent / 100)) . "<br>";
    }

    rabat(100, 10);

    // zda 5
    function maxi(int $a, int $b, int $c)
    {
        if ($a > $b && $a > $c) {
            echo "Największa liczba to $a";
        } elseif ($b > $a && $b > $c) {
            echo "Największa liczba to $b";
        } else {
            echo "Największa liczba to $c";
        }
    }

    maxi(1, 2, 3);

    // zad 6
    function  format ($tekst)
    {
        echo <<<T
        <p style="color: red; font-weight: bold; font-style: italic;">$tekst</p>
        T;
    }

    format("Tekst jest czerwony, pogrubiony i pochylony");


?>



<!-- TABLICE -->

<?php


    // $cars = array("Volvo", "BMW", "Toyota");
    // echo "I like " . $cars[0] . ", " . $cars[1] . " and " . $cars[2] . ".";

    // $age = array("Peter" => "35", "Ben" => "37", "Joe" => "43");
    // echo "Peter is " . $age['Peter'] . " years old.";

    // $age = array("Peter" => "35", "Ben" => "37", "Joe" => "43");

    // foreach ($age as $x => $x_value) {
    //     echo "Key=" . $x . ", Value=" . $x_value;
    //     echo "<br>";
    // }

    // array_push($miasta, "Poznań", "Łódź"); // dodajemy 2 elementy na końcu tablicy
    // unset($miasta); // usunie całą tablicę
    // unset($miasta[0], $miasta[3]); // usuwa elementy z tablicy
    // implode(", ", $miasta); // łączy elementy tablicy w ciąg oddzielony przecinkiem i spacją
    // $tekst = "PHP programowanie aplikacji internetowych";
    // explode(" ", $tekst); // elementy z ciągu zapisuje do tablicy
    // array_search("Siedlce", $miasta); // wyszukujemy nr elementu w tablicy
    // in_array("Siedlce", $miasta); // czy istn. wyszukiwany element z tablicy zm. logiczna (prawda(1) albo fałsz(0))
    // asort($lista); // sortuje dane w tablicy rosnąco
    // arsort($lista); // sortuje dane malejąca
    // count($lista); // zlicza elementy w tablicy
    // max($lista); // max z tablicy
    // min($lista); // min z tablicy

    // zad1
    $miasta = array("Poznań", "Warszawa", "Kraków", "Gdańsk", "Siedlce");
    for ($i = 0; $i < count($miasta); $i++) {
        echo $miasta[$i] . "<br>";
    }

    $liczby = array(1, 2, 3, 4, 5);
    foreach ($liczby as $x => $x_value) {
        echo $x_value;
        echo "<br>";
    }

    // zad2
    array_push($miasta, "Poznań", "Łódź");
    unset($miasta[3]);

    foreach ($miasta as $x => $x_value) {
        echo $x_value;
        echo "<br>";
    }

    // zad3
    $miasta = array("Poznań", "Warszawa", "Kraków", "Gdańsk", "Siedlce");
    $liczby = array(1, 2, 3, 4, 5);

    //  nie działa na polskich znakach
    asort($miasta);
    arsort($liczby);

    foreach ($miasta as $x => $x_value) {
        echo $x_value;
        echo "<br>";
    }

    foreach ($liczby as $x => $x_value) {
        echo $x_value;
        echo "<br>";
    }


    // zad4
    echo max($miasta);
    echo "<br>";
    echo min($miasta);
    echo "<br>";
    echo max($liczby);
    echo "<br>";
    echo min($liczby);
    echo "<br>";

    // zad5
    echo count($miasta);
    echo "<br>";
    echo count($liczby);


    // zad6
    $zdaanie = "Uczę się programowania w PHP";
    $tablica = explode(" ", $zdaanie);
    foreach ($tablica as $x => $x_value) {
        echo $x_value;
        echo "<br>";
    }

    echo "<br>";
    echo $tablica[3];

    // zad7
    for ($i = 0; $i < count($tablica); $i++) {
        echo $tablica[$i] . " " .  $i . "<br>";
    }


    // zad7
    $zdaanie = "Uczę się programowania w PHP";
    $tablica = explode(" ", $zdaanie);
    if (in_array("programowanie", $tablica)) {
        echo "Znaleziono";
    } else {
        echo "Nie znaleziono";
    }



    // zad8
    function doArray($a, $b)
    {
        $sum = 0;
        $tablica = array();
        for ($i = $a; $i <= $b; $i++) {
            $tablica[] = $i;
            $sum += $i;
        }
        echo "Suma: " . $sum . "<br>";
        echo "Średnia: " . $sum / $a . "<br>";
        echo "Max: " . max($tablica) . "<br>";
        echo "Min: " . min($tablica) . "<br>";
        echo "Ilość elementów: " . count($tablica) . "<br>";
    }

    doArray(5, 10);

    // zad9

    function doRondomArray($a, $b, $rangeA, $rangeB)
    {
        $tablica = array();
        for ($i = $a; $i <= $b; $i++) {
            $tablica[] = rand($rangeA, $rangeB);
        }

        // sortwanie bombelkowe
        for ($i = 0; $i < count($tablica); $i++) {
            for ($j = 0; $j < count($tablica) - 1; $j++) {
                if ($tablica[$j] > $tablica[$j + 1]) {
                    $temp = $tablica[$j];
                    $tablica[$j] = $tablica[$j + 1];
                    $tablica[$j + 1] = $temp;
                }
            }
        }

        foreach ($tablica as $x => $x_value) {
            echo $x_value;
            echo "<br>";
        }
    }

    doRondomArray(5, 10, 1, 10);



?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <!-- php -->
    <?php
    $miasta = array('Siedlce', 'Warszawa', 'Bydgoszcz', 'Lublin');
    $owoce = array('d' => 'mango', 'a' => 'papaja', 'b' => 'banan', 'c' => 'aronia');
    sort($miasta);
    asort($owoce);
    foreach ($miasta as $miasto) {
        echo $miasto . ' ';
    }
    echo '<br/>';
    echo $miasta[1] . '<br/>';
    foreach ($owoce as $owoc) {
        echo $owoc . ' ';
    }
    echo '<br/>';
    echo $owoce['a'] . '<br/>';

    // zad1
    // wartość
    echo '<br/>';
    rsort($miasta);
    arsort($owoce);
    foreach ($miasta as $miasto) {
        echo $miasto . ' ';
    }
    echo '<br/>';
    // wyświetl klucz i wartość
    foreach ($owoce as $klucz => $owoc) {
        echo $klucz . ' ' . $owoc . ' ';
    }
    // zad2
    // klucze
    echo '<br/>';
    ksort($owoce);
    foreach ($owoce as $klucz => $owoc) {
        echo $klucz . ' ' . $owoc . ' ';
    }

    // zad3
    // Usuń po jednym elemencie z każdej  tablicy i posortuj  malejąco. Użyj funkcji unset() do usunięcia elementu.

    echo '<br/>';
    unset($miasta[0]);
    unset($owoce['a']);
    rsort($miasta);
    arsort($owoce);
    foreach ($miasta as $miasto) {
        echo $miasto . ' ';
    }

    echo '<br/>';
    foreach ($owoce as $klucz => $owoc) {
        echo $klucz . ' ' . $owoc . ' ';
    }

    // zad4
    // Dopisz po 2 elementy do każdej z tablic (po jednym na początku i po jednym na końcu) i ponownie posortuj tablice rosnąco.

    echo '<br/>';
    array_unshift($miasta, 'Poznań', 'Gdańsk');
    array_push($miasta, 'Wrocław', 'Kraków');
    asort($miasta);
    foreach ($miasta as $miasto) {
        echo $miasto . ' ';
    }

    echo '<br/>';
    $owoce['e'] = 'jabłko';
    $owoce['f'] = 'gruszka';
    // ksort($owoce);
    foreach ($owoce as $klucz => $owoc) {
        echo $klucz . ' ' . $owoc . ' ';
    }

    // zad5




    ?>
</body>

</html>



<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8" />
    <title>Skrypt PHP</title>
</head>

<body>
    <?php

    // podwujana tablica asocjacyjna
    $tab = array(
        array(
            "imie" => "Jan",
            "nazwisko" => "Kowalski",
            "wiek" => 20,
            "adres" => array(
                "ulica" => "Kwiatowa",
                "nr_domu" => 10,
                "nr_mieszkania" => 2
            )
        ),

        array(
            "imie" => "Anna",
            "nazwisko" => "Nowak",
            "wiek" => 25,
            "adres" => array(
                "ulica" => "Słoneczna",
                "nr_domu" => 20,
                "nr_mieszkania" => 3
            )
        )
    );

    // wyświetlenie tablicy i minimalny wiek
    echo "<pre>";
    print_r($tab);

    // minimalny wiek z funkcją min() i imie i nazwisko z funkcją array_column()
    echo "Minimalny wiek: " . min(array_column($tab, "wiek")) . "<br>";
    // wyświetl imie z najmniejszym wiekiem
    echo "Imie z najmniejszym wiekiem: " . $tab[array_search(min(array_column($tab, "wiek")), array_column($tab, "wiek"))]["imie"] . "<br>";
    // wyjaśnij powyższy kod
    // 1. array_search() - wyszukuje w tablicy wartość i zwraca jej klucz
    // 2. array_column() - zwraca tablicę zawierającą wartości z kolumny tablicy asocjacyjnej
    // 3. min() - zwraca najmniejszą wartość z tablicy
    // 4. $tab - tablica asocjacyjna
    // 5. array_search(min(array_column($tab, "wiek")), array_column($tab, "wiek")) - wyszukuje w tablicy wartość i zwraca jej klucz
    // 6. $tab[array_search(min(array_column($tab, "wiek")), array_column($tab, "wiek"))] - zwraca tablicę zawierającą wartości z kolumny tablicy asocjacyjnej
    // 7. $tab[array_search(min(array_column($tab, "wiek")), array_column($tab, "wiek"))]["imie"] - zwraca imie z najmniejszym wiekiem

    ?>
</body>

</html>


<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
  Name: <input type="text" name="fname">
  <input type="submit">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // collect value of input field
    $name = htmlspecialchars($_REQUEST['fname']);
    if (empty($name)) {
        echo "Name is empty";
    } else {
        echo $name;
    }
}
?>




<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8" />
    <title>Skrypt PHP</title>
</head>

<body>

    <!-- FORMULARZ ZGŁOSZENIOWY Z WALIDACJĄ KARZDEGO POLA -->
    <form action="index.php" method="post">
        <label for="name">Imię:</label>
        <input type="text" name="name" id="name" />
        <br />
        <label for="surname">Nazwisko:</label>
        <input type="text" name="surname" id="surname" />
        <br />
        <label for="email">E-mail:</label>
        <input type="text" name="email" id="email" />
        <br />
        <label for="phone">Telefon:</label>
        <input type="text" name="phone" id="phone" />
        <br />
        <label for="message">Wiadomość:</label>
        <textarea name="message" id="message" cols="30" rows="10"></textarea>
        <br />
        <input type="submit" value="Wyślij" />
    </form>

    <?php

    // Sprawdzanie POPRAWNOŚCI WPROWADZONYCH DANYCH
    if (isset($_POST['name']) && isset($_POST['surname']) && isset($_POST['email']) && isset($_POST['phone']) && isset($_POST['message'])) {
        $name = $_POST['name'];
        $surname = $_POST['surname'];
        $email = $_POST['email'];
        $phone = $_POST['phone'];
        $message = $_POST['message'];

        // Sprawdzanie poprawności imienia
        if (strlen($name) < 3) {
            echo "Imię jest za krótkie";
        } else if (strlen($name) > 20) {
            echo "Imię jest za długie";
        } else if (ctype_alpha($name) == false) {
            echo "Imię może składać się tylko z liter";
        } else {
            echo "Imię: " . $name . "<br />";
        }

        // Sprawdzanie poprawności nazwiska
        if (strlen($surname) < 3) {
            echo "Nazwisko jest za krótkie";
        } else if (strlen($surname) > 20) {
            echo "Nazwisko jest za długie";
        } else if (ctype_alpha($surname) == false) {
            echo "Nazwisko może składać się tylko z liter";
        } else {
            echo "Nazwisko: " . $surname . "<br />";
        }

        // Sprawdzanie poprawności adresu e-mail
        $emailB = filter_var($email, FILTER_SANITIZE_EMAIL);
        if ((filter_var($emailB, FILTER_VALIDATE_EMAIL) == false) || ($emailB != $email)) {
            echo "Podaj poprawny adres e-mail";
        } else {
            echo "E-mail: " . $email . "<br />";
        }

        // Sprawdzanie poprawności numeru telefonu
        $phone = str_replace('-', '', $phone);
        $phone = str_replace(' ', '', $phone);
        $phone = str_replace('(', '', $phone);
        $phone = str_replace(')', '', $phone);
        if (strlen($phone) != 9) {
            echo "Podaj poprawny numer telefonu";
        } else if (ctype_digit($phone) == false) {
            echo "Numer telefonu może składać się tylko z cyfr";
        } else {
            echo "Telefon: " . $phone . "<br />";
        }

        // Sprawdzanie poprawności wiadomości
        if (strlen($message) < 20) {
            echo "Wiadomość jest za krótka";
        } else if (strlen($message) > 1000) {
            echo "Wiadomość jest za długa";
        } else {
            echo "Wiadomość: " . $message . "<br />";
        }
    }

    ?>
</body>

</html>



<!-- REFERENCJE I ZMIENNE GOLOBALNE I LOKALNE -->

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <!-- php -->
    <?php
    include 'function.php';


    $a = 2;
    $b = add($a);
    echo $a;
    echo $b;

    echo "<br>";
    function ojeden(&$x) // argument przekazany przez referencję
    {
        $x++;
    }
    $a = 10;
    ojeden($a);
    echo $a . '<br>';

    $a = 10;
    $b = &$a; // przypisanie przez referencję
    echo $a . '<br>';
    echo $b . '<br>';


    ?>




</body>

</html>


<!-- zmienne psełdo globalne  
http://www.capaciouscore.pl/kursy/kurs-php/superglobalne/


index.html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form action="index.php" method="post">

        <label for="A">Liczba A</label>
        <br>
        <input type="text" name="A" id="A">
        <br>
        <label for="B">Liczba B</label>
        <br>
        <input type="text" name="B" id="B">
        <br>
        <input type="submit" value="Wyślij">
    </form>
</body>

</html>

index.php
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    $C = $_POST["A"] + $_POST["B"];
    echo $C;
    ?>
</body>

</html>









    <?php

    function divide($a, $b)
    {
        try {
            if ($b == 0) {
                throw new Exception("Nie dziel przez zero");
            }
            return $a / $b;
        } catch (Exception $e) {
            echo "Błąd: " . $e->getMessage();
            echo "<br>";
            echo "Błąd: " . $e->getLine();
            echo "<br>";
            echo "Błąd: " . $e->getFile();
            echo "<br>";
            echo "Błąd: " . $e->getTraceAsString();
        }
    }

    echo divide(10, 0);
    echo "<br>";
    echo divide(10, 2);

    ?>




<body>
    <form action="index.php" method="post">
        <input type="text" name="tekst" id="">
        <input type="submit" value="Wyślij">
    </form>

    <?php

    function formatText($text)
    {

        try {
            if (!is_numeric($text)) {
                throw new Exception("Wpisz liczbę");
            }
        } catch (Exception $e) {
            echo "Błąd: " . $e->getMessage();
            echo "<br>";
            echo "Błąd: " . $e->getLine();
            echo "<br>";
            echo "Błąd: " . $e->getFile();
            echo "<br>";
            echo "Błąd: " . $e->getTraceAsString();
        }
    }

    formatText($_POST['tekst']);

    ?>
</body>


























<!-- PLIKI !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!-->
<!-- https://phpkurs.pl/operacje-na-plikach/#pliki.odczyt -->

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>


    <?php

    // ZADANIE 1
    if (!file_exists('czasami.txt')) {
        touch('czasami.txt');
        $file = fopen('czasami.txt', 'w');
        $date = date('Y-m-d');
        fwrite($file, $date);
        fclose($file);
    }


    // ZADANIE 2 dodanie pierwszej linii
    $fp = fopen('czasami.txt', 'r');
    $oldDate = fread($fp, filesize('czasami.txt'));
    $oldDate = $oldDate . PHP_EOL;
    fclose($fp);
    $hour = date('H:i') . PHP_EOL; // lub "\n"
    $fp = fopen('czasami.txt', 'w');
    fwrite($fp, $hour);
    fwrite($fp, $oldDate);
    fclose($fp);

    // ZADANIE 3
    // dopisz swoje imie i nawikso na kńcu pliku
    $fp = fopen('czasami.txt', 'a+');
    fwrite($fp, 'Mateusz Mróz');
    fclose($fp);

    // ZADANIE 4
    $fp = fopen('czasami.txt', 'r');
    foreach (file('czasami.txt') as $line) {
        echo $line . '<br>';
    }
    fclose($fp);


    // ZADANIE 5 Napisz skrypt, który wpisze do pliku liczby parzyste i podzielne przez 3 z przedziału od 1 do 1000, a następnie odczyta zawartość pliku i wyświetli go w oknie przeglądarki.
    $fp = fopen('liczby.txt', 'w+');
    for ($i = 1; $i <= 1000; $i++) {
        if ($i % 2 == 0 && $i % 3 == 0) {
            fwrite($fp, $i . PHP_EOL);
        }
    }

    foreach (file('liczby.txt') as $line) {
        echo $line . '<br>';
    }
    fclose($fp);


    // ZADANIE 6 Napisz skrypt odczytujący cztery liczby zapisane w pliku tekstowym (każda w osobnej linii) i wypisujący je w oknie przeglądarki w kolejności malejącej.
    $fp = fopen('liczby.txt', 'w+');
    $numbers = [5, 24, 4, 1];
    foreach ($numbers as $number) {
        fwrite($fp, $number . PHP_EOL);
    }

    $numbers = file('liczby.txt');
    rsort($numbers);

    foreach ($numbers as $number) {
        echo $number . '<br>';
    }

    fclose($fp);


    // ZADANIE 7 Napisz skrypt zapisujący do pliku 10 losowych liczb z przedziału od 0 do 100. Odczyt z pliku największą z wylosowanych liczb. 
    $fp = fopen('liczby.txt', 'w+');
    for ($i = 0; $i < 100; $i++) {
        fwrite($fp, rand(1, 100) . PHP_EOL);
    }

    $numbers = file('liczby.txt');
    max($numbers);
    echo max($numbers);


    // Tryb a - dopisuje do pliku
    // Tryb a+ - dopisuje do pliku i umożliwia odczyt
    // Tryb r - odczyt
    // Tryb r+ - odczyt i zapis na końcu pliku
    // Tryb w - zapis, jeśli plik istnieje to jego zawartość jest usuwana
    // Tryb w+ - zapis i odczyt, jeśli plik istnieje to jego zawartość jest usuwana

    // ZADANIE 8
    // OSTATNIA DATA MODYFIKACJI PLIKU czasami.txt
    $date = date('Y-m-d H:i:s', filemtime('czasami.txt'));
    echo $date;
    echo '<br>';

    $now = date('Y-m-d H:i:s');
    setcookie('lastVisit', $now, time() + 60 * 60 * 24 * 30);

    if (isset($_COOKIE['counter'])) {
        $counter = $_COOKIE['counter'] + 1;
        setcookie('counter', $counter, time() + 60 * 60 * 24 * 30);
    } else {
        $counter = 1;
        setcookie('counter', $counter, time() + 60 * 60 * 24 * 30);
    }
    echo $_COOKIE['lastVisit'];
    echo '<br>';
    echo $counter;

    // ZADANIE 9 Utwórz plik logi.txt, do którego wprowadzisz dane w jednej linii:
    // datę ostatniego odczyt pliku czasami.txt,
    // wielkość pliku czasami.txt,
    // datę ostatniej modyfikacji pliku czasami.txt,
    // a na końcu w nowej linii będzie licznik odwiedzin strony ze skryptem, który przy ponownym otwarciu jest aktualizowany.


    $fp = fopen('logi.txt', 'w+');
    $dateLastRead = date('Y-m-d H:i:s', fileatime('czasami.txt'));
    $size = filesize('czasami.txt');
    $dateLastModified = date('Y-m-d H:i:s', filemtime('czasami.txt'));
    if (isset($_COOKIE['counter'])) {
        $counter = $_COOKIE['counter'] + 1;
        setcookie('counter', $counter, time() + 60 * 60 * 24 * 30);
    } else {
        $counter = 1;
        setcookie('counter', $counter, time() + 60 * 60 * 24 * 30);
    }

    fwrite($fp, 'Data ostatniego odczytu: ' . $dateLastRead . PHP_EOL);
    fwrite($fp, 'Wielkość pliku: ' . $size . " B" . PHP_EOL);
    fwrite($fp, 'Data ostatniej modyfikacji: ' . $dateLastModified . PHP_EOL);
    fwrite($fp, 'Liczba odwiedzin: ' . $counter . PHP_EOL);

    // ZADANIE 10 Otwórz plik logi.txt z odpowiednią blokadą (wiele osób może odczytywać)

    $fp = fopen('logi.txt', 'r');
    flock($fp, LOCK_SH);
    foreach (file('logi.txt') as $line) {
        echo $line . '<br>';
    }
    flock($fp, LOCK_UN);
    fclose($fp);

    // WYJAŚNIENIE
    // LOCK_SH - Wspólne zamka (reader) . Pozwól innym procesy dostępu do pliku
    // LOCK_EX - Exclusive blokady (writer) . Zapobiec inne procesy z dostępem do pliku
    // LOCK_UN - Zwolnić wspólną lub wyłączną blokadę
    // LOCK_NB - Zapobiega blokowaniu inne procesy podczas blokowania

    





    ?>
</body>

</html>




<?php
session_start(); // musimy zacząć sesję
if (!isset($_SESSION['count'])) {
    $_SESSION['count'] = 0;
} else {
    $_SESSION['count']++;
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>


    <?php
    // ZADANIE 1

    $_SESSION['name'] = 'Jan';
    $_SESSION['surname'] = 'Kowalski';
    $_SESSION['age'] = 20;
    $_SESSION['time'] = time() + 30 * 60;

    if (isset($_SESSION['time'])) {
        if ($_SESSION['time'] < time()) {
            session_unset();
            session_destroy();
        }
    }

    echo $_SESSION['name'] . ' ' . $_SESSION['surname'] . ' ' . $_SESSION['age'];
    echo '<br>';
    echo date('Y-m-d H:i:s', $_SESSION['time']);

    // ZADANIE 2
    // Ustaw 3 własne ciasteczka do powyższej sesji. Usuń 1 z ciasteczek. Wyświetl wszystkie ciasteczka.

    setcookie('name', 'Jan', time() + 30 * 60);
    setcookie('surname', 'Kowalski', time() + 30 * 60);
    setcookie('age', 21, time() + 30 * 60);

    // setcookie('name', 'Jan', time() - 30 * 60);

    echo '<br>';
    if (isset($_COOKIE['name']) && isset($_COOKIE['surname']) && isset($_COOKIE['age'])) {
        echo $_COOKIE['name'] . ' ' . $_COOKIE['surname'] . ' ' . $_COOKIE['age'];
    }





    // session_unset();

    // session_start(); - rozpoczyna sesję na początku pliku
    // session_unset(); - usuwa wszystkie zmienne sesji
    // session_destroy(); - usuwa sesję
    // $_SESSION["favcolor"] = "yellow"; - tworzy zmienną sesji
    // print_r($_SESSION); - wyświetla wszystkie zmienne sesji




    // unset($_SESSION['count']); // usuwa zmienną sesji
    ?>
</body>

</html>
