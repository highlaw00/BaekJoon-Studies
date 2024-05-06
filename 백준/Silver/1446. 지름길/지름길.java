import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()), d = Integer.parseInt(st.nextToken());

        // 정점들의 Map 선언
        Map<Integer, Node> nodeMap = new HashMap<>();
        nodeMap.put(0, new Node(0));
        nodeMap.put(d, new Node(d));

        // 지름길 입력
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int src = Integer.parseInt(st.nextToken()), dest = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            if (!nodeMap.containsKey(src)) nodeMap.put(src, new Node(src));
            if (!nodeMap.containsKey(dest)) nodeMap.put(dest, new Node(dest));
            Node srcNode = nodeMap.get(src);
            Node destNode = nodeMap.get(dest);
            srcNode.connectedNodes.add(new Edge(srcNode, destNode, weight));
        }

        // 정점 정렬
        List<Node> nodeList = new ArrayList<>();
        for (Integer key: nodeMap.keySet()) {
            Node node = nodeMap.get(key);
            nodeList.add(node);
        }

        Collections.sort(nodeList, (n1, n2) -> {
            return Integer.compare(n1.sequence, n2.sequence);
        });

        for (int i = 0; i < nodeList.size(); i++) {
            Node node = nodeList.get(i);
            for (int j = i+1; j < nodeList.size(); j++) {
                Node nextNode = nodeList.get(j);
                int weight = nextNode.sequence - node.sequence;
                node.connectedNodes.add(new Edge(node, nextNode, weight));
            }
        }

        // 다익스트라 시작
        PriorityQueue<Node> pq = new PriorityQueue<>((n1, n2) -> Integer.compare(n1.distance, n2.distance));
        Node rootNode = nodeList.get(0);
        rootNode.distance = 0;
        pq.add(rootNode);

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            if (node.visited) continue;
            for (Edge edge: node.connectedNodes) {
                Node nextNode = edge.dest;
                if (nextNode.visited) continue;
                if (node.distance + edge.weight < nextNode.distance) {
                    nextNode.distance = node.distance + edge.weight;
                    pq.add(nextNode);
                }
            }
            node.visited = true;
        }

        for (Node node: nodeList) {
            if (node.sequence == d) System.out.println(node.distance);
        }
    }

    class Node {
        int sequence;
        List<Edge> connectedNodes;
        int distance;
        boolean visited;
        Node(int sequence) {
            this.sequence = sequence;
            this.connectedNodes = new ArrayList<>();
            this.distance = Integer.MAX_VALUE;
            this.visited = false;
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
}
