import java.util.*;

class Solution {
    static int answer = Integer.MAX_VALUE;
    static int[] picks;
    static String[] minerals;
    static final String[] pickNames = {"diamond", "iron", "stone"};
    
    public int solution(int[] picksInput, String[] mineralsInput) {
        // picks: 곡괭이의 개수
        // minerals: 광물들의 순서
        // back tracking!
        picks = picksInput;
        minerals = mineralsInput;
        
        backTracking(picks, 0, 0);
        
        return answer;
    }
    
    void backTracking(int[] picks, int mineralIdx, int stress) {
        // base case
        if (isBaseCase(picks, mineralIdx)) {
            Solution.answer = Integer.min(Solution.answer, stress);
            return;
        }
        
        // 곡괭이를 기준으로 백트래킹
        for (int i = 0; i < picks.length; i++) {
            if (picks[i] == 0) continue;
            // 곡괭이 사용
            picks[i] -= 1;
            String currentPick = pickNames[i];
            // 해당 곡괭이로 최대 5개의 광물을 캤을 때 쌓이는 피로도
            int newStress = 0;
            // 가장 마지막으로 캐는 광물의 인덱스를 기록하는 변수
            int lastPickedMineralIdx = mineralIdx;
            for (; lastPickedMineralIdx < minerals.length; lastPickedMineralIdx++) {
                if (lastPickedMineralIdx >= mineralIdx + 5) break;
                newStress += getStressScore(currentPick, minerals[lastPickedMineralIdx]);    
            }
            
            backTracking(picks, lastPickedMineralIdx, stress + newStress);
            
            // 원복
            picks[i] += 1;
        }
        
        
    }
    
    boolean isBaseCase(int[] picks, int mineralIdx) {
        int remainPicks = Arrays.stream(picks).sum();
        return remainPicks == 0 || Solution.minerals.length <= mineralIdx;
    }
    
    int getStressScore(String pick, String mineral) {
        int score = 1;
        if (pick.equals("iron") && mineral.equals("diamond")) score = 5;
        else if (pick.equals("stone") && mineral.equals("iron")) score = 5;
        else if (pick.equals("stone") && mineral.equals("diamond")) score = 25;
        
        return score;
    }
    
}