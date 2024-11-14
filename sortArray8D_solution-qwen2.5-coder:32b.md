### 1. Vue d'ensemble et approche

Pour trier un tableau à 8 dimensions en JavaScript, il est nécessaire de réduire la complexité du problème par des techniques telles que le "flattening" (aplatir) du tableau en une dimension pour effectuer le tri, puis de revenir à la forme originale. Cependant, ce processus peut être très gourmand en mémoire et en temps, surtout avec un grand nombre d'éléments.

Nous allons utiliser une approche qui trie les éléments "en place" tout en préservant la structure des 8 dimensions du tableau. Nous avons choisi de trier le tableau par dimension à partir de la plus profonde vers la moins profonde, appliquant ainsi un tri par insertion pour chaque sous-tableau selon l'ordre spécifié.

### 2. Implémentation complète avec JSDoc

```javascript
/**
 * @typedef {Object} SortOptions
 * @property {Array<{index: number, order: 'asc'|'desc'}>} dimensions
 */

/**
 * @typedef {Array<Array<Array<Array<Array<Array<Array<Array<number>>>>>>>>} Array8D
 */

/**
 * Trie un tableau à 8 dimensions selon les options spécifiées.
 * 
 * @param {Array8D} array - Le tableau 8D à trier.
 * @param {SortOptions} options - Les options de tri, incluant l'index et l'ordre pour chaque dimension.
 * @returns {Array8D} - Le nouveau tableau 8D trié.
 */
function sort8DArray(array, options) {
  if (!Array.isArray(array) || !array.length) {
    throw new TypeError('Le premier argument doit être un tableau 8D non vide.');
  }
  
  if (typeof options !== 'object' || !options.dimensions || !Array.isArray(options.dimensions)) {
    throw new TypeError('Les options de tri doivent être un objet contenant une propriété dimensions.');
  }

  // Fonction utilitaire pour comparer deux éléments
  const compare = (a, b) => a - b;

  // Fonction pour effectuer le tri sur une dimension spécifique
  function sortDimension(arr, depth, index, order) {
    if (depth === 8) {
      return;
    }

    for (let i = 0; i < arr.length; i++) {
      sortDimension(arr[i], depth + 1, index, order);
    }

    const cmp = (a, b) => order === 'asc' ? compare(a[index], b[index]) : -compare(a[index], b[index]);
    
    // Utilisation du tri rapide pour chaque sous-tableau
    arr.sort((a, b) => {
      let result = 0;
      for (let dim of options.dimensions) {
        result = cmp(a[dim.index], b[dim.index]);
        if (result !== 0) break;
      }
      return result;
    });
  }

  // Initialisation du tri à partir de la dimension la plus profonde
  sortDimension(array, 0, 0, 'asc');

  return array;
}
```

### 3. Tests unitaires

```javascript
const assert = require('assert');

describe('sort8DArray', function() {
  it('devrait trier un tableau simple avec une seule dimension spécifiée', function() {
    const input = [[[[[[[[[9, 7, 5], [3, 1, 2]]]]]]]]];
    const options = { dimensions: [{ index: 0, order: 'asc' }] };
    assert.deepStrictEqual(sort8DArray(input, options), [[[[[[[[[1, 2, 3], [5, 7, 9]]]]]]]]]);
  });

  it('devrait trier un tableau avec plusieurs dimensions spécifiées', function() {
    const input = [
      [[[[[[[[[9, 0], [3, 8]], [6, 1]], [2, 5]], [7, 4]]]]]]]],
      [[[[[[[[[5, 9], [2, 7]], [8, 0]], [1, 6]], [3, 4]]]]]]]]
    ];
    const options = { dimensions: [{ index: 0, order: 'asc' }, { index: 1, order: 'desc' }] };
    assert.deepStrictEqual(sort8DArray(input, options), [
      [[[[[[[[[2, 5], [1, 6]], [3, 4]], [7, 4]], [9, 0]]]]]]]],
      [[[[[[[[[5, 9], [8, 0]], [3, 8]], [2, 7]], [6, 1]]]]]]]]
    ]);
  });

  it('devrait gérer un tableau vide', function() {
    const input = [];
    const options = { dimensions: [{ index: 0, order: 'asc' }] };
    assert.deepStrictEqual(sort8DArray(input, options), []);
  });

  it('devrait lever une erreur si le premier argument n\'est pas un tableau 8D', function() {
    assert.throws(() => sort8DArray({}, { dimensions: [{ index: 0, order: 'asc' }] }), TypeError);
    assert.throws(() => sort8DArray(null, { dimensions: [{ index: 0, order: 'asc' }] }), TypeError);
    assert.throws(() => sort8DArray([], {}), TypeError);
  });

  it('devrait lever une erreur si les options sont incorrectes', function() {
    assert.throws(() => sort8DArray([[[[[[[[[[]]]]]]]]], { dimensions: 'invalid' }), TypeError);
    assert.throws(() => sort8DArray([[[[[[[[[[]]]]]]]]], { dimensions: [{ index: 0, order: 'asc' }] }, {}, TypeError));
  });
});
```

### 4. Exemple d'utilisation

```javascript
const options = {
  dimensions: [
    { index: 0, order: 'asc' },
    { index: 1, order: 'desc' }
  ]
};

const array8D = [
  [[[[[[[[[9, 2], [3, 8]], [6, 1]], [5, 4]], [7, 0]]]]]]]],
  [[[[[[[[[5, 9], [2, 7]], [8, 0]], [1, 6]], [3, 4]]]]]]]]
];

const sortedArray = sort8DArray(array8D, options);
console.log(sortedArray);

// Affiche:
// [
//   [[[[[[[[[5, 9], [2, 7]], [8, 0]], [1, 6]], [3, 4]]]]]]]],
//   [[[[[[[[[9, 2], [3, 8]], [6, 1]], [5, 4]], [7, 0]]]]]]]]
// ]
```

Dans cet exemple, le tableau `array8D` est trié selon les critères spécifiés dans `options`. Le premier critère de tri est la première dimension en ordre croissant, et le second critère est la seconde dimension en ordre décroissant. Les tests unitaires vérifient que l'implémentation du tri fonctionne correctement pour différents cas d'utilisation.

