public class Solution {
    public int majorityElement(int[] num) {
        int L = num.length;
        Arrays.sort(num);
        return num[L/2];
    }
}
