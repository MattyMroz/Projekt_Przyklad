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




Przykład  Serializacja i deserializacja tablicy

<?php
// zapis
$tablica = Array('a' => 'pierwszy', 'b' => 'drugi');
setcookie('tablica', serialize($tablica), time()+3600);

// odczyt zabezpieczony przed nieistniej±cym ciasteczkiem
if (isset($_COOKIE['tablica'])) {
    $tablica = unserialize($_COOKIE['tablica']);
} else {
    $tablica = Array();
}

?>






<?php
session_start();
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

    <!-- pobieranie plików z formularza -->
    <form action="upload.php" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <br>
        <!-- <label for="name">Nazwa pliku:</label>
        <br>
        <input type="text" name="name">
        <br> -->
        <br>
        <button type="submit" name="submit">UPLOAD</button>
    </form>


    <?php
    // echo "<script>alert(\"Witaj!\");</script>";



    if (isset($_POST["submit"])) {
        $file = $_FILES["file"];
        // print_r($file);
        $fileName = $_FILES["file"]["name"];
        $fileTmpName = $_FILES["file"]["tmp_name"];
        $fileSize = $_FILES["file"]["size"];
        $fileError = $_FILES["file"]["error"];
        $fileType = $_FILES["file"]["type"];

        // rozczłonkowanie nazwy pliku
        $fileExt = explode(".", $fileName);
        // pobranie ostatniego elementu z rozczłonkowanej nazwy pliku
        $fileActualExt = strtolower(end($fileExt));

        // tablica z rozszerzeniami plików
        $allowed = array("jpg", "jpeg", "png", "pdf");

        // sprawdzenie czy rozszerzenie pliku jest dozwolone
        if (in_array($fileActualExt, $allowed)) {
            // sprawdzenie czy nie ma błędów
            if ($fileError === 0) {
                // sprawdzenie czy rozmiar pliku nie przekracza 100MB - tak o *_*
                // 100 MB = 100000000
                if ($fileSize < 100000000) {
                    // ustawienie nazwy pliku
                    // $fileNameNew = uniqid("", true) . "." . $fileActualExt;
                    // uniqid() - generuje unikalny ciąg znaków (np. 60b9f2c5c5a7e)

                    // zapisz plik z taką samą nazwą

                    // if (isset($_POST["name"]) && $_POST["name"] != "") {
                    //     $fileNameNew = $_POST["name"] . "." . $fileActualExt;
                    // } else {
                    $fileNameNew = $fileName;
                    // }


                    // sprawdzenie czy plik o takiej nazwie już istnieje

                    for ($i = 0; $i < count($allowed); $i++) {
                        // folder obrazy lub dokumenty
                        if ($fileActualExt == $allowed[$i]) {
                            if ($i < 3) {
                                // jeśli plik istnieje to zakoncz działanie skryptu
                                // if (file_exists("obrazy/" . $fileNameNew)) {
                                //     echo "<script>alert(\"Plik o takiej nazwie już istnieje!\");</script>";
                                //     exit();
                                // }
                                $fileDestination = "obrazy/" . $fileNameNew;
                                // setcookie("file", $fileDestination, time() + 3600);
                            } else {
                                $fileDestination = "dokumenty/" . $fileNameNew;
                                // setcookie("file", $fileDestination, time() + 3600);
                            }
                        }
                    }

                    // jeśli plik o takiej nazwie już istnieje to zmień nazwę

                    // alert(), confirm() i prompt().
                    // echo "<script>prompt(\"Plik o takiej nazwie już istnieje. Podaj nową nazwę pliku lub nie wpisuj nic, aby nadpisać plik.\");</script>";
                    //  zapisz zmienną z prompt() do ciasteczka
                    // echo "<script>document.cookie = \"fileNameNew = \" + prompt(\"Plik o takiej nazwie już istnieje. Podaj nową nazwę pliku lub nie wpisuj nic, aby nadpisać plik.\");</script>";
                    // // odśwież ciasteczko
                    // $fileNameNew = $_COOKIE["fileNameNew"];


                    // przeniesienie pliku do folderu
                    move_uploaded_file($fileTmpName, $fileDestination);
                    $date = date("Y-m-d H:i:s", filemtime($fileDestination));
                    setcookie("time", $date, time() + 3600);
                    // header("Location: upload.php?uploadsuccess");
                } else {
                    echo "<script>alert(\"Plik jest za duży!\");</script>";
                }
            } else {
                echo "<script>alert(\"Wystąpił błąd podczas przesyłania pliku!\");</script>";
            }
        } else {
            echo "<script>alert(\"Nie można przesłać pliku o takim rozszerzeniu!\");</script>";
        }
        // odśwież stronę
        header("Refresh:0");
    }

    // wyświetl ciastko
    if (isset($_COOKIE["time"])) {
        echo "Ostatnio przesłano plik: " . $_COOKIE["time"];
    }

    // echo "Liczba sesji: " . $_SESSION["count"];
    session_write_close();
    ?>
