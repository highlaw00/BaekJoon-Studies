import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    // 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킴
    // 벽이나 자기 자신의 몸과 부딪히면 게임이 끝남. -> 몸에 대한 정보를 기록해야한다. -> grid에 기록
    // 사과가 있다면 사과가 없어지고 꼬리는 움직이지 않는다. -> 사과의 정보 -> grid
    // 사과가 없다면 꼬리칸을 비운다. -> 몸길이가 변하지 않음. (꼬리칸이 다음 몸으로 온다)
    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());
        int[][] grid = new int[n][n]; // 빈공간 0, 사과 1, 뱀 몸 2
        int[] dx = new int[]{-1, 0, 1, 0}; // 북 동 남 서
        int[] dy = new int[]{0, 1, 0, -1};
        int currentDir = 1; // 동쪽

        for (int i=0; i<k; i++) {
            String[] line = br.readLine().split(" ");
            int x = Integer.parseInt(line[0]);
            int y = Integer.parseInt(line[1]);
            grid[x-1][y-1] = 1;
        }

        int l = Integer.parseInt(br.readLine());
        Queue<Pair> navigationQueue = new LinkedList<>();
        for (int i=0; i<l; i++) {
            String[] line = br.readLine().split(" ");
            int seq = Integer.parseInt(line[0]);
            navigationQueue.add(new Pair(seq, line[1]));
        }

        // snakeBody의 앞부분 = 머리
        // snakeBody의 끝부분 = 꼬리
        Deque<int[]> snakeBody = new LinkedList<>();
        grid[0][0] = 2;
        snakeBody.addFirst(new int[]{0, 0}); // head 삽입

        int currentSeconds = 0;
        while (true) {
            currentSeconds ++;
            int[] head = snakeBody.peekFirst();
            int headX = head[0];
            int headY = head[1];
            // 뱀의 머리 이동, 가능한지 확인
            int nx = headX + dx[currentDir];
            int ny = headY + dy[currentDir];
            if (nx < 0 || ny < 0 || nx >= n || ny >= n || grid[nx][ny] == 2) {
                break;
            }

            // 이동했는데 사과가 있는 경우 -> 머리가 이동하고 꼬리는 움직이지 않음.
            // -> deque 끝에 삽입
            if (grid[nx][ny] == 1) {
                snakeBody.addFirst(new int[]{nx, ny});
            }
            // 이동했는데 사과가 없는 경우 -> 사과 없어지고 꼬리가 움직인다.
            else {
                snakeBody.addFirst(new int[]{nx, ny});
                int[] tail = snakeBody.pollLast();
                grid[tail[0]][tail[1]] = 0;
            }
            grid[nx][ny] = 2;

            // 방향 확인
            if (!navigationQueue.isEmpty() && navigationQueue.peek().sequence == currentSeconds) {
                Pair p = navigationQueue.poll();
                if (p.direction.equals("L")) { // direction - 1
                    currentDir = Math.floorMod(currentDir - 1, 4);
                } else {
                    currentDir = Math.floorMod(currentDir + 1, 4);
                }
            }
        }
        System.out.println(currentSeconds);
    }

    public class Pair {
        public int sequence;
        public String direction;
        public Pair(int sequence, String direction) {
            this.sequence = sequence;
            this.direction = direction;
        }
    }
}
