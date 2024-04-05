import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] nums = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int m = nums[0];
        int n = nums[1];
        
        int[] lens = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(lens);
        
        // 길이가 x인 막대 과자를 선택
        int left = 1;
        int right = 1_000_000_000;
        int answer = 0;
        
        while (left <= right) {
            int mid = (left + right) / 2;
            // 길이가 x인 막대 과자를 몇개 나눌 수 있는지 확인
            int cnt = 0;
            for (int i = 0; i < n; i ++) {
                int dividableCnt = lens[i] / mid;
                cnt += dividableCnt;
            }
            
            // 모두에게 나눠줄 수 있다면 탐색 범위를 (mid + 1, right) 로 변경
            // 모두에게 나눠줄 수 없다면 탐색 범위를 (left, mid - 1) 로 변경
            if (cnt >= m) {
                answer = Math.max(answer, mid);
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        System.out.println(answer);
    }
}