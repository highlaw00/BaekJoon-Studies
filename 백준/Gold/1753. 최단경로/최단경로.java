import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int v = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());

        Node[] nodeList = new Node[v+1];
        for (int i = 0; i <= v; i++) {
            nodeList[i] = new Node(i);
        }

        int startSeq = Integer.parseInt(br.readLine());

        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int src = Integer.parseInt(st.nextToken());
            int dest = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            Node srcNode = nodeList[src];
            Node destNode = nodeList[dest];
            srcNode.connectedNodes.add(new Edge(srcNode, destNode, weight));
        }

        int[] distances = new int[v+1];
        for (int i = 0; i <= v; i++) {
            distances[i] = Integer.MAX_VALUE;
        }
        distances[startSeq] = 0;
        PriorityQueue<Pair> pq = new PriorityQueue<>((p1, p2) -> Integer.compare(p1.distance, p2.distance));
        pq.add(new Pair(startSeq, 0));

        while(!pq.isEmpty()) {
            Pair info = pq.poll();

            Node currNode = nodeList[info.sequence];
            if (info.distance > distances[currNode.sequence]) continue;
            int distanceToCurr = info.distance;

            for (Edge edge: currNode.connectedNodes) {
                Node nextNode = edge.dest;
//                if (visited[nextNode.sequence]) continue;

                int distanceBetweenCurrAndNext = edge.weight;
                int newDistance = distanceToCurr + distanceBetweenCurrAndNext;
                int oldDistance = distances[nextNode.sequence];

                if (newDistance < oldDistance) {
                    distances[nextNode.sequence] = newDistance;
                    pq.add(new Pair(nextNode.sequence, newDistance));
                }
            }
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 1; i <= v; i++) {
            if (distances[i] == Integer.MAX_VALUE) sb.append("INF");
            else sb.append(distances[i]);

            sb.append("\n");
        }

        System.out.println(sb);
    }

    class Node {
        int sequence;
        List<Edge> connectedNodes;
        Node(int sequence) {
            this.sequence = sequence;
            connectedNodes = new ArrayList<>();
        }
    }
    class Edge {
        Node src;
        Node dest;
        int weight;
        Edge(Node src, Node dest, int weight) {
            this.src = src;
            this.dest = dest;
            this.weight = weight;
        }
    }

    class Pair {
        int sequence;
        int distance;
        Pair(int sequence, int distance) {
            this.sequence = sequence;
            this.distance = distance;
        }
    }
}
