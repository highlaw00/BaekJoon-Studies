import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        System.out.println(new Main().solution());
    }

    public int solution() throws IOException {
        int n = Integer.parseInt(br.readLine()); // 정점 수
        int m = Integer.parseInt(br.readLine()); // 에지 수

        Node[] nodeList = new Node[n+1];
        for (int i = 0; i <= n; i++) {
            nodeList[i] = new Node(i);
        }

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int src = Integer.parseInt(st.nextToken());
            int dest = Integer.parseInt(st.nextToken());
            Node srcNode = nodeList[src];
            Node destNode = nodeList[dest];
            srcNode.connectedNodes.add(destNode);
            destNode.connectedNodes.add(srcNode);
        }

        // 1번에서 BFS 하여 방문한 정점 기록
        boolean[] visited = new boolean[n+1];
        Queue<Node> queue = new LinkedList<>();
        queue.add(nodeList[1]);
        visited[1] = true;

        while (!queue.isEmpty()) {
            Node currentNode = queue.poll();
            for (Node nextNode: currentNode.connectedNodes) {
                int nextNodeSeq = nextNode.sequence;
                // 이미 방문한 경우
                if (visited[nextNodeSeq]) continue;
                queue.add(nextNode);
                visited[nextNodeSeq] = true;
            }
        }

        int answer = 0;
        for (boolean visitedBool: visited) {
            if (visitedBool) answer++;
        }

        return answer - 1;
    }

    class Node {
        int sequence;
        List<Node> connectedNodes;
        Node(int sequence) {
            this.sequence = sequence;
            connectedNodes = new ArrayList<>();
        }
    }
}
