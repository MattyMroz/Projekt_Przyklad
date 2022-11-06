<?php
if (isset($_SESSION['user'])) {
    if ($_SESSION['user'] == 'user1') {
        try {
            $dbhost = "localhost";
            $dbname = "szkola";
            $dbuser = "user1";
            $dbpassword = "user1";
            $conn = new PDO("mysql:host=" . $dbhost . ";dbname=" . $dbname, $dbuser, $dbpassword);
        } catch (PDOException $e) {
            echo "Connection failed: " . $e->getMessage();
        }
    }
    if ($_SESSION['user'] == 'user2') {
        try {
            $dbhost = "localhost";
            $dbname = "szkola";
            $dbuser = "user2";
            $dbpassword = "user2";
            $conn = new PDO("mysql:host=" . $dbhost . ";dbname=" . $dbname, $dbuser, $dbpassword);
        } catch (PDOException $e) {
            echo "Connection failed: " . $e->getMessage();
        }
    }
}
// $conn = null;
