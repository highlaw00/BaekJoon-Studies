import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        boolean[] isCycle = new boolean[n+1];
        boolean[] isVisited = new boolean[n+1];
        int[] distances = new int[n+1];
        List<Map<Integer, Edge>> nodes = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            nodes.add(new HashMap<>());
        }

        for (int i = 0; i < n; i++) {
            String[] line = br.readLine().split(" ");
            int src = Integer.parseInt(line[0]), dest = Integer.parseInt(line[1]);
            nodes.get(src).put(dest, new Edge());
            nodes.get(dest).put(src, new Edge());
        }

        for (int i = 1; i <= n; i++) {
            // 사이클에 포함되지 않은 정점에 대해서 dfs
            if (isCycle[i]) continue;
            isVisited[i] = true;
            dfs(i, i, nodes, isCycle, isVisited);
            isVisited[i] = false;
        }

        for (int i = 1; i <= n; i++) {
            // 사이클에 포함된 정점의 경우 순환선과의 거리가 0
            if (isCycle[i]) continue;

            // 사이클에 포함되지 않은 정점의 경우 순환선과의 거리를 bfs로 해결한다.
            distances[i] = bfs(i, nodes, isCycle, n);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            sb.append(distances[i]);
            sb.append(" ");
        }
        System.out.println(sb);
    }

    public boolean dfs(int ancestor, int current, List<Map<Integer, Edge>> nodes, boolean[] isCycle, boolean[] isVisited) {
        // 연결된 모든 정점 확인
        for (int dest: nodes.get(current).keySet()) {
            Edge edge = nodes.get(current).get(dest);

            // 이용한 간선이라면 무시
            if (edge.isUsed) continue;

            // 조상이라면 여지껏 방문했던 모든 정점 갱신
            if (dest == ancestor) {
                for (int i = 1; i < isVisited.length; i++) {
                    if (isVisited[i]) isCycle[i] = true;
                }
                return true;
            }
            // 만약 이미 방문한 정점이라면 무시
            if (isVisited[dest]) continue;

            // 재귀
            Edge otherEdge = nodes.get(dest).get(current);
            otherEdge.isUsed = true;
            edge.isUsed= true;
            isVisited[dest] = true;

            boolean result = dfs(ancestor, dest, nodes, isCycle, isVisited);

            otherEdge.isUsed = false;
            edge.isUsed= false;
            isVisited[dest] = false;

            // 사이클에 포함되는 경우 재귀 종료
            if (result) return true;
        }

        return false;
    }

    public int bfs(int root, List<Map<Integer, Edge>> nodes, boolean[] isCycle, int totalNode) {
        int result = 0;

        Queue<Integer> queue = new LinkedList<>();
        boolean[] isVisited = new boolean[totalNode + 1];
        int[] distances = new int[totalNode + 1];
        queue.add(root);
        isVisited[root] = true;

        while (!queue.isEmpty()) {
            int src = queue.poll();
            for (int dest: nodes.get(src).keySet()) {
                if (isVisited[dest]) continue;
                distances[dest] = distances[src] + 1;
                if (isCycle[dest]) {
                    result = distances[dest];
                    break;
                }
                isVisited[dest] = true;
                queue.add(dest);
            }
        }

        return result;
    }

    class Edge {
        boolean isUsed;
        Edge() {
            isUsed = false;
        }
    }
}
