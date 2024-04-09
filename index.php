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
    <link rel="stylesheet" href="v1.0/CSS/index.css">
</head>
<body>
    <div class="background">
        <div class="shape"></div>
        <div class="shape"></div>
    </div>
    
        

        <form class="login" action="v1.0/PHP/connexion.php" method="post">

            <h3>Se connecter</h3>

            <label for="username">Email</label>
            <input type="text" placeholder="Email" id="Email" name= "Email" required>

            <label for="password">Mot de passe</label>
            <input type="password" placeholder="Mot de passe" id="password" name= "password" required>

            <button>Se connecter</button>
            <a class="login__field" href="/v1.0/HTML/register.php">vous n'avez pas de compte ?</a>
        </form>

        
        
        
        
    
</body>
</html>