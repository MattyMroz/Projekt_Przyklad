<?php
include 'db.php';
if (isset($_POST['delete'])) {
    $stmt = $db_conn->prepare("DELETE FROM customer WHERE customer_id = :customer_id");
    $stmt->bindParam(':customer_id', $_POST['delete']);
    $stmt->execute();
    header("Location: index.php");
}
