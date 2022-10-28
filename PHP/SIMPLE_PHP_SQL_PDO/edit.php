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
                        $stmt = $db_conn->prepare("SELECT * FROM customer WHERE customer_id = :customer_id");
                        $stmt->bindParam(':customer_id', $_POST['edit']);
                        $stmt->execute();
                        $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
                        foreach ($result as $row) {
                            echo "<div class='d-flex justify-content-center'>";
                            echo "<div class='col-6'>";
                            echo "<input class='form-control' type='hidden' name='customer_id' value='" . $row['customer_id'] . "'>";
                            echo "<br>";
                            echo "<h3 class='text-center'>Edycja danych: Customer nr: " . $row['customer_id'] . "</h3>";
                            echo "<br>";
                            echo "<input class='form-control' type='text' name='title' value='" . $row['title'] . "'>";
                            echo "<br>";
                            echo "<input class='form-control' type='text' name='fname' value='" . $row['fname'] . "'>";
                            echo "<br>";
                            echo "<input class='form-control' type='text' name='lname' value='" . $row['lname'] . "'>";
                            echo "<br>";
                            echo "<input class='form-control' type='text' name='addressline' value='" . $row['addressline'] . "'>";
                            echo "<br>";
                            echo "<input class='form-control' type='text' name='town' value='" . $row['town'] . "'>";
                            echo "<br>";
                            echo "<input class='form-control' type='text' name='zipcode' value='" . $row['zipcode'] . "'>";
                            echo "<br>";
                            echo "<input class='form-control' type='text' name='phone' value='" . $row['phone'] . "'>";
                            echo "<br>";
                            echo "<div class='d-flex justify-content-center'>";
                            echo "<button type='submit' class='btn btn-success'>Zapisz</button>";
                            echo "<a href='index.php' class='btn btn-primary ml-2'>Powrót</a>";
                            echo "</div>";
                            echo "</div>";
                            echo "</div>";
                        }
                    }

                    if (isset($_POST['customer_id'])) {
                        $stmt = $db_conn->prepare("UPDATE customer SET title = :title, fname = :fname, lname = :lname, addressline = :addressline, town = :town, zipcode = :zipcode, phone = :phone WHERE customer_id = :customer_id");
                        $stmt->bindParam(':customer_id', $_POST['customer_id']);
                        $stmt->bindParam(':title', $_POST['title']);
                        $stmt->bindParam(':fname', $_POST['fname']);
                        $stmt->bindParam(':lname', $_POST['lname']);
                        $stmt->bindParam(':addressline', $_POST['addressline']);
                        $stmt->bindParam(':town', $_POST['town']);
                        $stmt->bindParam(':zipcode', $_POST['zipcode']);
                        $stmt->bindParam(':phone', $_POST['phone']);
                        $stmt->execute();
                        header("Location: index.php");
                    }
                    ?>
                </form>
            </div>
        </div>
    </div>



</body>

</html>



<?php
// include 'db.php';
// if (isset($_POST['edit'])) {
//     $stmt = $db_conn->prepare("SELECT * FROM customer WHERE customer_id = :customer_id");
//     $stmt->bindParam(':customer_id', $_POST['edit']);
//     $stmt->execute();
//     $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
//     foreach ($result as $row) {
//         echo "<form action='edit.php' method='post' class='form-group'>";
//         echo "<input class='form-control' type='hidden' name='customer_id' value='" . $row['customer_id'] . "'>";
//         echo "<input class='form-control' type='text' name='title' value='" . $row['title'] . "'>";
//         echo "<input class='form-control' type='text' name='fname' value='" . $row['fname'] . "'>";
//         echo "<input class='form-control' type='text' name='lname' value='" . $row['lname'] . "'>";
//         echo "<input class='form-control' type='text' name='addressline' value='" . $row['addressline'] . "'>";
//         echo "<input class='form-control' type='text' name='town' value='" . $row['town'] . "'>";
//         echo "<input class='form-control' type='text' name='zipcode' value='" . $row['zipcode'] . "'>";
//         echo "<input class='form-control' type='text' name='phone' value='" . $row['phone'] . "'>";
//         echo "<button type='submit' class='btn btn-success'>Zapisz</button>";
//         echo "</form>";
//     }
// }
?>