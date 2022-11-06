<?php
session_start();
include 'db.php';
if (isset($_POST['delete'])) {
    $stmt = $conn->prepare("DELETE FROM uczniowie WHERE id_ucz = :id_ucz");
    $stmt->bindParam(':id_ucz', $_POST['delete']);
    $stmt->execute();
    header("Location: user2.php");
    $conn = null;
}
