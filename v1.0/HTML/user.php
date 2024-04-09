<!DOCTYPE html>
<html lang="fr">
    <?php session_start(); ?>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../CSS/user.css">
    <title>Utilisateur</title>
</head>
<header>
    <?php echo $_SESSION["userPrenom"];?>
    <a class="login__field" href="../../index.php">Se déconnecter</a>
</header>
<body>
    <section id="liste-films" class="cartes-films">
    </section>
    <script src="../JS/user.js"></script>
</body>

</html>