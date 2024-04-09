<!DOCTYPE html>
<html lang="Fr">
<head>
<!-- Design by foolishdeveloper.com -->
    <title>Connection</title>
    <?php session_start(); ?>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;600&display=swap" rel="stylesheet">
    <!--Stylesheet-->
    <link rel="stylesheet" href="../CSS/register.css">

</head>
<body>
    <div class="background">
        <div class="shape"></div>
        <div class="shape"></div>
    </div>
        

        <form class="login" action="../PHP/creation.php" method="post">

            <h3>Créer un compte</h3>

            <label for="Nom">Nom</label>
            <input type="text" placeholder="Nom" id="Nom" name= "Nom" required>

            <label for="Prénom">Prénom</label>
            <input type="text" placeholder="Prénom" id="Prenom" name= "Prenom" required>

            <label for="username">Email</label>
            <input type="email" placeholder="Email" id="Email" name= "Email" required>

            <label for="password">Mot de passe</label>
            <input type="password" placeholder="Mot de passe" id="password" name= "password" required>
        
            <button class="submit">Log In</button>
            <a class="login__field" href="../../index.php">vous avez déja un compte ?</a>

        </form>

        
    
</body>
</html>
