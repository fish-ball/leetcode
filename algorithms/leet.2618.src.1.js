/**
 * @param {any} object
 * @param {any} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj === null || classFunction === null) return false
    if (obj === void 0 || classFunction === void 0) return false
    if (classFunction === Object) return true
    while (obj !== null && obj.__proto__) {
        if (obj.__proto__ === classFunction.prototype) return true
        obj = obj.__proto__
    }
    return false
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
