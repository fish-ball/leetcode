public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        long m = n;
        m = (m & 0x55555555l) + ((m & 0xAAAAAAAAl) >> 1);
        m = (m & 0x33333333l) + ((m & 0xCCCCCCCCl) >> 2);
        m = (m & 0x0F0F0F0Fl) + ((m & 0xF0F0F0F0l) >> 4);
        m = (m & 0x00FF00FFl) + ((m & 0xFF00FF00l) >> 8);
        m = (m & 0x0000FFFFl) + ((m & 0xFFFF0000l) >> 16);
        return (int)m;
    }
}
