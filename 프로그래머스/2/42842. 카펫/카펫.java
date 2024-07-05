import java.util.*; 

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {0, 0};
        int total = brown + yellow;
        // 1 ~ (total)^(1/2)
        for (int i = 1; i <= Math.sqrt(total); i++) {
            int height = i;
            if (height < 2) continue;
            if (total % height != 0) continue;
            
            int width = total / height;
            if (yellow == (height - 2) * (width - 2)) {
                answer[0] = width;
                answer[1] = height;
                break;
            }
        }
        return answer;
    }
}