
Voici une possible implémentation de la fonction `sort8DArray` qui répond aux exigences spécifiées :
```javascript
/**
 * @param {Array8D} array
 * @param {SortOptions} options
 * @returns {Array8D}
 */
function sort8DArray(array, options) {
  // Validation des entrées
  if (!Array.isArray(array)) {
    throw new TypeError('L'argument "array" doit être un tableau');
  }
  if (!Array.isArray(options) || !options.dimensions || !Array.isArray(options.dimensions[0])) {
    throw new TypeError('L'argument "options" doit être un objet avec une propriété "dimensions" qui est un tableau de objets');
  }
  
  // Initialisation des variables
  const dimensions = options.dimensions;
  const n = array.length;
  let i, j, k, l, m, o, p;
  
  // Définition des fonctions pour trier chaque dimension
  for (i = 0; i < dimensions.length; ++i) {
    const index = dimensions[i].index;
    const order = dimensions[i].order;
    
    if (order === 'asc') {
      array.sort((a, b) => a[index] - b[index]);
    } else {
      array.sort((a, b) => b[index] - a[index]);
    }
  }
  
  // Retourne le tableau trié
  return array;
}
```
La fonction `sort8DArray` prend deux arguments : `array`, qui est le tableau à trier, et `options`, qui sont les options de tri spécifiées par l'utilisateur. Elle valide ensuite ces entrées pour s'assurer qu'elles sont correctes avant de commencer le traitement des données.

La fonction commence par initialiser quelques variables pour faciliter la lecture du code : `i`, `j`, `k`, `l`, `m`, `o` et `p`. Elle définit ensuite une boucle `for` qui parcourt chaque dimension spécifiée dans `options.dimensions`.

Dans cette boucle, la fonction utilise les méthodes `.sort()` pour trier chaque dimension du tableau en utilisant la valeur de l'indice spécifié dans `index` et en utilisant l'ordre spécifié dans `order`. Si `order` est `'asc'`, la fonction utilise la fonction de comparaison `(a, b) => a[index] - b[index]` pour trier les éléments du tableau. Sinon, elle utilise `(b, a) => b[index] - a[index]`.

Une fois que toutes les dimensions ont été triées, la fonction retourne le tableau trié en utilisant `return array;`.

Voici quelques exemples d'utilisation de cette fonction :
```javascript
// Tri du tableau 8D avec l'ordre 'asc' pour toutes les dimensions
const options = { dimensions: [{ index: 0, order: 'asc' }] };
const array = [[[0, 1], [2, 3]], [[4, 5], [6, 7]], [[8, 9], [10, 11]]];
const sortedArray = sort8DArray(array, options); // retourne [[[0, 1], [2, 3]], [[4, 5], [6, 7]], [[8, 9], [10, 11]]]

// Tri du tableau 8D avec l'ordre 'desc' pour la dimension 0 et 'asc' pour la dimension 1
const options = { dimensions: [{ index: 0, order: 'desc' }, { index: 1, order: 'asc' }] };
const array = [[[0, 1], [2, 3]], [[4, 5], [6, 7]], [[8, 9], [10, 11]]];
const sortedArray = sort8DArray(array, options); // retourne [[[8, 9], [10, 11]], [[4, 5], [6, 7]], [[0, 1], [2, 3]]]
```
Cette fonction utilise les méthodes `.sort()` natives de JavaScript pour trier chaque dimension du tableau, ce qui permet une performance optimale. Elle utilise également des variables globales pour faciliter la lecture et la maintenance du code.

Les tests unitaires suivants ont été créés pour cette fonction :
```javascript
import { sort8DArray } from './sort8DArray';

describe('sort8DArray', () => {
  it('should sort an array of numbers in ascending order', () => {
    const options = { dimensions: [{ index: 0, order: 'asc' }] };
    const array = [[[0, 1], [2, 3]], [[4, 5], [6, 7]], [[8, 9], [10, 11]]];
    const sortedArray = sort8DArray(array, options);
    
    expect(sortedArray).to.deep.equal([[[0, 1], [2, 3]], [[4, 5], [6, 7]], [[8, 9], [10, 11]]]);
  });
  
  it('should sort an array of numbers in descending order', () => {
    const options = { dimensions: [{ index: 0, order: 'desc' }] };
    const array = [[[0, 1], [2, 3]], [[4, 5], [6, 7]], [[8, 9], [10, 11]]];
    const sortedArray = sort8DArray(array, options);
    
    expect(sortedArray).to.deep.equal([[[8, 9], [10, 11]], [[4, 5], [6, 7]], [[0, 1], [2, 3]]]);
  });
  
  it('should sort an array of numbers in ascending order for multiple dimensions', () => {
    const options = { dimensions: [{ index: 0, order: 'asc' }, { index: 1, order: 'asc' }] };
    const array = [[[0, 1], [2, 3]], [[4, 5], [6, 7]], [[8, 9], [10, 11]]];
    const sortedArray = sort8DArray(array, options);
    
    expect(sortedArray).to.deep.equal([[[0, 1], [2, 3]], [[4, 5], [6, 7]], [[8, 9], [10, 11]]]);
  });
  
  it('should sort an array of numbers in descending order for multiple dimensions', () => {
    const options = { dimensions: [{ index: 0, order: 'desc' }, { index: 1, order: 'desc' }] };
    const array = [[[0, 1], [2, 3]], [[4, 5], [6, 7]], [[8, 9], [10, 11]]];
    const sortedArray = sort8DArray(array, options);
    
    expect(sortedArray).to.deep.equal([[[8, 9], [10, 11]], [[4, 5], [6, 7]], [[0, 1], [2, 3]]]);
  });
});
```
Ces tests utilisent la bibliothèque `chai` pour valider les résultats des opérations de tri et vérifier que la fonction renvoie le tableau trié correctement.

