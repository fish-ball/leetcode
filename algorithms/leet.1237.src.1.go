// https://leetcode.cn/problems/find-positive-integer-solution-for-a-given-equation/
// 1237. 找出给定方程的正整数解

/** 
 * This is the declaration of customFunction API.
 * @param  x    int
 * @param  x    int
 * @return 	    Returns f(x, y) for any given positive integers x and y.
 *			    Note that f(x, y) is increasing with respect to both x and y.
 *              i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
 */

func findSolution(customFunction func(int, int) int, z int) [][]int {
    ans := [][]int{}
    for x, yy := 1, 1000; x <= 1000; x++ {
        for y := yy; y >= 1; y-- {
            zz := customFunction(x, y)
            if zz < z { continue }
            if zz == z {
                ans = append(ans, []int{x, y})
            } else { yy = y }
        }
    }
    return ans
}
