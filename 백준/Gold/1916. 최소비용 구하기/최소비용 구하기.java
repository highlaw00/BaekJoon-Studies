import java.util.*;
import java.io.*;

/*
    n개의 정점과 m개의 단방향 간선
    - a에서 b까지 갈 때 드는 버스 비용의 최소화
    - 다익스트라 알고리즘을 사용

    다익스트라 알고리즘
    - 시작 정점을 선택한다.
    - 인접한 노드 중 방문하지 않았으며 거리가 가장 가까운 정점을 선택한다.
    - 해당 정점에서 다시 방문하지 않았으며 거리가 가장 가까운 정점을 선택한다.
 */

public class Main {
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        // i번째 도시에서 j번째 도시로 갈 때의 가중치값을 가지는 자료구조
        ArrayList<ArrayList<Pair>> edges = new ArrayList<>();
        for (int i = 0; i <= n; i ++) edges.add(new ArrayList<>());
        for (int i = 0; i < m; i ++) {
            // src, dest, val
            String[] line = br.readLine().split(" ");
            int src = Integer.parseInt(line[0]);
            int dest = Integer.parseInt(line[1]);
            int val = Integer.parseInt(line[2]);
            edges.get(src).add(new Pair(dest, val));
        }
        String[] line = br.readLine().split(" ");
        int src = Integer.parseInt(line[0]);
        int finalDest = Integer.parseInt(line[1]);

        int[] dist = new int[n+1]; // 시작지점부터의 거리를 저장하는 배열
        boolean[] visited = new boolean[n+1]; // 방문 여부 배열

        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return Integer.compare(o1[0], o2[0]);
            }
        });
        // src부터의 거리, 정점 번호
        pq.add(new int[]{0, src});

        while (!pq.isEmpty()) {
            int[] info = pq.poll();
            int currWeight = info[0];
            int node = info[1];

            if (visited[node]) continue;
            visited[node] = true;
            dist[node] = currWeight;
            if (node == finalDest) break;

            for (Pair pair: edges.get(node)) {
                int dest = pair.dest;
                int nextWeight = pair.val;
                if (!visited[dest]) pq.add(new int[]{currWeight + nextWeight, dest});
            }
        }

        System.out.println(dist[finalDest]);
    }

    class Pair {
        public int dest;
        public int val;
        public Pair(int dest, int val) {
            this.dest = dest;
            this.val = val;
        }
    }
}
