class Solution {
    fun solution(n: Int, a: Int, b: Int): Int {
        var answer = 0
        var numa = a;
        var numb = b;
        for (i in 1 until 22) {
            numa = (numa + 1) / 2;
            numb = (numb + 1) / 2;
            if (numa ==  numb) {
                answer = i
                break;
            }
        }
        return answer
    }
}