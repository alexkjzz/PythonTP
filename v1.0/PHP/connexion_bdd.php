<?php

// Connexion à la base de données
$servername = "mysql-serveurlucien.alwaysdata.net";
$username = "340488";
$dbpassword = "racinepython2024";
$dbname = "serveurlucien_pythonbdd";

$conn = new mysqli($servername, $username, $dbpassword, $dbname);

// verification de la connexion
if ($conn->connect_error) {
    die ("La connexion a echoué : " . $conn->connect_error);
    
}

?>