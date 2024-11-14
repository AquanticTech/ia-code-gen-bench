const fs = require('fs');
const vm = require('vm');

/**
 * Extrait le code JavaScript d'un fichier Markdown et l'exécute.
 * @param {string} markdownFilePath - Chemin du fichier Markdown.
 * @returns {Promise<any>} - Une promesse qui résout avec le résultat de l'exécution du code.
 */
async function executeJsFromMarkdown(markdownFilePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(markdownFilePath, 'utf-8', (err, data) => {
      if (err) {
        reject(err);
        return;
      }

      // Expression régulière pour extraire le code JavaScript entre les balises ```javascript ... ```
      const jsCodeRegex = /```javascript([\s\S]*?)```/g;
      let match;
      let jsCode = '';

      while ((match = jsCodeRegex.exec(data)) !== null) {
        jsCode += match[1];
      }


      if (!jsCode) {
        reject(new Error('Aucun code JavaScript trouvé dans le fichier Markdown.'));
        return;
      }

      try {

        // Crée un contexte de VM sandbox pour une exécution sécurisée.
        const context = vm.createContext({});
        const script = new vm.Script(jsCode);
        const result = script.runInContext(context);
        resolve(result);

      } catch (executionError) {
        reject(new Error(`Erreur lors de l'exécution du code JavaScript: ${executionError.message}`));
      }
    });
  });
}


// Exemple d'utilisation :
const markdownFile = process.argv[2] || 'sortArray8D_solution-codellama.md'; // Par défaut, le fichier codellama.md


executeJsFromMarkdown(markdownFile)
  .then(result => {
    console.log('Résultat de l\'exécution du code JavaScript:', result);
  })
  .catch(error => {
    console.error('Erreur:', error.message);
  });

