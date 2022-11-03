<?php
try {
    $dbhost = "localhost";
    $dbname = "app";
    $dbuser = "root";
    $dbpassword = "";
    $conn = new PDO("mysql:host=" . $dbhost . ";dbname=" . $dbname, $dbuser, $dbpassword);
} catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}

// $conn = null;
