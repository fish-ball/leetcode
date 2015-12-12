/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
var getHint = function(secret, guess) {
    var i, j, x, y, bull, cow, n = secret.length;
    for(i = bull = 0; i < n; ++i) {
        bull += secret[i] == guess[i] ? 1 : 0;
    }
    for(i = 0, cow = -bull; i < 10; ++i) {
        for(j = x = y = 0; j < n; ++j) {
            x += i == secret[j] ? 1 : 0;
            y += i == guess[j] ? 1 : 0;
        }
        cow += Math.min(x, y);
    }
    return ''+bull+'A'+cow+'B';
};
