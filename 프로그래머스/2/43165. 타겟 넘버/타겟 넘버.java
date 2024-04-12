class Solution {
    public static int answer = 0;

    public int solution(int[] numbers, int target) {
        back(numbers, new int[numbers.length], 0, target);
        return Solution.answer;
    }

    // Back Tracking 구현
    public void back(int[] numbers, int[] arr, int cnt, int target) {
        // 기저 사례
        if (cnt == arr.length) {
            int sum = 0;
            for (int i = 0; i < arr.length; i++) {
                sum += arr[i];
            }
            if (sum == target) Solution.answer += 1;
            return;
        }

        arr[cnt] = numbers[cnt];
        back(numbers, arr, cnt + 1, target);
        arr[cnt] = -numbers[cnt];
        back(numbers, arr, cnt + 1, target);
    }
}