</body>

</html>

<?php
$polaczenie = mysqli_connect("localhost", "test", "test")
    or die("Brak połączenia z serwerem MySQL");
mysqli_select_db($polaczenie, "baza_filmow")
    or die("Błąd wyboru bazy danych");
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- bootstrap -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">


    <style>
        body {
            margin: 50px;
        }
    </style>
</head>

<body>
    <div class="container justify-content-center">
        <h1 class="display-4 text-center">Debate On Euthanasia</h1>
        <div class="row">
            <table class="table ">
                <tbody class="test">
                    <?php
                    $zapytanie = "SELECT * FROM filmy";
                    $wynik = mysqli_query($polaczenie, $zapytanie)
                        or die("Wystąpiły problemy przy zapisywaniu danych");
                    while ($wiersz_danych = mysqli_fetch_row($wynik)) {
                        for ($i = 0; $i < count($wiersz_danych); $i++) {
                            echo "<td>$wiersz_danych[$i]</td>";
                        }
                        echo "</tr>";
                    }
                    ?>
                </tbody>
            </table>


        </div>
        <div class="row">
            <div class="col">
                <?php
                $zapytanie = "SELECT rezyser FROM filmy";
                $wynik = mysqli_query($polaczenie, $zapytanie)
                    or die("Wystąpiły problemy przy zapisywaniu danych");
                while ($wiersz_danych = mysqli_fetch_row($wynik)) {
                    for ($i = 0; $i < count($wiersz_danych); $i++) {
                        echo "<li>$wiersz_danych[$i]</li>";
                    }
                }
                ?>
            </div>
            <div class="col">
                <?php
                $zapytanie = "SELECT tytul FROM filmy";
                $wynik = mysqli_query($polaczenie, $zapytanie)
                    or die("Wystąpiły problemy przy zapisywaniu danych");
                echo "<ol>";
                while ($wiersz_danych = mysqli_fetch_row($wynik)) {
                    for ($i = 0; $i < count($wiersz_danych); $i++) {
                        echo "<li>$wiersz_danych[$i]</li>";
                    }
                }
                echo "</ol>";
                mysqli_close($polaczenie);
                ?>
            </div>
        </div>
    </div>



</body>

</html>

<?php
// $polaczenie = mysqli_connect("localhost", "test", "test")
//     or die("Brak połączenia z serwerem MySQL");
// mysqli_select_db($polaczenie, "baza_filmow")
//     or die("Błąd wyboru bazy danych");


// $polaczenie = mysqli_connect("localhost", "test", "test", "baza_filmow");
// if (!$polaczenie) {
//     die("Connection failed: " . mysqli_connect_error());
// }



?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- bootstrap -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

</head>

