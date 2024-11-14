#!/bin/bash

# Liste des modèles disponibles pour le test
models=("codellama" "qwen2.5-coder" "deepseek-coder" "mistral")

# Demande de sélection du modèle
echo "Sélectionnez le modèle parmi les options suivantes :"
select model in "${models[@]}"; do
  if [[ " ${models[*]} " == *" $model "* ]]; then
    echo "Modèle sélectionné : $model"
    break
  else
    echo "Sélection invalide, veuillez réessayer."
  fi
done


# Sauvegarde du prompt dans un fichier
cat << 'EOT' > prompt.txt
[CONTEXT]
Je suis un développeur travaillant sur une application d'analyse de données multidimensionnelles qui nécessite une fonction de tri optimisée pour des tableaux à 8 dimensions en JavaScript.

[TASK]
Créer une fonction JavaScript permettant de trier un tableau à 8 dimensions selon des critères spécifiques.

[REQUIREMENTS]
Environnement:
- JavaScript (ES2022+)
- Node.js 18+ / Navigateurs modernes
- Pas de dépendances externes
- JSDoc pour documentation

Spécifications de la fonction:
- Entrée: Un tableau 8D de nombres + options de tri
- Sortie: Nouveau tableau 8D trié
- Performance: O(n log n)
- Mémoire: O(1) préféré
- Temps réponse: <100ms pour 10x10x10x10x10x10x10x10

Exemple de structure:
```javascript
/**
 * @typedef {Object} SortOptions
 * @property {Array<{index: number, order: 'asc'|'desc'}>} dimensions
 */

/**
 * @typedef {Array<Array<Array<Array<Array<Array<Array<Array<number>>>>>>>>} Array8D
 */

const options = {
  dimensions: [
    { index: 0, order: 'asc' },
    { index: 3, order: 'desc' }
  ]
};

/**
 * @param {Array8D} array
 * @param {SortOptions} options
 * @returns {Array8D}
 */
function sort8DArray(array, options) {
  // Implementation requise
}
```

[CONSTRAINTS]
1. Code lisible et bien documenté (JSDoc)
2. Gestion des erreurs robuste
3. Tests unitaires requis
4. Pas de variables globales
5. Utiliser les méthodes natives quand possible
6. Compatible navigateurs modernes

[OUTPUT_FORMAT]
Structurer la réponse en 4 parties:
1. Vue d'ensemble et approche
2. Implémentation complète avec JSDoc
3. Tests unitaires
4. Exemple d'utilisation

[EVALUATION_CRITERIA]
- Qualité du code et documentation: 40%
- Performance et optimisation: 30%
- Gestion des erreurs: 15%
- Tests et couverture: 15%

[INSTRUCTIONS]
Générer une solution complète qui:
1. Respecte les contraintes de performance
2. Inclut une documentation complète
3. Gère les cas d'erreur
4. Fournit des tests
5. Utilise les features modernes de JS

[END]
Merci de fournir une solution complète et optimisée suivant ces spécifications.
EOT

# Exécution d'Ollama avec le prompt
ollama run $model "$(cat prompt.txt)" > sortArray8D_solution-$model.js

echo "La solution a été enregistrée dans sortArray8D_solution-$model.js"