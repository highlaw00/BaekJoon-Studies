import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] line = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int n = line[0];
        int m = line[1];
        int l = line[2];
        
        int[] spots = new int[m+1];
        int last = 0;
        for (int i = 0; i < m; i ++) {
            int spot = Integer.parseInt(br.readLine());
            spots[i] = spot - last;
            last = spot;
        }
        spots[m] = l - last;
        
        for (int i = 0; i < n; i ++) {
            int q = Integer.parseInt(br.readLine());
            int left = 1;
            int right = l;
            int ans = 0;
            
            while (left <= right) {
                int mid = (left + right) / 2;
                // 최적해가 mid일 때를 가정
                // mid 이상의 조각이 q + 1개 나와야한다.
                
                // 가능하다면 갱신해주고 더 큰 범위를 탐색
                if (isPossible(spots, mid, q)) {
                    ans = Math.max(ans, mid);
                    left = mid + 1;
                } else { // 불가능하다면 더 작은 범위를 탐색
                    right = mid - 1;
                }
            }
            
            System.out.println(ans);
        }
    }
    
    public static boolean isPossible(int[] spots, int x, int q) {
        // x 이상의 조각이 (q + 1)개 나오는지 반환
        int sliceCnt = 0;
        int partialSum = 0;
        for (int i=0; i<spots.length; i++) {
            partialSum += spots[i];
            
            if (partialSum >= x) {
                sliceCnt += 1;
                partialSum = 0;
            }
        }
        
        return sliceCnt >= q + 1;
    }
}