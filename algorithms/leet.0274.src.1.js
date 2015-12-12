/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    // Note that the default sort condition 
    //   is based on string comparision.
    citations.sort(function(a,b){return a-b;});
    var ans = 0, n = citations.length, h;
    for(h = 1; h <= n; ++h) {
        if(gteCount(citations, h) >= h) ans = h;
    }
    return ans;
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
