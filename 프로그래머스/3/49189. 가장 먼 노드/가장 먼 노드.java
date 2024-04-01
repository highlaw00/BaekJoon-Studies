import java.util.*;

class Solution {
    public int solution(int n, int[][] edges) {
        int answer = 0;
        
        // 사용할 리스트 초기화
        ArrayList<ArrayList<Integer>> graphs = new ArrayList<>();
        for (int i=0; i < n+1; i++) {
            ArrayList<Integer> arr = new ArrayList<>();
            graphs.add(arr);
        }
        
        for (int[] edge: edges) {
            int src = edge[0];
            int dest = edge[1];
            graphs.get(src).add(dest);
            graphs.get(dest).add(src);
        }
        
        ArrayList<Boolean> visited = new ArrayList<>();
        ArrayList<Integer> dist = new ArrayList<>();
        for (int i=0; i < n+1; i++) {
            visited.add(false);
            dist.add(-1);
        }
        
        // BFS 변수 초기화
        Queue<Integer> queue = new LinkedList<>();
        dist.set(1, 0);
        queue.add(1);
        visited.set(1, true);
        
        while (!queue.isEmpty()) {
            int currVertex = queue.poll();
            
            for (Integer nextVertex: graphs.get(currVertex)) {
                if (visited.get(nextVertex)) continue;
                dist.set(nextVertex, dist.get(currVertex) + 1);
                queue.add(nextVertex);
                visited.set(nextVertex, true);
            }
        }
        
        // dist 리스트 순회하며 maxValue의 개수 확인
        int maxValue = Collections.max(dist);
        answer = Collections.frequency(dist, maxValue);
        
        return answer;
    }
}