/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    var l = 0, r = citations.length + 1, m;
    while(l+1<r) {
        m = l+r>>1;
        if(gteCount(citations, m) >= m) l = m;
        else r = m;
    }
    return l;
};

var gteCount = function(arr, x) {
    var l = -1, r = arr.length, m;
    while(l+1<r) {
        m = l+r>>1;
        if(arr[m] < x) l = m;
        else r = m;
    }
    return arr.length - r;
};
