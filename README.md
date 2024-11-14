# ia-code-gen-bench

Ce référentiel vise à comparer rapidement les performances des modèles LLM en génération de code, en utilisant le moteur Ollama, y compris des modèles comme QWEN2.5-coder.

## Objectif

L'objectif principal est d'évaluer et de comparer la qualité du code généré par différents modèles LLM pour une tâche spécifique : le tri d'un tableau à 8 dimensions en JavaScript.  Ce benchmark se concentre sur plusieurs critères d'évaluation, notamment la performance, la gestion des erreurs, la qualité du code et la documentation.

## Méthodologie

Le processus de benchmark est automatisé grâce au script `prompt.sh`. Ce script effectue les étapes suivantes :

1. **Sélection du modèle:** L'utilisateur choisit parmi une liste de modèles disponibles via une interface interactive. Les modèles actuellement supportés incluent `codellama`, `qwen2.5-coder`, `deepseek-coder` et `mistral`.
2. **Exécution du prompt:** Le script charge le prompt contenu dans le fichier `prompt.txt` et l'exécute avec le modèle LLM sélectionné via Ollama. Le prompt définit la tâche de génération de code, les exigences spécifiques (performance, gestion des erreurs, etc.) et les critères d'évaluation.
3. **Sauvegarde du résultat:** Le code généré par le modèle est sauvegardé dans un fichier spécifique au modèle (e.g., `sortArray8D_solution-codellama.js`).

Le script `parseSrcToFile.py` permet d'analyser le contenu du répertoire et de générer un fichier JSON (`repository_contents.json`) contenant les informations sur chaque fichier, y compris leur contenu. Ceci facilite l'analyse ultérieure du code généré.

## Prompt

Le fichier `prompt.txt` contient le prompt détaillé pour la tâche de génération de code. Il est structuré en sections claires pour fournir un contexte, les exigences, les contraintes et les critères d'évaluation au modèle LLM.  Le prompt demande spécifiquement :

* Une fonction JavaScript pour trier un tableau 8D.
* Des performances optimales (O(n log n)).
* Une gestion robuste des erreurs.
* Des tests unitaires.
* Une documentation JSDoc complète.

## Analyse des résultats

Les fichiers `sortArray8D_solution-*.md` contiennent les réponses des différents modèles LLM.  L'analyse de ces fichiers permet de comparer les solutions proposées selon les critères d'évaluation définis dans le prompt.  Vous pouvez comparer les implémentations, les tests unitaires et la documentation générée par chaque modèle pour déterminer lequel est le plus performant pour cette tâche spécifique.

## Exécution du benchmark

Pour exécuter le benchmark, suivez ces étapes :

1. Assurez-vous d'avoir installé Ollama et les modèles LLM que vous souhaitez tester.
2. Clonez ce référentiel.
3. Exécutez le script `prompt.sh`.
4. Sélectionnez le modèle LLM souhaité.
5. Le code généré sera sauvegardé dans le répertoire.

## Contributions

Les contributions sont les bienvenues. Vous pouvez contribuer en :

* Ajoutant des modèles LLM au benchmark.
* Améliorant le script `prompt.sh`.
* Proposant des tâches de génération de code supplémentaires.
* Analysant et comparant les résultats des différents modèles.


## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.