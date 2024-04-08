import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        // 각 원소를 비교하여 최종 문자열 반환
        Integer[] newNumbers = new Integer[numbers.length];
        for (int i=0; i < numbers.length; i ++) newNumbers[i] = numbers[i];
        Arrays.sort(newNumbers, myComp);
        
        // 모든 원소가 0인 경우는 제외
        boolean isZero = true;
        for (int num: newNumbers) {
            if (num != 0) {
                isZero = false;
                break;
            }
        }
        
        if (isZero) return "0";
        
        StringBuilder builder = new StringBuilder();
        for (int num: newNumbers) builder.append(num);
        
        return builder.toString();
    }
    
    public static Comparator<Integer> myComp = new Comparator<>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            String s1 = Integer.toString(o1);
            String s2 = Integer.toString(o2);
            Integer s1ConcatS2 = Integer.parseInt(s1 + s2);
            Integer s2ConcatS1 = Integer.parseInt(s2 + s1);
            // 더 큰 녀석이 앞에 와야한다. == 내림차순

            if (s1ConcatS2 > s2ConcatS1) return -1;
            else if (s1ConcatS2 == s2ConcatS1) return 0;
            else return 1;
        }
    };
}
