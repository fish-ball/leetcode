/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class Solution {
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        ArrayList<Interval> result = new ArrayList<Interval>();
        for(Interval itv : intervals) {
            if(newInterval == null) {
                result.add(itv);
            } else if(newInterval.start > itv.end) {
                // not overlapping
                result.add(itv);
            } else if(newInterval.end < itv.start) {
                if(newInterval != null) {
                    result.add(newInterval);
                    newInterval = null;
                }
                result.add(itv);
            } else {
                // overlapping
                newInterval.start = Math.min(newInterval.start, itv.start);
                newInterval.end = Math.max(newInterval.end, itv.end);
            }
        }
        if(newInterval != null) {
            result.add(newInterval);
        }
        return result;
    }
}
