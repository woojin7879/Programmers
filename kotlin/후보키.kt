import kotlin.math.*
class Solution {
    lateinit var table: Array<Array<String>>
    val minList = ArrayList<Int>()
    fun solution(relation: Array<Array<String>>): Int {
        var answer = 0
        table = relation
        for (i in 1 until ((2.0).pow(relation[0].size).toInt())) {
            if (!checkUnique(i)) continue
            if (!checkMinimum(minList, i)) continue
            minList.add(i)
            answer++
        }
        return answer
    }
    fun checkMinimum(list: ArrayList<Int>, index: Int) : Boolean {
        list.forEach { key ->
            if (key and index == key) {
                return false
            }
        }
        return true
    }
    fun checkUnique(index: Int) : Boolean {
        val list = ArrayList<Int>()
        for (i in 0 until table[0].size) {
            val bit = 1 shl i
            if (index and bit != 0) {
                list.add(i)
            }
        }
        val uniqueSet = HashSet<String>()

        table.forEach { tuple ->
            val sb = StringBuilder()
            list.forEach { index ->
                sb.append(tuple[index]).append("?")
            }
            uniqueSet.add(sb.toString())
        }
        if (uniqueSet.size < table.size) {
            return false
        }
        return true
    }
}