import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        // Queue에 index 삽입
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < progresses.length; i ++) {
            queue.add(i);
        }
        
        // Queue가 빌 때 까지..
        while (!queue.isEmpty()) {
            // 모든 기능 하루 개발하기
            for (int i = 0; i < progresses.length; i ++) {
                if (progresses[i] >= 100) continue;
                progresses[i] += speeds[i];
            }
            int releaseCnt = 0;
            while (!queue.isEmpty() && progresses[queue.peek()] >= 100) {
                releaseCnt += 1;
                queue.poll();
            }
            // 출시 가능하다면 출시하기
            if (releaseCnt > 0) {
                answer.add(releaseCnt);
            }
        }
        
        int[] ansArray = answer.stream().mapToInt(i -> i).toArray();
        
        return ansArray;
    }
}