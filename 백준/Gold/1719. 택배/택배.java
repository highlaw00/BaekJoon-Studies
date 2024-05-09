import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Node[] nodes = new Node[n+1];
        for (int i = 0; i <= n; i++) {
            nodes[i] = new Node(i);
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int srcSeq = Integer.parseInt(st.nextToken());
            int destSeq = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            Node srcNode = nodes[srcSeq];
            Node destNode = nodes[destSeq];
            srcNode.connectedNodes.add(new Edge(destNode, weight));
            destNode.connectedNodes.add(new Edge(srcNode, weight));
        }

        int[][] routeTable = new int[n+1][n+1];

        for (int i = 1; i <= n; i++) {
            int[] distanceTable = initDistanceTable(n);
            // 각 노드에 대해 dijkstra 시작
            Node startNode = nodes[i];
            // distance, node # 를 포함하는 객체를 우선순위큐에 삽입
            PriorityQueue<Triple> pq = new PriorityQueue<>(
                    (o1, o2) -> Integer.compare(o1.distance, o2.distance)
            );
            pq.add(new Triple(startNode, startNode, 0));

            while (!pq.isEmpty()) {
                Triple t = pq.poll();
                Node callerNode = t.srcNode;
                Node destNode = t.destNode;
                int distance = t.distance;
                if (distance > distanceTable[destNode.seq]) continue;
                routeTable[i][destNode.seq] = getClosestNode(routeTable, i, callerNode.seq, destNode.seq);

                for (Edge edge: destNode.connectedNodes) {
                    Node nextNode = edge.dest;
                    int weight = edge.weight;
                    if (distanceTable[nextNode.seq] > distance + weight) {
                        distanceTable[nextNode.seq] = distance + weight;
                        pq.add(new Triple(destNode, nextNode, distanceTable[nextNode.seq]));
                    }
                }
            }
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i == j) sb.append("- ");
                else sb.append(routeTable[i][j] + " ");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }

    private int getClosestNode(int[][] routeTable, int rootSeq, int callerSeq, int calleeSeq) {
        // i -> j 까지의 경로 중 가장 먼저 만나는 노드의 인덱스를 구하는 함수
        // j를 호출한 노드가 i인 경우 그대로 반환
        if (rootSeq == callerSeq) return calleeSeq;
        else return routeTable[rootSeq][callerSeq];
        // j를 호출한 노드가 i가 아닌 경우 i -> k_1 -> ... -> k_t -> j
        // k_1을 재귀적으로 탐색
//        else return getClosestNode(routeTable, rootSeq, routeTable[rootSeq][callerSeq], callerSeq);
    }

    private int[] initDistanceTable(int n) {
        int[] distanceTable = new int[n+1];
        for (int i = 0; i <= n; i++) {
            distanceTable[i] = Integer.MAX_VALUE;
        }

        return distanceTable;
    }

    class Node {
        int seq;
        List<Edge> connectedNodes;
        Node(int seq) {
            this.seq = seq;
            this.connectedNodes = new ArrayList<>();
        }
    }

    class Edge {
        Node dest;
        int weight;
        Edge(Node dest, int weight) {
            this.dest = dest;
            this.weight = weight;
        }
    }

    class Triple {
        Node srcNode;
        Node destNode;
        int distance;
        Triple(Node srcNode, Node destNode, int distance) {
            this.srcNode = srcNode;
            this.destNode = destNode;
            this.distance = distance;
        }
    }
}
