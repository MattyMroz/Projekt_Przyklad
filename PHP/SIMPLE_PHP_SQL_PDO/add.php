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
                            <h3 class="text-center">Dodaj nowego klienta</h3>
                            <br>
                            <input class="form-control" type="text" name="title" placeholder="Tytuł">
                            <br>
                            <input class="form-control" type="text" name="fname" placeholder="Imię">
                            <br>
                            <input class="form-control" type="text" name="lname" placeholder="Nazwisko">
                            <br>
                            <input class="form-control" type="text" name="addressline" placeholder="Adres">
                            <br>
                            <input class="form-control" type="text" name="town" placeholder="Miasto">
                            <br>
                            <input class="form-control" type="text" name="zipcode" placeholder="Kod pocztowy">
                            <br>
                            <input class="form-control" type="text" name="phone" placeholder="Telefon">
                            <br>
                            <div class="d-flex justify-content-center">
                                <button type="submit" class="btn btn-success">Dodaj</button>
                                <a href="index.php" class="btn btn-primary ml-2">Powrót</a>
                            </div>
                        </div>
                    </div>
                </form>

                <?php
                include 'db.php';

                try {
                    if (isset($_POST['title']) && isset($_POST['fname']) && isset($_POST['lname']) && isset($_POST['addressline']) && isset($_POST['town']) && isset($_POST['zipcode']) && isset($_POST['phone'])) {

                        if (empty($_POST['title']) || empty($_POST['fname']) || empty($_POST['lname']) || empty($_POST['addressline']) || empty($_POST['town']) || empty($_POST['zipcode']) || empty($_POST['phone'])) {
                            echo '<div class="alert alert-danger" role="alert">
                            Wypełnij wszystkie pola!
                          </div>';
                        } else {
                            $stmt = $db_conn->prepare("INSERT INTO customer (title, fname, lname, addressline, town, zipcode, phone) VALUES (:title, :fname, :lname, :addressline, :town, :zipcode, :phone)");
                            $stmt->bindParam(':title', $_POST['title']);
                            $stmt->bindParam(':fname', $_POST['fname']);
                            $stmt->bindParam(':lname', $_POST['lname']);
                            $stmt->bindParam(':addressline', $_POST['addressline']);
                            $stmt->bindParam(':town', $_POST['town']);
                            $stmt->bindParam(':zipcode', $_POST['zipcode']);
                            $stmt->bindParam(':phone', $_POST['phone']);
                            $stmt->execute();

                            echo "<div class='alert alert-success' role='alert'>
                            Dodano nowego klienta
                          </div>";
                            header("refresh:1;url=index.php");
                        }
                    }
                } catch (PDOException $e) {
                    echo "<div class='alert alert-danger' role='alert'>
                    Nie udało się dodać klienta
                  </div>";
                    header("refresh:1;url=index.php");
                }
                ?>

            </div>
        </div>
    </div>



</body>

</html>