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
    <!-- bootstrap -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <form action="add.php" method="post" class="form-group justify-content-center">
                    <div class="d-flex justify-content-center">
                        <div class="col-6">
                            <br>
                            <h3 class="text-center">Dodaj Nowego Uczna</h3>
                            <label for="nazwisko">Nazwisko</label>
                            <input type="text" name="nazwisko" id="nazwisko" class="form-control">
                            <label for="imie">Imie</label>
                            <input type="text" name="imie" id="imie" class="form-control">
                            <label for="pesel">Pesel</label>
                            <input type="text" name="pesel" id="pesel" class="form-control">
                            <label for="adres_ul">Ulica</label>
                            <input type="text" name="adres_ul" id="adres_ul" class="form-control">
                            <label for="adres_nr">Numer domu</label>
                            <input type="text" name="adres_nr" id="adres_nr" class="form-control">
                            <label for="miasto">Miasto</label>
                            <input type="text" name="miasto" id="miasto" class="form-control">
                            <br>
                            <div class="d-flex justify-content-center">
                                <button type="submit" class="btn btn-success">Dodaj</button>
                                <a href="user2.php" class="btn btn-primary ml-2">Powrót</a>
                            </div>
                        </div>
                    </div>
                </form>

                <?php
                // include 'db.php';

                // try {
                //     if (isset($_POST['title']) && isset($_POST['fname']) && isset($_POST['lname']) && isset($_POST['addressline']) && isset($_POST['town']) && isset($_POST['zipcode']) && isset($_POST['phone'])) {

                //         if (empty($_POST['title']) || empty($_POST['fname']) || empty($_POST['lname']) || empty($_POST['addressline']) || empty($_POST['town']) || empty($_POST['zipcode']) || empty($_POST['phone'])) {
                //             echo '<div class="alert alert-danger" role="alert">
                //             Wypełnij wszystkie pola!
                //           </div>';
                //         } else {
                //             $stmt = $db_conn->prepare("INSERT INTO customer (title, fname, lname, addressline, town, zipcode, phone) VALUES (:title, :fname, :lname, :addressline, :town, :zipcode, :phone)");
                //             $stmt->bindParam(':title', $_POST['title']);
                //             $stmt->bindParam(':fname', $_POST['fname']);
                //             $stmt->bindParam(':lname', $_POST['lname']);
                //             $stmt->bindParam(':addressline', $_POST['addressline']);
                //             $stmt->bindParam(':town', $_POST['town']);
                //             $stmt->bindParam(':zipcode', $_POST['zipcode']);
                //             $stmt->bindParam(':phone', $_POST['phone']);
                //             $stmt->execute();

                //             echo "<div class='alert alert-success' role='alert'>
                //             Dodano nowego klienta
                //           </div>";
                //             header("refresh:1;url=index.php");
                //         }
                //     }
                // } catch (PDOException $e) {
                //     echo "<div class='alert alert-danger' role='alert'>
                //     Nie udało się dodać klienta
                //   </div>";
                //     header("refresh:1;url=index.php");
                // }

                require_once 'db.php';

                if (isset($_POST['nazwisko']) && isset($_POST['imie']) && isset($_POST['pesel']) && isset($_POST['adres_ul']) && isset($_POST['adres_nr']) && isset($_POST['miasto'])) {

                    if (empty($_POST['nazwisko']) || empty($_POST['imie']) || empty($_POST['pesel']) || empty($_POST['adres_ul']) || empty($_POST['adres_nr']) || empty($_POST['miasto'])) {
                        echo '<div class="alert alert-danger" role="alert">
                        Wypełnij wszystkie pola!
                      </div>';
                    } else {
                        $stmt = $conn->prepare("INSERT INTO uczniowie (nazwisko, imie, pesel, adres_ul, adres_nr, miasto) VALUES (:nazwisko, :imie, :pesel, :adres_ul, :adres_nr, :miasto)");
                        $stmt->bindParam(':nazwisko', $_POST['nazwisko']);
                        $stmt->bindParam(':imie', $_POST['imie']);
                        $stmt->bindParam(':pesel', $_POST['pesel']);
                        $stmt->bindParam(':adres_ul', $_POST['adres_ul']);
                        $stmt->bindParam(':adres_nr', $_POST['adres_nr']);
                        $stmt->bindParam(':miasto', $_POST['miasto']);
                        $stmt->execute();

                        echo "<div class='alert alert-success' role='alert'>
                        Dodano nowego ucznia
                      </div>";
                        header("refresh:1;url=user2.php");
                    }
                }
                $conn = null;
                ?>

            </div>
        </div>
    </div>



</body>

</html>