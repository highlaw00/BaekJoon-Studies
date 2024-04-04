import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine());
        String line = sc.nextLine();
        int[] cards = Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(cards);

        int m = Integer.parseInt(sc.nextLine());
        int[] targets = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        for (int target: targets) {
            if (search(cards, target, 0, n-1)) {
                System.out.print("1 ");
            } else System.out.print("0 ");
        }
    }

    private static boolean search(int[] cards, int target, int s, int e) {
        if (s > e) return false;
        int m = (s + e) / 2;
        if (cards[m] == target) return true;
        else if (cards[m] > target) {
            e = m - 1;
        } else {
            s = m + 1;
        }
        return search(cards, target, s, e);
    }
}