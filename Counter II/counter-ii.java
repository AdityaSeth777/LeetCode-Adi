/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let counter = init;
    let resetVal = init;

    let obj = {
        increment : () => ++counter,
        decrement : () => --counter,
        reset : () => counter = resetVal
    }

    return obj;
};