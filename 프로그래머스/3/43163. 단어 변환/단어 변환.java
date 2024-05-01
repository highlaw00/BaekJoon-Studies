import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        Map<String, Boolean> visited = new HashMap<>();
        visited.put(begin, false);
        for (String word: words) {
            visited.put(word, false);
        }

        Queue<Pair> queue = new LinkedList<>();
        queue.add(new Pair(begin, 0));

        while (!queue.isEmpty()) {
            Pair pair = queue.poll();
            String keyString = pair.string;
            int cnt = pair.cnt;
            if (visited.containsKey(keyString) && visited.get(keyString)) {
                continue;
            }
            visited.put(keyString, true);
            if (keyString.equals(target)) {
                answer = cnt;
                break;
            }

            for (String word: words) {
                // 이미 만든 경우 pass
                if (visited.get(word)) continue;
                // keyString에서 알파벳 하나만 바꾸었을 때 word로 변환이 가능한지 확인
                if (getDifferentIndex(keyString, word) != -1) {
                    queue.add(new Pair(word, cnt + 1));
                }
            }
        }

        return answer;
    }

    public int getDifferentIndex(String s1, String s2) {
        int differentIdx = 0;
        int differentCnt = 0;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                differentCnt ++;
                differentIdx = i;
            }
        }

        // 서로 다른 알파벳이 1개를 넘는 경우: 변경 불가
        if (differentCnt > 1) {
            differentIdx = -1;
        }

        return differentIdx;
    }

    class Pair {
        String string;
        int cnt;
        Pair(String string, int cnt) {
           this.string = string;
           this.cnt = cnt;
        }
    }
}