<?php

header("Content-Type: application/json");

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $email = $_POST["email"];
    $username = $_POST["username"];
    $password = $_POST["password"];

    $user_details = [
        "email" => $email,
        "username" => $username,
        "password" => $password
    ];

    $file = "users.json";

    if (file_exists($file)) {
        $data = json_decode(file_get_contents($file), true);
        $data["user_details"][] = $user_details;
        file_put_contents($file, json_encode($data, JSON_PRETTY_PRINT));
    } else {
        $data = [
            "user_details" => [$user_details]
        ];
        file_put_contents($file, json_encode($data, JSON_PRETTY_PRINT));
    }

    echo json_encode(["status" => "success"]);
} else {
    echo json_encode(["status" => "error"]);
}

?>

