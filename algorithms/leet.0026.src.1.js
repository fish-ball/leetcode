/**
 * @param {number[]} A
 * @return {number}
 */
var removeDuplicates = function(A) {
    var i = 0, m = 0;
    for(; i < A.length; ++i) {
        if(m === 0 || A[i] != A[m-1]) A[m++] = A[i];
    }
    return m;
};
