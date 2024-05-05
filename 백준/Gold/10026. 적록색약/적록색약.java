import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void solution() throws IOException {
        // 적록색약이 아닌 사람과 적록색약인 사람의 구역의 수를 공백으로 출력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        // grid 초기화
        char[][] normalGrid = new char[n][n];
        char[][] blindnessGrid = new char[n][n];
        int normalAnswer = 0;
        int blindnessAnswer = 0;

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < line.length(); j++) {
                char ch = line.charAt(j);
                normalGrid[i][j] = ch;
                if (ch == 'G') ch = 'R';
                blindnessGrid[i][j] = ch;
            }
        }

        boolean[][] normalVisited = new boolean[n][n];
        boolean[][] blindnessVisited = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!normalVisited[i][j]) {
                    bfs(i, j, normalGrid, normalVisited);
                    normalAnswer++;
                }
                if (!blindnessVisited[i][j]) {
                    bfs(i, j, blindnessGrid, blindnessVisited);
                    blindnessAnswer++;
                }
            }
        }
        
        System.out.println(normalAnswer + " " + blindnessAnswer);
    }

    public void bfs(int si, int sj, char[][] grid, boolean[][] visited) {
        int[][] dirs = new int[][] {
                {1, 0}, {-1, 0}, {0, 1}, {0, -1}
        };
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {si, sj});
        visited[si][sj] = true;

        while (!queue.isEmpty()) {
            int[] pair = queue.poll();
            int i = pair[0], j = pair[1];
            for (int[] dir: dirs) {
                int di = dir[0], dj = dir[1];
                int ni = i + di, nj = j + dj;
                if (ni < 0 || nj < 0 || ni >= grid.length || nj >= grid[0].length || visited[ni][nj]) continue;
                if (grid[i][j] == grid[ni][nj]) {
                    visited[ni][nj] = true;
                    queue.add(new int[] {ni, nj});
                }
            }
        }
    }
}
