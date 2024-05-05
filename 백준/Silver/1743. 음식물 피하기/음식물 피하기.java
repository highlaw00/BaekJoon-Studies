import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        System.out.println(new Main().solution());
    }

    public int solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int n = Integer.parseInt(line[0]), m = Integer.parseInt(line[1]), k = Integer.parseInt(line[2]);
        int answer = 0;

        // grid 초기화
        int[][] grid = new int[n+1][m+1];
        boolean[][] visited = new boolean[n+1][m+1];
        for (int i = 0; i < k; i++) {
            String[] rowCol = br.readLine().split(" ");
            int row = Integer.parseInt(rowCol[0]), col = Integer.parseInt(rowCol[1]);
            grid[row][col] = 1;
        }

        // 각 칸을 iterate. 해당 칸의 값이 1인 경우 bfs.
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    answer = Integer.max(answer, bfs(i, j, grid, visited));
                }
            }
        }

        return answer;
    }

    public int bfs(int si, int sj, int[][] grid, boolean[][] visited) {
        int cnt = 0;
        int[][] dirs = new int[][]{
                {1, 0}, {-1, 0}, {0, 1}, {0, -1}
        };
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{si, sj});
        visited[si][sj] = true;

        while (!queue.isEmpty()) {
            cnt += 1;
            int[] location = queue.poll();
            int i = location[0], j = location[1];

            for (int[] dir: dirs) {
                int di = dir[0], dj = dir[1];
                int ni = i + di, nj = j + dj;
                if (ni <= 0 || nj <= 0 || ni >= grid.length || nj >= grid[0].length) continue;
                if (grid[ni][nj] == 0 || visited[ni][nj]) continue;
                visited[ni][nj] = true;
                queue.add(new int[] {ni, nj});
            }
        }

        return cnt;
    }
}
