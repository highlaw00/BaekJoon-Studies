import java.util.*;

class Solution {
    public boolean solution(String[] phoneBook) {
        Set<String> set = new HashSet<>();
        boolean answer = true;

        // 전화번호부를 길이순으로 오름차순 정렬
        Arrays.sort(phoneBook);

        // i번째 전화번호를...
        // map에 저장하고, i번째 전화번호[len(i번째)-2]까지 늘려가며 map에 존재하는지 확인
        for (String phoneNumber: phoneBook) {
            set.add(phoneNumber);
            for (int i=1; i<phoneNumber.length(); i++) {
                String subPhoneNumber = phoneNumber.substring(0, i);
                if (set.contains(subPhoneNumber)) {
                    answer = false;
                    break;
                }
            }
        }
        
        return answer;
    }
}