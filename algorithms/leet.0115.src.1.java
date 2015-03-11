public class Solution {
    public int numDistinct(String S, String T) {
        int K = S.length(), L = T.length();
        int[] C = new int[L+1];
        C[0] = 1;
        for(int i = 0; i < K; ++i) {
            for(int j = L; j > 0; --j) {
                if(T.charAt(j-1) == S.charAt(i)) {
                    C[j] += C[j-1];
                }
            }
        }
        return C[L];
    }
}
