// https://leetcode.cn/problems/convert-the-temperature/
// 2469. 温度转换

func convertTemperature(celsius float64) []float64 {
    return []float64{celsius + 273.15,  celsius * 1.8 + 32}
}
