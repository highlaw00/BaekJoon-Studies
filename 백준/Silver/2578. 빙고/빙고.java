import java.util.*;
import java.io.*;

public class Main {
    class Pair {
        int number;
        boolean isCalled;
        Pair(int number) {
            this.number = number;
            this.isCalled = false;
        }
    }
    
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        Pair[][] board = new Pair[5][5];
        List<Integer> numbers = new ArrayList<>();

        for (int i = 0; i < 5; i++) {
            String line = br.readLine();
            st = new StringTokenizer(line);
            for (int j = 0; j < 5; j++) {
                int number = Integer.parseInt(st.nextToken());
                board[i][j] = new Pair(number);
            }
        }

        for (int i = 0; i < 5; i++) {
            String line = br.readLine();
            st = new StringTokenizer(line);
            while (st.hasMoreTokens()) {
                int number = Integer.parseInt(st.nextToken());
                numbers.add(number);
            }
        }

        for (int idx = 0; idx < numbers.size(); idx++) {
            int number = numbers.get(idx);
            // 빙고판에서 찾기
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    if (board[i][j].number == number) {
                        board[i][j].isCalled = true;
                    }
                }
            }

            // 빙고 여부 확인하기
            if (checkBingo(board)) {
                System.out.println(idx + 1);
                break;
            }
        }
    }

    public boolean checkBingo(Pair[][] board) {
        int bingoCnt = 0;
        // 행, 열 확인
        for (int i = 0; i < 5; i++) {
            int rowCnt = 0;
            int colCnt = 0;
            for (int j = 0; j < 5; j++) {
                if (board[i][j].isCalled) rowCnt++;
                if (board[j][i].isCalled) colCnt++;
            }
            if (rowCnt == 5) bingoCnt ++;
            if (colCnt == 5) bingoCnt ++;
        }

        // 대각방향 확인
        int leftToRightCrossCnt = 0;
        int rightToLeftCrossCnt = 0;
        for (int i = 0; i < 5; i++) {
            if (board[i][i].isCalled) leftToRightCrossCnt++;
            if (board[i][4-i].isCalled) rightToLeftCrossCnt++;
        }
        if (leftToRightCrossCnt == 5) bingoCnt++;
        if (rightToLeftCrossCnt == 5) bingoCnt++;

        return bingoCnt >= 3;
    }
}