<body>
    <div class="container justify-content-center">
        <h1 class="display-4 text-center">Debata na temat eutanazji</h1>
        <div class="row">
            <table class="table ">
                <tbody class="test">
                    <?php
                    // $zapytanie = "SELECT * FROM filmy";
                    // $wynik = mysqli_query($polaczenie, $zapytanie)
                    //     or die("Wystąpiły problemy przy zapisywaniu danych");
                    // while ($wiersz_danych = mysqli_fetch_row($wynik)) {
                    //     for ($i = 0; $i < count($wiersz_danych); $i++) {
                    //         echo "<td>$wiersz_danych[$i]</td>";
                    //     }
                    //     // dodaj przycisk usuwający rekord
                    //     echo "<td><button class='btn btn-danger'>Usuń</button></td>";
                    //     echo "</tr>";
                    // }

                    $mysqli = new mysqli("localhost", "test", "test", "baza_filmow");
                    $result = $mysqli->query("SELECT * FROM filmy");
                    while ($row = $result->fetch_row()) {
                        echo "<tr>";
                        for ($i = 0; $i < count($row); $i++) {
                            echo "<td>$row[$i]</td>";
                        }
                        echo "<form action='' method='post'>";
                        echo "<td><button class='btn btn-danger' name='usun' value='$row[0]'>Usuń</button></td>";
                        echo "<td><button class='btn btn-warning' name='edytuj' value=''>Edytuj</button></td>";
                        echo "</form>";
                        echo "</tr>";


                        // INSERT INTO filmy VALUES (NULL, "Pan Tadeusz", "A.Wajda", 207);
                        // INSERT INTO filmy VALUES (NULL, "Matrix", "A.Wachowski", 196);
                        // INSERT INTO filmy VALUES (NULL, "Shrek", "A.Adamson", 150);



                    }
                    echo '</table>';

                    echo "<form action='' method='post'>";
                    echo "<input type='text' name='tytul' placeholder='Tytuł'>";
                    echo "<input type='text' name='rezyser' placeholder='Reżyser'>";
                    echo "<input type='text' name='dlugosc' placeholder='Długość'>";
                    echo "<button class='btn btn-success' name='dodaj' value=''>Dodaj</button>";
                    echo "</form>";


                    if (isset($_POST['usun'])) {
                        $id = $_POST['usun'];
                        $mysqli->query("DELETE FROM filmy WHERE id=$id");
                        header("Location: index.php");
                    }

                    if (isset($_POST['dodaj'])) {
                        $tytul = $_POST['tytul'];
                        $rezyser = $_POST['rezyser'];
                        $dlugosc = $_POST['dlugosc'];
                        $mysqli->query("INSERT INTO filmy VALUES (NULL, '$tytul', '$rezyser', $dlugosc)");
                        header("Location: index.php");
                    }

                    if (isset($_POST['edytuj'])) {
                        $id = $_POST['edytuj'];
                        echo "<form action='' method='post'>";
                        echo "<input type='text' name='tytul2' placeholder='Tytuł'>";
                        echo "<input type='text' name='rezyser2' placeholder='Reżyser'>";
                        echo "<input type='text' name='dlugosc2' placeholder='Długość'>";
                        echo "<button class='btn btn-success' name='dodaj2' value=''>Dodaj</button>";
                        echo "</form>";

                        if (isset($_POST['dodaj2'])) {
                            $tytul = $_POST['tytul2'];
                            $rezyser = $_POST['rezyser2'];
                            $dlugosc = $_POST['dlugosc2'];
                            $mysqli->query("UPDATE filmy SET tytul='$tytul', rezyser='$rezyser', dlugosc=$dlugosc WHERE id=$id");
                            header("Location: index.php");
                        }
                    }




                    ?>
                </tbody>
            </table>


        </div>

    </div>



</body>

</html>




