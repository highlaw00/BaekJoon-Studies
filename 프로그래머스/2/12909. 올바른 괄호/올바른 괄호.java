import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Stack<Character> stack = new Stack<>();
        
        // 문자열을 반복합니다.
        
        for (int i = 0; i < s.length(); i ++) {
            Character currentChar = s.charAt(i);
            // '('를 만난 경우, stack에 삽입
            if (currentChar == '(') {
                stack.push(currentChar);
                continue;
            }
            
            // ')'를 만난 경우, stack.top 확인
            if (stack.isEmpty()) {
                answer = false;
                break;
            }
            
            // - '('가 top에 있는 경우 ok
            if (stack.peek() == '(') {
                stack.pop();
            } 
            // - '('가 top에 없는 경우 ... not ok
            else {
                answer = false;
                break;
            }
        }
        
        // 모든 반복이 끝나고 stack에 무언가 남아있다면 not ok
        if (stack.size() > 0) answer = false;
        
        return answer;
    }
}