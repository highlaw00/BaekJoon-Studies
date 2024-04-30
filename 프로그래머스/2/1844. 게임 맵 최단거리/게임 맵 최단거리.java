import java.util.*;

class Solution {
    static int[][] dirs = new int[][] {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    public int solution(int[][] maps) {
        int answer = -1;
        int n = maps.length, m = maps[0].length;
        boolean[][] visited = new boolean[n][m];
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0, 1});

        while (!queue.isEmpty()) {
            int[] pair = queue.poll();
            int i = pair[0], j = pair[1], cnt = pair[2];
            if (visited[i][j]) continue;
            visited[i][j] = true;

            if (i == n-1 && j == m-1) {
                answer = cnt;
                break;
            }

            for (int[] dir: dirs) {
                int di = dir[0], dj = dir[1];
                int ni = i + di, nj = j + dj;
                if (ni < 0 || nj < 0 || ni >= n || nj >= m) continue;
                if (maps[ni][nj] == 0 || visited[ni][nj]) continue;
                queue.add(new int[] {ni, nj, cnt + 1});
            }
        }

        return answer;
    }
}