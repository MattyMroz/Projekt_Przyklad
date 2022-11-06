<?php
session_start();
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <form action="edit.php" method="post" class="form-group justify-content-center">
                    <?php
                    include 'db.php';
                    if (isset($_POST['edit'])) {
                        $stmt = $conn->prepare("SELECT * FROM uczniowie WHERE id_ucz = :id_ucz");
                        $stmt->bindParam(':id_ucz', $_POST['edit']);
                        $stmt->execute();
                        $result = $stmt->fetch(PDO::FETCH_ASSOC);

                        echo "<div class='d-flex justify-content-center'>";
                        echo "<div class='col-4'>";
                        echo "<input class='form-control' type='hidden' name='id_ucz' value='" . $result['id_ucz'] . "'>";
                        echo "<br>";
                        echo "<h3 class='text-center'>ID Ucznia: " . $result['id_ucz'] . "</h3>";
                        echo "<br>";
                        echo "<label class='form-label font-weight-bold' for='nazwisko'>Nazwisko</label>";
                        echo "<input class='form-control' type='text' name='nazwisko' value='" . $result['nazwisko'] . "'>";
                        echo "<br>";
                        echo "<label class='form-label font-weight-bold' for='imie'>Imię</label>";
                        echo "<input class='form-control' type='text' name='imie' value='" . $result['imie'] . "'>";
                        echo "<br>";
                        echo "<label class='form-label font-weight-bold' for='pesel'>Pesel</label>";
                        echo "<input class='form-control' type='text' name='pesel' value='" . $result['pesel'] . "'>";
                        echo "<br>";
                        echo "<label class='form-label font-weight-bold' for='adres_ul'>Ulica</label>";
                        echo "<input class='form-control' type='text' name='adres_ul' value='" . $result['adres_ul'] . "'>";
                        echo "<br>";
                        echo "<label class='form-label font-weight-bold' for='adres_nr'>Numer domu</label>";
                        echo "<input class='form-control' type='text' name='adres_nr' value='" . $result['adres_nr'] . "'>";
                        echo "<br>";
                        echo "<label class='form-label font-weight-bold' for='miasto'>Miasto</label>";
                        echo "<input class='form-control' type='text' name='miasto' value='" . $result['miasto'] . "'>";
                        echo "<br>";
                        echo "<div class='d-flex justify-content-center'>";
                        echo "<button type='submit' class='btn btn-success'>Zapisz</button>";
                        echo "<a href='user2.php' class='btn btn-primary ml-2'>Powrót</a>";
                        echo "</div>";
                        echo "</div>";
                        echo "</div>";
                    }
                    ?>
                </form>

                <?php
                if (isset($_POST['id_ucz'])) {
                    $stmt = $conn->prepare("UPDATE uczniowie SET nazwisko = :nazwisko, imie = :imie, pesel = :pesel, adres_ul = :adres_ul, adres_nr = :adres_nr, miasto = :miasto WHERE id_ucz = :id_ucz");
                    $stmt->bindParam(':id_ucz', $_POST['id_ucz']);
                    $stmt->bindParam(':nazwisko', $_POST['nazwisko']);
                    $stmt->bindParam(':imie', $_POST['imie']);
                    $stmt->bindParam(':pesel', $_POST['pesel']);
                    $stmt->bindParam(':adres_ul', $_POST['adres_ul']);
                    $stmt->bindParam(':adres_nr', $_POST['adres_nr']);
                    $stmt->bindParam(':miasto', $_POST['miasto']);
                    $stmt->execute();
                    header("Location: user2.php");
                }

                $conn = null;
                ?>
            </div>
        </div>
    </div>



</body>

</html>