<!-- TABLICE I SORTOWANIA -->
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
    function randomArray($n)
    {
        $arr = [];
        if ($n > 100) {
            echo "Podaj liczbę mniejszą od 100";
            array_push($arr, "Podaj liczbę mniejszą od 100");
        } else {
            for ($i = 0; $i < $n; $i++) {
                $arr[$i] = rand(1, 100);

                for ($j = 0; $j < $i; $j++) {
                    if ($arr[$i] == $arr[$j]) {
                        $i--;
                        break;
                    }
                }
                // co robi powyższy for
                // dla każdego elementu tablicy sprawdza czy jest taki sam jak poprzedni
                // jeśli tak to cofa się o jeden element i generuje nową liczbę
            }
        }

        return $arr;
    }

    $arr = randomArray(100);
    echo "ZADANIE 1 - Funkcja jako parametry ma przyjmować rozmiar tablicy i zwracać tablicę liczb wygenerowanych losowo z przedziału od 1 do 100. Liczby nie mogą się powtarzać.<br>";
    echo "<pre>";
    print_r($arr);
    echo "</pre>";


    // ZADANIE 2
    function minArray($arr)
    {
        $min = $arr[0];
        foreach ($arr as $value) {
            if ($value < $min) {
                $min = $value;
            }
        }

        // for ($i = 0; $i < count($arr); $i++) {
        //     if ($arr[$i] == $min) {
        //         $arr[$i] = 0;
        //     }
        // }
        return $min;
    }

    echo "<br>ZADANIE 2 - Funkcja jako parametr przyjmuje tablicę liczb i zwraca element minimalny.<br>";
    echo minArray($arr);


    // ZADANIE 3
    function maxArray($arr)
    {
        $max = $arr[0];
        foreach ($arr as $value) {
            if ($value > $max) {
                $max = $value;
            }
        }

        // for ($i = 0; $i < count($arr); $i++) {
        //     if ($arr[$i] == $max) {
        //         $arr[$i] = 0;
        //     }
        // }

        return $max;
    }
    echo "<br><br>ZADANIE 3 - Funkcja jako parametr przyjmuje tablicę liczb i zwraca element maksymalny.<br>";
    echo maxArray($arr);


    // ZADANIE 4
    function average($arr)
    {
        $sum = 0;
        foreach ($arr as $value) {
            $sum += $value;
        }

        // for ($i = 0; $i < count($arr); $i++) {
        //     $sum += $arr[$i];
        // }

        return $sum / count($arr);
    }

    echo "<br><br>ZADANIE 4 - Funkcja jako parametr przyjmuje tablicę liczb i zwraca średnią wszystkich elementów.<br>";
    echo average($arr);


    // ZADANIE 5
    function sortWithValue($arr, $value)
    {
        for ($i = 0; $i < count($arr); $i++) {
            for ($j = 0; $j < count($arr) - 1; $j++) {
                if ($arr[$j] > $arr[$j + 1]) {
                    $temp = $arr[$j];
                    $arr[$j] = $arr[$j + 1];
                    $arr[$j + 1] = $temp;
                }
            }
        }
        if ($value == "asc") {
            return $arr;
        } else if ($value == "desc") {
            for ($i = 0; $i < count($arr) / 2; $i++) {
                $temp = $arr[$i];
                $arr[$i] = $arr[count($arr) - 1 - $i];
                $arr[count($arr) - 1 - $i] = $temp;
            }
            return $arr;
        }
    }
    echo "<br><br>ZADANIE 5 - Funkcja jako parametry przyjmuje tablicę liczb oraz sposób sortowania i zwraca tą samą tablicę, ale z elementami posortowanymi w zależności od wartości parametru.";
    echo "<br>ZADANIE 5.1<br>";
    echo "<pre>";
    print_r(sortWithValue($arr, "asc"));
    echo "</pre>";

    echo "<br>ZADANIE 5.2<br>";
    echo "<pre>";
    print_r(sortWithValue($arr, "desc"));
    echo "</pre>";


    // ZADANIE 6
    function twoToOne($arr1, $arr2)
    {
        $arr = [];
        for ($i = 0; $i < count($arr1); $i++) {
            $arr[$i] = $arr1[$i];
        }
        // jeśli się powtarzają to nie dodaje
        for ($i = 0; $i < count($arr2); $i++) {
            for ($j = 0; $j < count($arr1); $j++) {
                if ($arr2[$i] == $arr1[$j]) {
                    break;
                }
                if ($j == count($arr1) - 1) {
                    array_push($arr, $arr2[$i]);
                }
            }
        }
        return $arr;
    }


    $arr1 = randomArray(10);
    $arr2 = randomArray(10);

    echo "<br>ZADANIE 6 - Funkcja jako parametry przyjmuje dwie tablice i zwraca tablicę powstałą przez połączenie tych dwóch tablic. Należy pamiętać że elementy w tablicy wynikowej nie mogą się powtarzać.<br>";
    echo "<pre>";
    print_r(twoToOne($arr1, $arr2));
    echo "</pre>";


    // ZADANIE 7
    function intersectionArray($arr1, $arr2)
    {
        $arr = [];
        for ($i = 0; $i < count($arr1); $i++) {
            for ($j = 0; $j < count($arr2); $j++) {
                if ($arr1[$i] == $arr2[$j]) {
                    array_push($arr, $arr1[$i]);
                }
            }
        }
        return $arr;
    }

    echo "<br>ZADANIE 7 - Funkcja jako parametry przyjmuje dwie tablice i jako wynik zwraca tablicę, w której zawarta jest część wspólna obu tablic (elementy, które znajdują się w obu tablicach).<br>";
    echo "<pre>";
    print_r(intersectionArray($arr1, $arr2));
    echo "</pre>";
    ?>
