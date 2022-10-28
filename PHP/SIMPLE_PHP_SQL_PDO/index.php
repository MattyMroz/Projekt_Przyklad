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
    <div class="container">
        <div class="row mt-3">
            <!-- serch form -->
            <div class="col-12 d-flex justify-content-center">
                <form action="index.php" method="post" class="form-group">
                    <div class="d-flex justify-content-center">
                        <div class="col-6">
                            <!-- długość pola tekstowego to 50 znaków -->
                            <input class="form-control" type="text" name="search" placeholder="Wyszukaj klienta" maxlength="50" required>
                        </div>
                        <div class="col-2">
                            <button type="submit" class="btn btn-success">Szukaj</button>
                        </div>
                        <div class="col-2">
                            <a href="index.php" class="btn btn-primary">Powrót</a>
                        </div>
                    </div>
                </form>
            </div>
            <!-- table bootstrap -->
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
                    include 'db.php';
                    try {
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
                            echo "<td>
                                        <form action='edit.php' method='post'>
                                            <input type='hidden' name='edit' value='" . $row['customer_id'] . "'>
                                            <button type='submit' class='btn btn-warning'>Edytuj</button>
                                        </form>
                                    </td>";

                            // buttom delete red
                            echo "<td>
                                        <form action='delete.php' method='post'>
                                            <input type='hidden' name='delete' value='" . $row['customer_id'] . "'>
                                            <button type='submit' class='btn btn-danger'>Usuń</button>
                                        </form>
                                    </td>";
                        }
                    } catch (PDOException $e) {
                        echo "Connection failed: " . $e->getMessage();
                    }

                    $db_conn = null;
                    ?>
                </tbody>
            </table>
        </div>
        <!-- buttom add green -->
        <div class='d-flex justify-content-center'>
            <a href="add.php" class="btn btn-success">Dodaj</a>
        </div>
        <br>
        <br>
        <br>
        <br>
    </div>




</body>

</html>