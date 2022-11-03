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
    <!-- Przekierowanie do formularzy logowania i rejestracji -->
    <?php if (empty($_SESSION['user'])) : ?>
        <div class="container mt-4">
            <div class="row d-flex justify-content-center">
                <div class="col-4 ">
                    <h1 class="text-center mb-4">Login And Registration</h1>
                    <div class="row">
                        <a href="login.php" class="btn btn-primary btn-block mb-4">Login</a>
                    </div>

                    <div class="row">
                        <a href="register.php" class="btn btn-primary btn-block mb-4">Register</a>
                    </div>
                </div>
            </div>
        </div>
    <?php else : ?>
        <div class="container mt-4">
            <div class="row d-flex justify-content-center">
                <div class="col-4 ">
                    <h1 class="text-center mb-4">Hi, <?= $_SESSION['user'] ?>! </h1>
                    <div class="row d-flex justify-content-center alert alert-success" type="alert">
                        You have registered successfully!
                    </div>
                    <div class="row">
                        <a href="logout.php" class="btn btn-primary btn-block mb-4">Logout</a>
                    </div>
                </div>
            </div>
        </div>
    <?php endif; ?>
</body>

</html>