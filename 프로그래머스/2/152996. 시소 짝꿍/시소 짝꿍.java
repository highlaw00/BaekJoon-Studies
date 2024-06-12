import java.util.*;

class Solution {
    public long solution(int[] weights) {
        // 몸무게: "해당 몸무게를 가진 사람 수" 를 매핑
        Map<Long, Long> weightCntMap = new HashMap<>();
        
        // Map 초기화
        for (int weight: weights) {
            long prevCnt = weightCntMap.getOrDefault((long) weight, 0L);
            weightCntMap.put((long) weight, prevCnt + 1);
        }
        
        // 내 몸무게가 x일 때.. y가 짝꿍이 되려면
        // 2y = 2x, 2y = 3x, 2y = 4x / 3y = 2x, 3y = 3x, 3y = 4x / 4y = 2x, 4y = 3x, 4y = 4x
        int[] coefficients = {2, 3, 4};
        long answer = 0L;
        
        // 몸무게가 다른 사람들을 기준으로 짝꿍 탐색
        for (long weight: weightCntMap.keySet()) {
            Set<Long> visited = new HashSet<>();
            
            for (int coX: coefficients) {
                for (int coY: coefficients) {
                    if (coX == coY) continue;
                    
                    // 나눠떨어지지 않으면 그 자체로 불가능
                    if ((coX * weight) % coY != 0) continue;
                    long target = (coX * weight) / coY;
                    
                    if (weightCntMap.containsKey(target) && !visited.contains(target)) {
                        visited.add(target);
                        answer += weightCntMap.get(weight) * weightCntMap.get(target);
                    }
                }
            }
        }
        
        // 중복 제거
        answer = answer / 2L;
        
        // 몸무게가 같은 사람들 확인
        for (long weight: weightCntMap.keySet()) {
            if (weightCntMap.get(weight) >= 2L) {
                answer += weightCntMap.get(weight) * (weightCntMap.get(weight) - 1L) / 2L;
            }
        }
        
        return answer;
    }
}