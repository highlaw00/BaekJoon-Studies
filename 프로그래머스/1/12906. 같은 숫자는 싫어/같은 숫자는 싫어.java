import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Queue<Integer> queue = new LinkedList<>();
        
        int curr = -1;
        int prev = -1;
        for (int i=0; i < arr.length; i ++) {
            curr = arr[i];
            if (prev != curr) {
                queue.add(curr);
            }
            prev = curr;
        }
        
        int[] answer = new int[queue.size()];
        int len = queue.size();
        for (int i = 0; i < len; i ++) {
            answer[i] = queue.poll();
        }
        
        return answer;
    }
}