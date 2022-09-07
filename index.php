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
