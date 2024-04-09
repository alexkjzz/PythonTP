<?php
session_start(); // Démarrer la session
require('connexion_bdd.php'); // Inclure fichier de connexion à la base de données

// Vérifier si le formulaire de création de compte a été soumis
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Récupérer les données du formulaire
    $usernameEmail = $_POST["Email"];
    $password = $_POST["password"];
    $userPrenom = $_POST["Prenom"];
    $userNom = $_POST["Nom"];

    // Valider l'adresse e-mail
    if (filter_var($usernameEmail, FILTER_VALIDATE_EMAIL)) {
        // Utiliser des déclarations préparées pour éviter les injections SQL
        $stmt = $conn->prepare("SELECT * FROM Utilisateurs WHERE Email = ?");
        $stmt->bind_param("s", $usernameEmail);
        $stmt->execute();
        $result_check_duplicate = $stmt->get_result();

        if ($result_check_duplicate->num_rows > 0) {
            // Doublon trouvé, afficher un message d'erreur
            echo "Un compte avec ce nom d'utilisateur ou email existe déjà.";
        } else {
            // Hacher le mot de passe
            $hashed_password = password_hash($password, PASSWORD_DEFAULT);

            // Insérer les données dans la base de données avec le mot de passe chiffré
            $stmt_insert = $conn->prepare("INSERT INTO Utilisateurs (Email, MDP, Prenom, Nom) VALUES (?, ?, ?, ?)");
            $stmt_insert->bind_param("ssss", $usernameEmail, $hashed_password, $userPrenom, $userNom);

            if ($stmt_insert->execute()) {
                // Compte créé avec succès
                echo "Compte créé avec succès !";
                header("refresh:5;url=../HTML/user.html");
            } else {
                // Erreur lors de l'insertion dans la base de données
                echo "Erreur lors de la création du compte : " . $stmt_insert->error;
            }
        }

        // Fermer la connexion à la base de données
        $stmt->close();
        $stmt_insert->close();
    } else {
        // Adresse e-mail invalide, afficher un message d'erreur
        echo "Adresse e-mail invalide.";
    }

    $conn->close();
}
?>
