import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    static int[][] dirs = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int problemNumber = 1;
        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) break;
            int[][] grid = new int[n][n];
            for (int i = 0; i < n; i++) {
                String[] str = br.readLine().split(" ");
                for (int j = 0; j < n; j++) {
                    grid[i][j] = Integer.parseInt(str[j]);
                }
            }
            int[][] score = new int[n][n];
            boolean[][] visited = new boolean[n][n];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) visited[i][j] = false;
            }

            PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2) {
                    return Integer.compare(o1[0], o2[0]);
                }
            });

            // 0,0 지점부터 dijkstra 탐색
            // 우선순위 큐에 해당 정점까지의 dist, i, j 저장
            pq.add(new int[]{grid[0][0], 0, 0});

            // 방문하지 않은 노드들 중 가장 가중치가 적은 노드를 선택
            while (!pq.isEmpty()) {
                int[] info = pq.poll();
                int prevDist = info[0];
                int x = info[1];
                int y = info[2];

                if (visited[x][y]) continue;
                visited[x][y] = true;
                score[x][y] = prevDist;

                if (x == n-1 && y == n-1) break;

                // 방문하지 않은 인접 노드들 전부 삽입
                for (int[] dir: dirs) {
                    int dx = dir[0];
                    int dy = dir[1];
                    int nx = x + dx;
                    int ny = y + dy;
                    if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
                    if (visited[nx][ny]) continue;
                    pq.add(new int[]{prevDist + grid[nx][ny], nx, ny});
                }
            }

            System.out.println("Problem " + problemNumber + ": " + score[n-1][n-1]);
            problemNumber ++;
        }
    }
}