</body>

</html>






<!-- Klasy -->




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
    class Osoba
    {
        public $imie;
        public $nazwisko;
        public $rok_urodzenia;

        public function __construct($imie, $nazwisko, $rok_urodzenia)
        {
            $this->imie = $imie;
            $this->nazwisko = $nazwisko;
            $this->rok_urodzenia = $rok_urodzenia;
        }

        public function wiek()
        {
            return date('Y') - $this->rok_urodzenia;
        }

        public function __toString()
        {
            return $this->imie . ' ' . $this->nazwisko . ' ' . $this->rok_urodzenia;
        }

        // czjest pełnoletnia
        public function pelnoletnia()
        {
            return $this->wiek() >= 18;
        }

        // destruktor
        public function __destruct()
        {
            echo 'Obiekt został usunięty';
        }
    }

    // czy osoba jest pełnolentia
    $osoba = new Osoba('Jan', 'Kowalski', 1990);
    echo $osoba->pelnoletnia() ? 'Osoba jest pełnoletnia' : 'Osoba nie jest pełnoletnia';

    echo '<br>';
    echo '<pre>';
    print_r($osoba);
    echo '</pre>';

    echo $osoba->__toString();
    echo '<br>';
    echo $osoba->wiek();

    // podlksa dziecko
    class Dziecko extends Osoba
    {
        public $opiekun;

        public function __construct($imie, $nazwisko, $rok_urodzenia, $opiekun)
        {
            parent::__construct($imie, $nazwisko, $rok_urodzenia);
            $this->opiekun = $opiekun;
        }

        public function __toString()
        {
            return parent::__toString() . ' ' . $this->opiekun;
        }
    }

    $dziecko = new Dziecko('Jan', 'Kowalski', 2000, 'Janina Kowalska');
    echo '<br>';
    echo '<pre>';
    print_r($dziecko);
    echo '</pre>';

    echo $dziecko->__toString();
    echo '<br>';
    echo $dziecko->wiek();
    echo '<br>';
    echo $dziecko->pelnoletnia() ? 'Osoba jest pełnoletnia' : 'Osoba nie jest pełnoletnia';
    echo '<br>';
    echo $dziecko->opiekun;

    // jeśli jest pełnoletnia to usuń opiekuna
    // if ($dziecko->pelnoletnia()) {
    //     unset($dziecko->opiekun);
    // }

    echo '<br>';
    echo '<pre>';
    print_r($dziecko);
    echo '</pre>';




    ?>




</body>

</html>













<!-- ZADANIE -->
<!-- https://mansfeld.pl/programowanie/kurs-pdo-bazy-danych-php/ -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- bootstrap -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

</head>

