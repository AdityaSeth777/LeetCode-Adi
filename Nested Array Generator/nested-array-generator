type MultidimensionalArray = (MultidimensionalArray | number)[]

function* inorderTraversal(arr: MultidimensionalArray): Generator<number, void, unknown> {
    for (const v of arr) {
        if (Array.isArray(v)) yield* inorderTraversal(v);
        else yield v;
    }
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */