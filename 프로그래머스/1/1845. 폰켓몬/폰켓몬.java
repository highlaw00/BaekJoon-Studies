import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int n = nums.length;
        Map<Integer, Boolean> map = new HashMap<>();
        
        for (int pokemonNum: nums) {
            map.put(pokemonNum, true);
        }
        
        for (Integer pokemonNum: map.keySet()) {
            if (answer == n / 2) {
                break;
            }
            answer += 1;
        }
        
        return answer;
    }
}