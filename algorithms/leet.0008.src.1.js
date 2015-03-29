/**
 * @param {string} str
 * @return {number}
 */
var atoi = function(str) {
    return Math.max(Math.min(parseInt(str), 2147483647), -2147483648) || 0;
};
