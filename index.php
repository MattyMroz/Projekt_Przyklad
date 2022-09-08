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





