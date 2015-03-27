public class Solution {
    public List<List<Integer>> generate(int numRows) {
        
        // case == 0
        if(numRows == 0) return new ArrayList<List<Integer>>();
        
        // case > 0
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        ArrayList<Integer> last = new ArrayList<Integer>();
        last.add(1);
        
        for(int i = 0; i < numRows; ++i) {
            ans.add(last);
            ArrayList<Integer> current = new ArrayList<Integer>();
            current.add(1);
            for(int j = 1; j < last.size(); ++j) {
                current.add(last.get(j-1) + last.get(j));
            }
            current.add(1);
            last = current;
        }
        return ans;
    }
}
