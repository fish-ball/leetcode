/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var rangeBitwiseAnd = function(m, n) {
    for(var ans = 0, p = 1; n >= p; p *= 2) {
        if((m&p) === (n&p)) {
            ans += (m&p);
        } else {
            ans = 0;
        }
    }
    return ans;
};
