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
    <!-- Logowanie -->
    <div class="container mt-4">
        <div class="row d-flex justify-content-center">
            <div class="col-4 ">
                <h1 class="text-center mb-4">Sign in</h1>
                <form class="form-group" action="login.php" method="post">
                    <div class="form-outline mb-3">
                        <input type="email" id="email" class="form-control" placeholder="Email address" name="email" />
                    </div>

                    <div class="form-outline mb-3">
                        <input type="password" id="password" class="form-control" placeholder="Password" name="password" />
                    </div>

                    <div class="row mb-4">
                        <div class="col d-flex justify-content-center">
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" value="" id="form2Example31" checked />
                                <label class="form-check-label" for="form2Example31"> Remember me </label>
                            </div>
                        </div>

                        <div class="col">
                            <a href="#!">Forgot password?</a>
                        </div>
                    </div>

                    <button type="submit" name="login" class="btn btn-primary btn-block mb-4">Sign in</button>

                    <div class="row d-flex justify-content-center mb-4">
                        <a href="register.php">Register</a>
                    </div>
                </form>
                <?php
                require_once 'db.php';
                if (isset($_POST['login'])) {
                    $email = $_POST['email'];
                    $password = $_POST['password'];
                    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
                        echo "<div class='alert alert-danger' role='alert'>Email is not valid!</div>";
                        // dodać plskie znaki
                    } else if (!preg_match('/^(?=.*\d)(?=.*[A-Za-z])[0-9A-Za-z!@#$%]{8,20}$/', $password)) {
                        echo "<div class='alert alert-danger' role='alert'>Password must be between 8 and 20 characters long and contain at least one digit, one uppercase and one lowercase letter!</div>";
                    } else {
                        $stmt = $conn->prepare("SELECT * FROM users WHERE email = :email");
                        $stmt->bindParam(':email', $email, PDO::PARAM_STR);
                        $stmt->execute();
                        $user = $stmt->fetch(PDO::FETCH_ASSOC);
                        if ($user) {
                            if (password_verify($password, $user['password'])) {
                                $_SESSION['user'] = htmlspecialchars($user['login']);
                                echo "<div class='alert alert-success' role='alert'>Login successful!</div>";
                                header("Location: index.php");
                            } else {
                                echo "<div class='alert alert-danger' role='alert'>Wrong password!</div>";
                            }
                        } else {
                            echo "<div class='alert alert-danger' role='alert'>User does not exist!</div>";
                        }
                    }
                }
                $conn = null;
                ?>
            </div>
        </div>
    </div>
</body>

</html>