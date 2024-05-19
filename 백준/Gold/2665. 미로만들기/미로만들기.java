import java.util.*;
import java.io.*;

public class Main {

    class Pair {
        int i;
        int j;
        Pair(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] rooms = new int[n][n];
        // 흰 방: 1, 검은 방: 0
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < n; j++) {
                rooms[i][j] = line.charAt(j) - '0';
            }
        }

        int[][] changedRooms = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) changedRooms[i][j] = Integer.MAX_VALUE;
        }

        // (0, 0) 부터 (n-1, n-1)까지 bfs 진행
        Queue<Pair> queue = new LinkedList<>();
        changedRooms[0][0] = 0;
        queue.add(new Pair(0, 0));
        int[][] dirs = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        while (!queue.isEmpty()) {
            Pair p = queue.poll();
            int i = p.i, j = p.j;
            for (int[] dir: dirs) {
                int di = dir[0], dj = dir[1];
                int ni = i + di, nj = j + dj;
                if (ni < 0 || nj < 0 || ni >= n || nj >= n) continue;

                // 색깔을 바꾼 방의 개수를 더 적게할 수 있는 경우 추가
                int currChangedCnt = changedRooms[i][j];
                int nextChangedCnt = changedRooms[ni][nj];

                if (currChangedCnt < nextChangedCnt) {
                    // 흰 방인 경우
                    if (rooms[ni][nj] == 1) {
                        changedRooms[ni][nj] = currChangedCnt;
                    } else {
                        changedRooms[ni][nj] = currChangedCnt + 1;
                    }
                    queue.add(new Pair(ni, nj));
                }
            }
        }

        System.out.println(changedRooms[n-1][n-1]);
    }

}
