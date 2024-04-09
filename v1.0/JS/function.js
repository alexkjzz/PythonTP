const { exec } = require('child_process');

// Chemin vers le script Python
const cheminScriptPython = 'v1.0/PYTHON/function.py';

// Exécuter le script Python
exec(`python ${cheminScriptPython}`, (err, stdout, stderr) => {
    if (err) {
        console.error('Erreur lors de l\'exécution du script Python:', err);
        return;
    }

    // Utiliser directement la sortie JSON sans la parser
    const filmsData = stdout;

    // Afficher les informations des films dans la console
    console.log(filmsData);
});
