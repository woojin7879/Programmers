class Solution {
    fun solution(s: String): Int {
        var answer = s.length;
        for (i in 1 until (s.length / 2 + 1)) {
          var temp = s.substring(0,i);
          var length = s.length;
          var same = 1;
          for (j in i until (s.length) step(i)){
            if (s.substring(j, Math.min(j + i, s.length)) == temp) {
              length = length - i;
              same += 1;
            } else {
              if (same > 1) {
                length += same.toString().length;
              }
              temp = s.substring(j, Math.min(j + i, s.length));
              same = 1;
            }
          }
          if (same > 1) {
            length += same.toString().length;
          }
          answer = Math.min(length, answer);
        }
        return answer
    }
}