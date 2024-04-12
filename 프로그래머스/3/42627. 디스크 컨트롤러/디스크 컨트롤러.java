import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        // 시작 순서를 기준으로 오름차순
        Arrays.sort(jobs, (o1, o2) -> Integer.compare(o1[0], o2[0]));

        // 소요 시간 기준으로 오름차순
        PriorityQueue<int[]> executablePriorityQueue = new PriorityQueue<>((o1, o2) -> Integer.compare(o1[1], o2[1]));

        int waitTime = 0; // 모든 job들의 대기 시간
        int endTime = jobs[0][0]; // 가장 최근의 job이 끝난 시간
        int jobIndex = 0;
        int executedCnt = 0; // 수행된 job 카운터

        while (executedCnt < jobs.length) {
            // endTime보다 같거나 작은 모든 job을 선택
            while (jobIndex < jobs.length && jobs[jobIndex][0] <= endTime) {
                executablePriorityQueue.add(jobs[jobIndex]);
                jobIndex ++;
            }

            // 만약 아무것도 선택된 job이 없으면 현재 endTime보다 작은 startTime을 가지는 job이 없는것
            if (executablePriorityQueue.isEmpty()) {
                endTime = jobs[jobIndex][0];
                continue;
            }

            // 수행 가능한 job 중 가장 수행시간이 짧은것을 뽑아 수행
            int[] job = executablePriorityQueue.poll();
            int arrivedTime = job[0];
            int elapseTime = job[1];
            waitTime += endTime - arrivedTime;
            waitTime += elapseTime;
            endTime += elapseTime;
            executedCnt += 1;
        }

        return waitTime / jobs.length;
    }
}