class MinStack {
    
    int a[99999], b[99999];
    int n = 0, m = 0;
    
public:

    void push(int x) {
        a[n++] = x;
        if(m == 0 || b[m-1] >= x) b[m++] = x;
    }

    void pop() {
        if(n == 0) return;
        if(b[m-1] == a[n-1]) m--;
        n--;
    }

    int top() {
        return n ? a[n-1] : 0;
    }

    int getMin() {
        return m ? b[m-1] : 0;
    }
    
};
