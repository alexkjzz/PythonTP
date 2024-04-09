<?php
session_start(); // Démarrer la session
require('connexion_bdd.php'); // Inclure fichier de connexion à la base de données

// Vérifier si le formulaire de connexion a été soumis
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Récupérer les données du formulaire
    $userEmail = $_POST["Email"];
    $password = $_POST["password"];

    // Requête SQL 
    $stmt = $conn->prepare("SELECT * FROM Utilisateurs WHERE Email = ?");
    $stmt->bind_param("s", $userEmail);
    $stmt->execute();
    $result = $stmt->get_result();

    // Vérifier si l'utilisateur existe dans la base de données
    if ($result->num_rows == 1) {
        // Récupérer toutes les informations de l'utilisateur
        $user = $result->fetch_assoc();
        
        // Vérifier si le mot de passe correspond
        if (password_verify($password, $user["MDP"])) {
            // Mot de passe correct, connexion réussie
            // Stocker les informations de l'utilisateur dans la session
            $_SESSION["userID"] = $user['ID_utilisateur'];
            $_SESSION["userNom"] = $user['Nom'];
            $_SESSION["userPrenom"] = $user['Prenom'];
            $_SESSION["userEmail"] = $user['Email'];
            $_SESSION["role"] = $user['Role'];

            // Rediriger l'utilisateur vers la page de réservation
            header("Location: ../HTML/user.html");
            exit();
        } else {
            // Mot de passe incorrect, afficher un message d'erreur
            echo "Nom d'utilisateur / email ou mot de passe incorrect.";
        }
    } else {
        // L'utilisateur n'a pas été trouvé, afficher un message d'erreur
        echo "Nom d'utilisateur / email ou mot de passe incorrect.";
    }

    // Fermer la connexion à la base de données
    $stmt->close();
    $conn->close();
}
?>
