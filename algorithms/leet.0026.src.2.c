int removeDuplicates(int A[], int n) {
    int m = 0, i = 0;
    while(i < n) {
        if(m == 0 || A[i] != A[m-1]) {
            A[m++] = A[i];
        }
        i += 1;
    }
    return m;
}
