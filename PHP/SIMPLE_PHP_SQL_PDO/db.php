<?php
try {
    $dbhost = "localhost";
    $dbname = "firma";
    $dbuser = "root";
    $dbpassword = "";
    $db_conn = new PDO("mysql:host=" . $dbhost . ";dbname=" . $dbname, $dbuser, $dbpassword);
} catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}

if (isset($_POST['search'])) {
    $stmt = $db_conn->prepare("SELECT * FROM customer WHERE lname LIKE '%' :lname '%' ");
    $stmt->bindValue(':lname', $_POST['search']);
    $stmt->execute();
    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
} else {
    $sql = "SELECT * FROM customer";
    $stmt = $db_conn->prepare($sql);
    $stmt->execute();
    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// $db_conn = null;


// CREATE DATABASE firma;
// use firma;

// CREATE TABLE `customer` (
//   `customer_id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
//   `title` char(4) DEFAULT NULL,
//   `fname` varchar(32) DEFAULT NULL,
//   `lname` varchar(32) NOT NULL,
//   `addressline` varchar(64) DEFAULT NULL,
//   `town` varchar(32) DEFAULT NULL,
//   `zipcode` char(10) NOT NULL,
//   `phone` varchar(16) DEFAULT NULL
//   ) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

//   INSERT INTO `customer` (`customer_id`,`title`,`fname`,`lname`,`addressline`,`town`,`zipcode`,`phone`) VALUES
//  (1,'Miss','Jenny','Stones','27 Rowan Avenue','Hightown','NT2 1AQ','023 9876'),
//  (2,'Mr','Andrew','Stones','52 The Willows','Lowtown','LT5 7RA','876 3527'),
//  (3,'Miss','Alex','Matthew','4 The Street','Nicetown','NT2 2TX','010 4567'),
//  (4,'Mr','Adrian','Matthew','The Barn','Yuleville','YV67 2WR','487 3871'),
//  (5,'Mr','Simon','Cozens','7 Shady Lane','Oahenham','OA3 6QW','514 5926'),
//  (6,'Mr','Neil','Matthew','5 Pasture Lane','Nicetown','NT3 7RT','267 1232'),
//  (7,'Mr','Richard','Stones','34 Holly Way','Bingham','BG4 2WE','342 5982'),
//  (8,'Mrs','Anna','Stones','34 Holly Way','Bingham','BG4 2WE','342 5982'),
//  (9,'Mrs','Christine','Hickman','36 Queen Street','Histon','HT3 5EM','342 5432'),
//  (10,'Mr','Mike','Howard','86 Dysart Street','Tibsville','TB3 7FG','505 5482'),
//  (11,'Mr','Dave','Jones','54 Vale Rise','Bingham','BG3 8GD','342 8264'),
//  (12,'Mr','Richard','Neill','42 Thached way','Winersby','WB3 6GQ','505 6482'),
//  (13,'Mrs','Laura','Hendy','73 Margeritta Way','Oxbridge','OX2 3HX','821 2335'),
//  (14,'Mr','Bill','Neill','2 Beamer Street','Welltown','WT3 8GM','435 1234'),
//  (15,'Mr','David','Hudson','4  The Square','Milltown','MT2 6RT','961 4526');