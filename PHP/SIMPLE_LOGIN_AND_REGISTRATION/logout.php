<?php
session_start();
if (isset($_SESSION['user'])) {
    session_destroy();
    header("refresh:1;url=index.php");
}
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
    <!-- Wylogowanie i usunięcie sesji -->
    <div class="container mt-4">
        <div class="row d-flex justify-content-center">
            <div class="col-4 ">
                <h1 class="text-center mb-4">Successfully Logged Out!</h1>
                <div class="row d-flex justify-content-center alert alert-success" type="alert">
                    Bye! See you soon!
                </div>
            </div>
        </div>
    </div>
</body>

</html>