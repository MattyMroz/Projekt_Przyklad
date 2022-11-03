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

    <!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"> -->
    <!-- <link rel="stylesheet" href="style.css"> -->

</head>

<body>
    <!-- Rejestracja -->
    <div class="container mt-4">
        <div class="row d-flex justify-content-center">
            <div class="col-4 ">
                <h1 class="text-center mb-4">Registration</h1>
                <form class="form-group" action="register.php" method="post">
                    <div class="form-outline mb-3">
                        <input type="text" id="login" class="form-control" placeholder="Login" name="login" />
                    </div>

                    <div class="form-outline mb-3">
                        <input type="email" id="email" class="form-control" placeholder="Email address" name="email" />
                    </div>

                    <div class="form-outline mb-3">
                        <input type="password" id="password" class="form-control" placeholder="Password" name="password" />
                    </div>

                    <div class="form-outline mb-4">
                        <input type="password" id="password2" class="form-control" placeholder="Repeat your password" name="password2" />
                    </div>

                    <button type="submit" class="btn btn-primary btn-block mb-4" name="register">Register</button>

                    <div class="row d-flex justify-content-center mb-4">
                        <a href="login.php">Login</a>
                    </div>
                </form>
                <?php
                require_once 'db.php';
                if (isset($_POST['register'])) {
                    $login = $_POST['login'];
                    $email = $_POST['email'];
                    $password = $_POST['password'];
                    $password2 = $_POST['password2'];
                    $password_hash = password_hash($password, PASSWORD_DEFAULT);
                    $password2_hash = password_hash($password2, PASSWORD_DEFAULT);

                    // login nie może mieć więcej niż 20 znaków miećspacji i znaków specjalnych
                    // dodać plskie znaki
                    if (strlen($login) > 20 || strlen($login) < 3 || preg_match('/\s/', $login) || preg_match('/[^A-Za-z0-9]/', $login)) {
                        echo "<div class='alert alert-danger' role='alert'> Login must be between 3 and 20 characters long and cannot contain spaces or special characters </div>";
                    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
                        echo "<div class='alert alert-danger' role='alert'>Email is not valid!</div>";
                    } else if ($password != $password2) {
                        echo "<div class='alert alert-danger' role='alert'>Passwords are not the same!</div>";
                        // dodać plskie znaki
                    } else if (!preg_match('/^(?=.*\d)(?=.*[A-Za-z])[0-9A-Za-z!@#$%]{8,20}$/', $password)) {
                        echo "<div class='alert alert-danger' role='alert'>Password must be between 8 and 20 characters long and contain at least one digit, one uppercase and one lowercase letter!</div>";
                    } else {
                        // sprawdzenie czy login i email nie istnieją w bazie
                        $stmt = $conn->prepare("SELECT * FROM users WHERE login = :login OR email = :email");
                        $stmt->bindParam(':login', $login, PDO::PARAM_STR);
                        $stmt->bindParam(':email', $email, PDO::PARAM_STR);
                        $stmt->execute();
                        $user = $stmt->fetch(PDO::FETCH_ASSOC);
                        if ($user) {
                            echo "<div class='alert alert-danger' role='alert'>Login or email already exists!</div>";
                        } else {
                            // dodanie użytkownika do bazy
                            $stmt = $conn->prepare("INSERT INTO users (login, email, password) VALUES (:login, :email, :password)");
                            $stmt->bindParam(':login', $login, PDO::PARAM_STR);
                            $stmt->bindParam(':email', $email, PDO::PARAM_STR);
                            $stmt->bindParam(':password', $password_hash, PDO::PARAM_STR);
                            $stmt->execute();
                            echo "<div class='alert alert-success' role='alert'>Registration successful!</div>";
                            header("refresh:1;url=login.php");
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