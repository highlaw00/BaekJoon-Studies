import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void solution() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i=0; i<t; i++) {
            String[] line = br.readLine().split(" ");
            int len = Integer.parseInt(line[0]);
            int targetIdx = Integer.parseInt(line[1]);

            // index 별 priority 저장
            int[] priorities = Arrays.stream(br.readLine().split( " ")).mapToInt(Integer::parseInt).toArray();
            // priority 별 개수 저장
            int[] priorityCnts = new int[10];
            int maximumPriority = 0;
            for (int priority: priorities) {
                priorityCnts[priority]++;
                maximumPriority = Math.max(maximumPriority, priority);
            }

            Queue<Integer> queue = new LinkedList<>();
            int[] answer = new int[len];
            int printedCnt = 0;
            for (int j=0; j<len; j++) queue.add(j);

            while (!queue.isEmpty()) {
                int idx = queue.peek();
                // 현재 top이 가장 우선순위가 높은 경우 출력
                if (priorities[idx] == maximumPriority) {
                    printedCnt ++;
                    answer[idx] = printedCnt;
                    queue.poll();

                    // 가장 높은 우선순위 개수 갱신
                    priorityCnts[maximumPriority] --;
                    // 가장 높은 우선순위 갱신
                    if (priorityCnts[maximumPriority] == 0) {
                        maximumPriority = 0;
                        for (int j=0; j<10; j++) {
                            if (priorityCnts[j] > 0) maximumPriority = Math.max(maximumPriority, j);
                        }
                    }
                } else {
                    queue.add(queue.poll());
                }
            }

            System.out.println(answer[targetIdx]);
        }
    }

}
