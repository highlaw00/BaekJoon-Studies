import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        PriorityQueue<ArrayList<Integer>> pq = new PriorityQueue<>(startTimeAscending);
        for (int i=0; i<jobs.length; i++) {
            ArrayList<Integer> arr = new ArrayList<>(Arrays.asList(jobs[i][0], jobs[i][1]));
            pq.add(arr);
        }
        int curr = pq.peek().get(0); // 현재 시각 최초의 job이 수행 시작 시간
        int answer = 0;
        while (!pq.isEmpty()) {
            PriorityQueue<ArrayList<Integer>> executable = new PriorityQueue<>(elapseTimeAscending);
            // 현재 수행할 수 있는 job을 여러개 뽑는다.
            while (!pq.isEmpty() && pq.peek().get(0) <= curr) {
                executable.add(pq.poll());
            }
            
            if (executable.isEmpty()) executable.add(pq.poll());

            // 수행할 수 있는 job 중 수행 시간이 가장 짧은 job을 선택한다.
            ArrayList<Integer> pair = executable.poll();
            int arrivedTime = pair.get(0);
            int elapseTime = pair.get(1);
            if (arrivedTime > curr) {
                curr = arrivedTime;
            }
            answer += (curr - arrivedTime); // 대기 시간 누적
            answer += elapseTime; // 소요 시간 누적
            curr += elapseTime; // 현재 시간 갱신

            while (!executable.isEmpty()) {
                pq.add(executable.poll());
            }
        }

        return answer / jobs.length;
    }

    public Comparator<ArrayList<Integer>> startTimeAscending = new Comparator<>() {
        @Override
        public int compare(ArrayList<Integer> o1, ArrayList<Integer> o2) {
            if (o1.get(0) > o2.get(0)) return 1;
            else if (o1.get(0) == o2.get(0)) {
                if (o1.get(1) > o2.get(1)) return 1;
                else if (o1.get(1) == o2.get(1)) return 0;
                else return -1;
            } else return -1;
        }
    };

    public Comparator<ArrayList<Integer>> elapseTimeAscending = new Comparator<>() {
        @Override
        public int compare(ArrayList<Integer> o1, ArrayList<Integer> o2) {
            if (o1.get(1) > o2.get(1)) return 1;
            else if (o1.get(1) == o2.get(1)) {
                if (o1.get(0) > o2.get(0)) return 1;
                else if (o1.get(0) == o2.get(0)) return 0;
                else return -1;
            } else return -1;
        }
    };
}