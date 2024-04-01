import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for (int score: scoville) {
            pq.add(score);
        }
        
        // 남은 음식이 1개라면 종료
        // 가장 맵지 않은 음식이 K 이상이 될 때까지 진행
        while (pq.size() > 1 && pq.peek() < K) {
            int mildest = pq.poll();
            int mildestSecond = pq.poll();
            
            mildest += 2 * mildestSecond;
            pq.add(mildest);
            answer += 1;
        }
        
        if (pq.peek() < K) answer = -1;
        
        return answer;
    }
}