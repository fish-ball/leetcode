public class Solution {
    public List<List<Integer>> subsets(int[] S) {
        int L = S.length;
        for(int i = 0; i < L; ++i) {
            for(int j = 0; j < i; ++j) {
                if(S[i] < S[j]) {
                    int t = S[i];
                    S[i] = S[j];
                    S[j] = t;
                }
            }
        }
        int mask = 1 << L;
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        for(int b = 0; b < mask; ++b) {
            List<Integer> subset = new ArrayList<Integer>();
            for(int i = 0; i < L; ++i) {
                if(((1<<i) & b) > 0) {
                    subset.add(S[i]);
                }
            }
            ans.add(subset);
        }
        return ans;
    }
}