<body>
    <?php
    // CREATE DATABASE firma;
    // use firma;

    // CREATE TABLE `customer` (
    //   `customer_id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    //   `title` char(4) DEFAULT NULL,
    //   `fname` varchar(32) DEFAULT NULL,
    //   `lname` varchar(32) NOT NULL,
    //   `addressline` varchar(64) DEFAULT NULL,
    //   `town` varchar(32) DEFAULT NULL,
    //   `zipcode` char(10) NOT NULL,
    //   `phone` varchar(16) DEFAULT NULL
    //   ) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

    //   INSERT INTO `customer` (`customer_id`,`title`,`fname`,`lname`,`addressline`,`town`,`zipcode`,`phone`) VALUES
    //  (1,'Miss','Jenny','Stones','27 Rowan Avenue','Hightown','NT2 1AQ','023 9876'),
    //  (2,'Mr','Andrew','Stones','52 The Willows','Lowtown','LT5 7RA','876 3527'),
    //  (3,'Miss','Alex','Matthew','4 The Street','Nicetown','NT2 2TX','010 4567'),
    //  (4,'Mr','Adrian','Matthew','The Barn','Yuleville','YV67 2WR','487 3871'),
    //  (5,'Mr','Simon','Cozens','7 Shady Lane','Oahenham','OA3 6QW','514 5926'),
    //  (6,'Mr','Neil','Matthew','5 Pasture Lane','Nicetown','NT3 7RT','267 1232'),
    //  (7,'Mr','Richard','Stones','34 Holly Way','Bingham','BG4 2WE','342 5982'),
    //  (8,'Mrs','Anna','Stones','34 Holly Way','Bingham','BG4 2WE','342 5982'),
    //  (9,'Mrs','Christine','Hickman','36 Queen Street','Histon','HT3 5EM','342 5432'),
    //  (10,'Mr','Mike','Howard','86 Dysart Street','Tibsville','TB3 7FG','505 5482'),
    //  (11,'Mr','Dave','Jones','54 Vale Rise','Bingham','BG3 8GD','342 8264'),
    //  (12,'Mr','Richard','Neill','42 Thached way','Winersby','WB3 6GQ','505 6482'),
    //  (13,'Mrs','Laura','Hendy','73 Margeritta Way','Oxbridge','OX2 3HX','821 2335'),
    //  (14,'Mr','Bill','Neill','2 Beamer Street','Welltown','WT3 8GM','435 1234'),
    //  (15,'Mr','David','Hudson','4  The Square','Milltown','MT2 6RT','961 4526');


    try {
        $dbhost = "localhost";
        $dbname = "firma";
        $dbuser = "root";
        $dbpassword = "";
        $db_conn = new PDO("mysql:host=" . $dbhost . ";dbname=" . $dbname, $dbuser, $dbpassword);
    } catch (PDOException $e) {
        echo "Connection failed: " . $e->getMessage();
    }


    $sql = "SELECT * FROM customer";
    $stmt = $db_conn->prepare($sql);
    $stmt->execute();
    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);


    ?>

    <!-- tabela bootstrap -->
    <div class="container">
        <div class="row">
            <div class="col-12">
                <table class="table table-striped table-hover">
                    <thead class="thead-dark">
                        <tr>
                            <th>Customer ID</th>
                            <th>Title</th>
                            <th>First Name</th>
                            <th>Last Name</th>
                            <th>Address Line</th>
                            <th>Town</th>
                            <th>Zip Code</th>
                            <th>Phone</th>
                            <th>Edytuj</th>
                            <th>Usuń</th>
                        </tr>
                    </thead>
                    <tbody>

                        <?php
                        foreach ($result as $row) {
                            echo "<tr>";
                            echo "<td>" . $row['customer_id'] . "</td>";
                            echo "<td>" . $row['title'] . "</td>";
                            echo "<td>" . $row['fname'] . "</td>";
                            echo "<td>" . $row['lname'] . "</td>";
                            echo "<td>" . $row['addressline'] . "</td>";
                            echo "<td>" . $row['town'] . "</td>";
                            echo "<td>" . $row['zipcode'] . "</td>";
                            echo "<td>" . $row['phone'] . "</td>";
                            // buttom edit yelow
                            echo "<td><a href='edit.php?customer_id=" . $row['customer_id'] . "' class='btn btn-warning'>Edytuj</a></td>";
                            // buttom delete
                            echo "<td><a href='delete.php?customer_id=" . $row['customer_id'] . "' class='btn btn-danger'>Usuń</a></td>";
                        }
                        ?>

                        <!-- <?php foreach ($result as $row) : ?>
                            <tr>
                                <td><?php echo $row['customer_id'] ?></td>
                                <td><?php echo $row['title'] ?></td>
                                <td><?php echo $row['fname'] ?></td>
                                <td><?php echo $row['lname'] ?></td>
                                <td><?php echo $row['addressline'] ?></td>
                                <td><?php echo $row['town'] ?></td>
                                <td><?php echo $row['zipcode'] ?></td>
                                <td><?php echo $row['phone'] ?></td>
                            </tr>
                        <?php endforeach; ?> -->
                    </tbody>
            </div>
        </div>


        <?php
        // usuwanie
        class Delete
        {
            public function delete($id)
            {
                $dbhost = "localhost";
                $dbname = "firma";
                $dbuser = "root";
                $dbpassword = "";
                $db_conn = new PDO("mysql:host=" . $dbhost . ";dbname=" . $dbname, $dbuser, $dbpassword);
                $sql = "DELETE FROM customer WHERE customer_id = :id";
                $stmt = $db_conn->prepare($sql);
                $stmt->bindParam(':id', $id);
                $stmt->execute();
                header("Location: index.php");
            }
        }

        if (isset($_GET['customer_id'])) {
            $id = $_GET['customer_id'];
            $delete = new Delete();
            $delete->delete($id);
        }



        ?>




</body>

</html>

