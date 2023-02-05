<?php

$email = $_POST['email'];
$username = $_POST['username'];
$password = $_POST['password'];


if (/* registration was successful */) {
    echo json_encode(array('success' => true));
} else {
    echo json_encode(array('success' => false));
}

?>