import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        // command: [start, end, idx]
        int[] answer = new int[commands.length];
        int cnt = 0;
        for (int[] command: commands) {
            int s = command[0]; // 2
            int e = command[1]; // 5
            int idx = command[2]; // 3
            
            ArrayList<Integer> arr = new ArrayList<>();
            
            for (int i=s-1; i<=e-1; i++) {
                arr.add(array[i]);
            }
            
            Collections.sort(arr);
            
            answer[cnt] = arr.get(idx-1);
            cnt += 1;
        }
        return answer;
    }
}