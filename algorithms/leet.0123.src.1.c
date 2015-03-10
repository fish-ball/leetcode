int maxProfit(int prices[], int n) {
    
    // definitions
    int a[100000] = {}, b[100000] = {}, i = 0, p;
    
    int low, high, mx = 0;
    
    // bound case
    if(n == 0) return 0;

    low = high = prices[0];
    mx = 0;
    for(i = 1; i < n; ++i) {
        p = prices[i];
        if(p > high) {
            high = p;
            if(mx < high - low) {
                mx = high - low;
            }
        } else if(p < low) {
            low = high = p;
        }
        a[i] = mx;
    }
    
    high = low = prices[n-1];
    mx = 0;
    for(i = n-2; i >= 0; --i) {
        p = prices[i];
        if(p < low) {
            low = p;
            if(mx < high - low) {
                mx = high - low;
            }
        } else if(p > high) {
            low = high = p;
        }
        b[i] = mx;
    }
    
    mx = 0;
    for(i = 0; i < n; ++i) {
        if(mx < a[i] + b[i]) {
            mx = a[i] + b[i];
        }
    }
    
    return mx;
    
}
