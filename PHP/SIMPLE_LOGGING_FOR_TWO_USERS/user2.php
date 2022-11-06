<?php
session_start();
$_SESSION['user'] = "user2";
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
    <div class="time">
        <?php
        $date = date("Y-m-d H:i:s");
        echo $date;
        ?>
    </div>
    <div class="container mt-4">
        <div class="row d-flex justify-content-center">
            <div class="col-4">
                <h1 class="text-center mb-4">Uczniowie</h1>
                <div class="row d-flex justify-content-center">
                    <a href="index.php" class="btn btn-danger btn-block mb-4">Rozłącz</a>
                </div>
            </div>
        </div>

        <div class="row d-flex justify-content-center">
            <div class="col-6">
                <h1 class="text-center mb-4">Imię i Nazwisko</h1>
                <div class="d-flex justify-content-center">
                    <form action="user2.php" method="post">
                        <div class="form-check">
                            <?php
                            require 'db.php';

                            $sql = "SELECT * FROM `uczniowie`";
                            $result = $conn->query($sql);

                            foreach ($result as $row) {
                                echo '<input class="form-check-input" type="checkbox" name="uczen[]" value="' . $row['id_ucz'] . '" id="' . $row['id_ucz'] . '">';
                                echo '<label class="form-check-label" for="' . $row['id_ucz'] . '">'
                                    . $row['imie'] . ' ' . $row['nazwisko'] . '
                                    </label><br>';
                            }
                            ?>
                        </div>

                        <div class='d-flex justify-content-center mt-4'>
                            <button class="btn btn-primary" name="search">Szukaj</button>
                        </div>
                    </form>
                </div>


            </div>
            <div class="col-6">
                <h1 class="text-center mb-4">Dane</h1>
                <div class="d-flex justify-content-center">
                    <table class="table table-striped table-hover">
                        <thead class="bg-primary">
                            <tr>
                                <th scope="col">Imię</th>
                                <th scope="col">Nazwisko</th>
                                <th scope="col">Pesel</th>
                                <th scope="col">Ulica</th>
                                <th scope="col">Numer</th>
                                <th scope="col">Miasto</th>
                                <th scope="col">Edytuj</th>
                                <th scope="col">Usuń</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php
                            if (isset($_POST['search']) && isset($_POST['uczen'])) {
                                $uczen = $_POST['uczen'];
                                $sql = "SELECT * FROM `uczniowie` WHERE `id_ucz` IN (" . implode(',', $uczen) . ")";
                                $result = $conn->query($sql);

                                foreach ($result as $row) {
                                    echo '<tr>';
                                    echo '<td>' . $row['imie'] . '</td>';
                                    echo '<td>' . $row['nazwisko'] . '</td>';
                                    echo '<td>' . $row['pesel'] . '</td>';
                                    echo '<td>' . $row['adres_ul'] . '</td>';
                                    echo '<td>' . $row['adres_nr'] . '</td>';
                                    echo '<td>' . $row['miasto'] . '</td>';
                                    echo '<td>
                                            <form action="edit.php" method="post">
                                                <input type="hidden" name="edit" value="' . $row['id_ucz'] . '">
                                                <button class="btn btn-warning">Edytuj</button>
                                            </form>
                                        </td>';
                                    echo '<td>
                                            <form action="delete.php" method="post">
                                                <input type="hidden" name="delete" value="' . $row['id_ucz'] . '">
                                                <button class="btn btn-danger">Usuń</button>
                                            </form>
                                            </td>';
                                    echo '</tr>';
                                }
                            } else {
                                $sql = "SELECT * FROM `uczniowie`";
                                $result = $conn->query($sql);

                                foreach ($result as $row) {
                                    echo '<tr>';
                                    echo '<td>' . $row['imie'] . '</td>';
                                    echo '<td>' . $row['nazwisko'] . '</td>';
                                    echo '<td>' . $row['pesel'] . '</td>';
                                    echo '<td>' . $row['adres_ul'] . '</td>';
                                    echo '<td>' . $row['adres_nr'] . '</td>';
                                    echo '<td>' . $row['miasto'] . '</td>';
                                    echo '<td>
                                            <form action="edit.php" method="post">
                                                <input type="hidden" name="edit" value="' . $row['id_ucz'] . '">
                                                <button class="btn btn-warning">Edytuj</button>
                                            </form>
                                        </td>';
                                    echo '<td>
                                            <form action="delete.php" method="post">
                                                <input type="hidden" name="delete" value="' . $row['id_ucz'] . '">
                                                <button class="btn btn-danger">Usuń</button>
                                            </form>
                                            </td>';
                                    echo '</tr>';
                                }
                            }
                            ?>
                            <tr>
                                <td colspan="8">
                                    <form action="add.php" method="post">
                                        <div class="d-flex justify-content-center">
                                            <button class="btn btn-success">Dodaj Ucznia</button>
                                        </div>
                                    </form>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <?php

                if (isset($_POST['search']) && isset($_POST['uczen'])) {
                    $uczen = $_POST['uczen'];
                    $sql = "SELECT `pesel` FROM `uczniowie` WHERE `id_ucz` IN (" . implode(',', $uczen) . ")";
                    $result = $conn->query($sql);
                } else {
                    $sql = "SELECT `pesel` FROM `uczniowie`";
                    $result = $conn->query($sql);
                }

                $pesel = [];
                foreach ($result as $row) {
                    $pesel[] = $row['pesel'];
                }
                $rocznik = [];
                foreach ($pesel as $row) {
                    $rocznik[] = substr($row, 0, 2);
                }
                $rocznik2 = [];
                foreach ($rocznik as $row) {
                    if ($row[0] == 0 || $row[0] == 1) {
                        $rocznik2[] = '20' . $row;
                    } else {
                        $rocznik2[] = '19' . $row;
                    }
                }
                sort($rocznik2);

                $rocznik3 = array_count_values($rocznik2);
                echo '<div class="d-flex justify-content-center">';
                echo '<table class="table table-striped table-hover">';
                echo '<thead class="bg-primary">';
                echo '<tr>';
                echo '<th scope="col">Rocznik</th>';
                echo '<th scope="col">Ilość Uczniów</th>';
                echo '</tr>';
                echo '</thead>';
                echo '<tbody>';
                foreach ($rocznik3 as $key => $value) {
                    echo '<tr>';
                    echo '<td>' . $key . '</td>';
                    echo '<td>' . $value . '</td>';
                    echo '</tr>';
                }
                echo '</tbody>';
                echo '</table>';
                echo '</div>';
                $conn = null;
                ?>
            </div>
        </div>
    </div>`
</body>

</html>