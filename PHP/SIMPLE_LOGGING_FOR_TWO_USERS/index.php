<?php
session_start();
if (isset($_SESSION['user']) && $_SESSION['user'] == 'user2') {
    $_SESSION = array();
}
$_SESSION['user'] = "user1";
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
    <div class="container mt-4">
        <div class="row d-flex justify-content-center">
            <div class="col-4">
                <h1 class="text-center mb-4">Uczniowie</h1>
                <div class="row d-flex justify-content-center">
                    <a href="user2.php" class="btn btn-success btn-block mb-4">Połącz</a>
                </div>
            </div>
        </div>

        <div class="row d-flex justify-content-center">
            <div class="col-6">
                <h1 class="text-center mb-4">Imię i Nazwisko</h1>
                <div class="d-flex justify-content-center">
                    <form action="index.php" method="post">
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
                <h1 class="text-center mb-4">Adresy</h1>
                <div class="d-flex justify-content-center">
                    <table class="table table-striped table-hover">
                        <thead class="bg-primary">
                            <tr>
                                <th scope="col">Imię</th>
                                <th scope="col">Nazwisko</th>
                                <th scope="col">Ulica</th>
                                <th scope="col">Numer</th>
                                <th scope="col">Miasto</th>
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
                                    echo '<td>' . $row['adres_ul'] . '</td>';
                                    echo '<td>' . $row['adres_nr'] . '</td>';
                                    echo '<td>' . $row['miasto'] . '</td>';
                                    echo '</tr>';
                                }
                                $conn = null;
                            } else {
                                $sql = "SELECT * FROM `uczniowie`";
                                $result = $conn->query($sql);

                                foreach ($result as $row) {
                                    echo '<tr>';
                                    echo '<td>' . $row['imie'] . '</td>';
                                    echo '<td>' . $row['nazwisko'] . '</td>';
                                    echo '<td>' . $row['adres_ul'] . '</td>';
                                    echo '<td>' . $row['adres_nr'] . '</td>';
                                    echo '<td>' . $row['miasto'] . '</td>';
                                    echo '</tr>';
                                }
                            }
                            $conn = null;
                            ?>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
    <?php
    session_destroy();
    ?>
</body>

</html>