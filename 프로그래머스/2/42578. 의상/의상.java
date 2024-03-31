import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        Map<String, Integer> map = new HashMap<>();
        
        for (String[] clothesInfo: clothes) {
            String category = clothesInfo[1];
            int amount = map.getOrDefault(category, 0);
            map.put(category, amount + 1);
        }
        
        for (String category: map.keySet()) {
            int count = map.get(category);
            // 현재까지의 경우의 수 * (의상의 개수 + 1)
            // +1을 해줌으로써 입지않는 경우의 수를 반영
            answer *= (count + 1);
        }
        
        // 모든 옷을 입지 않는 경우는 제외
        answer -= 1;
        
        return answer;
    }
}