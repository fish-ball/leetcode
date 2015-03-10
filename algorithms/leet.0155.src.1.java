class MinStack {
    
    int[] a = new int[99999];
    int[] b = new int[99999];
    int n = 0, m = 0;
    
    public void push(int x) {
        a[n++] = x;
        if(m == 0 || b[m-1] >= x) b[m++] = x;
    }

    public void pop() {
        if(b[m-1] == a[n-1]) m--;
        n--;
    }

    public int top() {
        return a[n-1];
    }

    public int getMin() {
        return b[m-1];
    }
    
}
