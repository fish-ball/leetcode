public class Solution {
    public boolean canJump(int[] A) {
        int i = 0, j = 0;
        while(j < A.length - 1 && i <= j && i < A.length) {
            if(j < i + A[i]) j = i + A[i];
            i++;
        }
        return j >= A.length - 1;
    }
}
