import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        
        // 0 ~ n-1 까지의 노드를 순차적으로 탐색
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                answer++;
                bfs(computers, visited, i, n);
            }
        }
        
        return answer;
    }
    
    public void bfs(int[][] computers, boolean[] visited, int root, int n) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            int currNode = queue.poll();
            if (visited[currNode]) continue;
            visited[currNode] = true;
            // currNode와 연결된 노드 확인
            for (int i = 0; i < n; i++) {
                // 연결되어있고 방문하지 않은 경우
                if (computers[currNode][i] == 1 && !visited[i]) {
                    queue.add(i);
                }
            }
        }
    }
}