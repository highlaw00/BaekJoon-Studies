import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        System.out.println(new Main().solution());
    }

    public int solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] srcDest = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int srcNode = srcDest[0], destNode = srcDest[1];
        int m = Integer.parseInt(br.readLine());

        // Node 초기화
        Node[] nodes = new Node[n+1];
        for (int i = 1; i <= n; i++) {
            nodes[i] = new Node(i);
        }

        // edges 초기화
        for (int i = 1; i <= m; i++) {
            int[] xy = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int x = xy[0], y = xy[1];
            // x는 y의 부모, y는 x의 자식
            nodes[x].edges.add(y);
            nodes[y].edges.add(x);
        }

        // BFS 시작
        Queue<Node> queue = new LinkedList<>();
        boolean[] visited = new boolean[n+1];
        int[] dists = new int[n+1];
        for (int i = 0; i <= n; i++) dists[i] = -1;
        queue.add(nodes[srcNode]);
        visited[srcNode] = true;
        dists[srcNode] = 0;

        while (!queue.isEmpty()) {
            Node currNode = queue.poll();
            for (int nextSeq: currNode.edges) {
                if (visited[nextSeq]) continue;
                visited[nextSeq] = true;
                dists[nextSeq] = dists[currNode.sequence] + 1;
                queue.add(nodes[nextSeq]);
            }
        }

        return dists[destNode];
    }

    class Node {
        int sequence;
        List<Integer> edges;
        public Node(int sequence) {
            this.sequence = sequence;
            this.edges = new ArrayList<>();
        }
    }
}
